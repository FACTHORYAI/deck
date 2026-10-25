# The fidelity corpus (W6)

How faithfully Facthory Deck opens, saves and draws real `.pptx` files that PowerPoint wrote, as a
pass rate per step. Part of the Facthory patch set (`facthory/README.md`).

## The files

`corpus.toml` lists 71 files (64.1 MB), each one pinned by URL (a commit or a fixed
public-sector address) and SHA-256. **None is committed**: upstream's rule ("never commit files
produced by PowerPoint") holds, and the runner fetches them into a cache and checks them against
their pin.

- **Microsoft-made:** each file was written by PowerPoint, checked by `docProps/app.xml` and by
  traces only Office writes (`scan.py`).
- **Licences:** MIT 42, Apache-2.0 19, CC0-1.0 (US federal public domain) 6, CC-BY-4.0 1, Open Government Licence v3.0 (NHS Digital; portal record says CC-BY) 1, European Parliament reuse (portal record COM_REUSE: reproduction authorised, source acknowledged) 1, Open Government Licence v3.0 1. Each entry records its licence and where it was read.
- **Tiers:** `smoke` (20 small, feature-dense files whose renders may be published) and
  `full` (all).
- **Review:** `publish_renders = "review"` (21 files: user attachments, logos, names) need a
  content check before even our renders of them are shown publicly.
- **Mirrors:** public-sector entries marked `mirror = "required"` change at their origin; a copy
  belongs in our own bucket once it exists.

**Owner decision:** upstream's contributor rules (DeckCraft's `AGENTS.md`) allow only decks its
contributors made, and never publishing PowerPoint screenshots. This distribution measures
openly licensed third-party decks, fetched by pin and never committed, and publishes only our
own renders and the scores, never PowerPoint's. If Facthory keeps upstream's rule instead, the
corpus becomes a commissioned set Bandpey makes and owns (see "Adding files").

## Running it

```sh
python3 facthory/rebrand.py apply      # on a fresh checkout
cargo build --release -p facthorydeck-cli
python3 facthory/corpus/fidelity.py --cli target/release/facthorydeck-cli --tier smoke
```

`.github/workflows/facthory-fidelity.yml` runs it weekly over every file, by hand over a tier,
and on pull requests that change the corpus over the smoke tier. The pass rates are the job's
summary; `report.json` and `report.md` are its artifact.

| Step | Passes when |
| ---- | ----------- |
| open | `info`: the presentation opens |
| save | `convert` to `.pptx` |
| roundtrip | the saved file opens and its outline (`convert` to `.md`, word by word) is the original's |
| render | `convert` to PDF |
| pages | with `--reference`: our PDF has as many slides as PowerPoint's |

A crash (a panic or a signal) or a step over the time limit fails the file. A file passes when
every step it ran passed. A step with nothing to check (a presentation without slides has
nothing to render) is skipped and counts neither way.

## Microsoft's renders

Comparing with PowerPoint's own output needs PowerPoint. A person with a Microsoft 365 licence
exports each file on one fixed Windows machine: black-box, open, export, close, never looking
inside Office. The environment is held constant and recorded per run:
- the default printer (Microsoft Print to PDF) and its resolution;
- the Office build, with updates paused;
- the fonts, by hash;
- the proofing languages and regional format.

The exports go to a private bucket, never into git. `fidelity.py --reference DIR`, with
`DIR/<id>.pdf`, then compares page counts. PDFs compare by slide count. A per-slide PNG comparison (SSIM and differing pixels) is still to build; PowerPoint's references come as PDF plus one PNG per slide at 1920 px. Reports publish our renders and the
scores; PowerPoint's pages and diff overlays stay private.

## The bar for "ready" (proposed; the owner sets it after the first full run)

- **Open and round trip:** at least 98% of files open and round-trip, none crashes, and PowerPoint opens our save without offering a repair.
- **Render:** per-slide SSIM of at least 0.95 on 90% of slides (a comparison step still to build, shaped like page's `visual-diff`).

## Adding files

Run `scan.py` (`python3 -I facthory/corpus/scan.py DIR > files.jsonl`) to see each candidate's
producer, Office traces, SHA-256 and features. Add an entry only for a file PowerPoint wrote, under
a licence that allows keeping and showing it. Pin a commit or a stable URL.

Thin spots a commissioned set, made in Microsoft 365 and released by Bandpey under CC0, would
fill: right-to-left and CJK content, Aptos and the 2023 theme, embedded fonts, large documents.
