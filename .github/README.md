<p align="center">
  <img src="../facthory/icons/app-icon/hicolor/256x256/apps/com.facthory.deck.png" width="128" height="128" alt="Facthory Deck icon: a slide with rising bars on a slate tile">
</p>

# Facthory Deck

An open-source presentation app for macOS, Windows and Linux that opens and saves `.pptx`
decks, from [Facthory](https://facthory.com). Slide masters and layouts, shapes, tables, charts,
animations and transitions, presenter view and slide shows; every command is also available to
scripts and AI agents through a command-line tool and an MCP server.

Facthory Deck is based on [DeckCraft](https://github.com/storytold/deckcraft) by the ArtCraft
team, and follows it closely: this repository carries DeckCraft's history, merges every DeckCraft
release, and offers fixes back. Facthory's changes are a small set of brand files in
[`facthory/`](../facthory/README.md), applied when the app is built.

Upstream calls DeckCraft alpha, heading for beta: expect gaps and rough edges, and keep the
originals of decks that matter to you.

Downloads arrive with the first release. Until then, build it from source.

## Build

```sh
python3 facthory/rebrand.py apply   # on a fresh checkout: the Facthory brand
cargo build --release -p facthorydeck -p facthorydeck-cli
```

`facthory/rebrand.py apply` rewrites the checkout in place (names, app ids, icons, links,
installer identities); run it on a clean clone, not on a tree you commit from. Without it you
build DeckCraft as upstream ships it. The Linux build needs the packages listed in
[`.github/workflows/facthory.yml`](workflows/facthory.yml).

## Report a problem

[Open an issue](https://github.com/FACTHORYAI/deck/issues). Problems that also occur in
DeckCraft are reported there too, so the fix reaches both.

## Licence

MIT OR Apache-2.0, as upstream: [`LICENSE-MIT`](../LICENSE-MIT), [`LICENSE-APACHE`](../LICENSE-APACHE),
[`NOTICE`](../NOTICE) and [`ATTRIBUTION.md`](../ATTRIBUTION.md). Copyright © Bandpey GmbH for the
Facthory changes; DeckCraft is copyright © the ArtCraft Team and the DeckCraft contributors.
"ArtCraft" and its logos are trademarks of the ArtCraft Team; Facthory Deck is not an ArtCraft
product and is not endorsed by the ArtCraft Team.
