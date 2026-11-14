#!/usr/bin/env python3
"""Tests of sync.py's merge on throwaway repositories: an upstream release that deletes a directory
we edited a file of completes without stopping, and an unlisted conflict still stops.

  python3 facthory/test_sync.py
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sync  # noqa: E402

REMOVED = [".github/dependabot.yml", "crates/hevc/"]


def run(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@example.com", "-c", "commit.gpgsign=false", *args],
        cwd=cwd, capture_output=True, text=True, check=True,
    ).stdout


def write(root: Path, rel: str, text: str) -> None:
    (root / rel).parent.mkdir(parents=True, exist_ok=True)
    (root / rel).write_text(text, encoding="utf-8")


class MergeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        run(self.root, "init", "-q", "-b", "main")
        write(self.root, "crates/hevc/src/filter.rs", "a\nb\nc\n")
        write(self.root, "crates/hevc/src/lib.rs", "lib\n")
        write(self.root, "crates/geom/lib.rs", "geom\n")
        run(self.root, "add", "-A")
        run(self.root, "commit", "-qm", "upstream v0.18.1")
        run(self.root, "checkout", "-qb", "up")
        # Upstream's next release deletes the crate.
        run(self.root, "rm", "-qr", "crates/hevc")
        write(self.root, "crates/geom/lib.rs", "geom 2\n")
        run(self.root, "add", "-A")
        run(self.root, "commit", "-qm", "upstream v0.19.0")
        run(self.root, "update-ref", "refs/upstream-tags/v0.19.0", "HEAD")
        run(self.root, "checkout", "-q", "main")
        # Our in-tree commit edits a file of the crate.
        write(self.root, "crates/hevc/src/filter.rs", "a\nB\nc\n")
        run(self.root, "commit", "-qam", "Deck: hevc guard")
        self._root = sync.ROOT
        sync.ROOT = self.root

    def tearDown(self) -> None:
        sync.ROOT = self._root
        self.tmp.cleanup()

    def test_upstream_deletion_of_a_directory_we_edited_merges(self) -> None:
        self.assertEqual(sync.next_release(), "v0.19.0")
        self.assertEqual(sync.merge("v0.19.0", "DeckCraft", REMOVED), [])
        self.assertFalse((self.root / "crates/hevc").exists())
        self.assertEqual((self.root / "crates/geom/lib.rs").read_text(), "geom 2\n")
        self.assertEqual(run(self.root, "status", "--porcelain"), "")
        self.assertEqual(len(run(self.root, "rev-list", "--parents", "-1", "HEAD").split()), 3)
        self.assertIsNone(sync.next_release())

    def test_unlisted_conflict_still_stops_and_aborts(self) -> None:
        self.assertEqual(sync.merge("v0.19.0", "DeckCraft", [".github/dependabot.yml"]), ["crates/hevc/src/filter.rs"])
        self.assertEqual(run(self.root, "status", "--porcelain"), "")
        self.assertTrue((self.root / "crates/hevc/src/filter.rs").exists())

    def test_is_removed(self) -> None:
        self.assertTrue(sync.is_removed("crates/hevc/src/x.rs", REMOVED))
        self.assertTrue(sync.is_removed(".github/dependabot.yml", REMOVED))
        self.assertFalse(sync.is_removed("crates/hevc2/x.rs", REMOVED))
        self.assertFalse(sync.is_removed("crates/geom/lib.rs", REMOVED))


if __name__ == "__main__":
    unittest.main()
