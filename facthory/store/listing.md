# Microsoft Store listing: Facthory Deck

Draft for W9, 2026-10-25. Listing language: English (United States). Product type in Partner Center: **EXE or MSI app**. Everything in a `text` block is ready to paste; the counts beside each heading were measured on the block. Field limits are from Partner Center's MSI/EXE submission checklist ([create-app-submission](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/msi/create-app-submission), updated 2026-08-24) and Store Policies 7.20 ([store-policies](https://learn.microsoft.com/en-us/windows/apps/publish/store-policies), effective 2026-10-22).

Facts come from the app's own docs (this repository: README, ROADMAP, docs/gaps.md, docs/file-format-parity.md, docs/localization-parity.md) and the brand patch set (`facthory/brand.toml`). The tree still says DeckCraft; this listing uses only the Facthory name, except the credit.

## Recommendation: submit Deck after its beta gates, not with Page and Grid

Upstream calls Deck "alpha, heading for beta" (about 55 % ready for real work, `README.md`). Its own work list (`docs/gaps.md`, 2026-10-18) names beta blockers that a Store certification tester can hit in minutes:

- **Closing an edited presentation discards it without asking** (storytold/deckcraft#60, fix in storytold/deckcraft#75). Silent data loss.
- **Startup crashes on some Windows GPUs** (storytold/deckcraft#40, storytold/deckcraft#59).
- **No printing** (storytold/deckcraft#6), and pasting a picture from the clipboard fails on Windows (storytold/deckcraft#53).

Microsoft's MSI certification guidance says "Submit your app only when it's finished" and Policy 10.4.2 requires apps to "start up promptly" and "not close unexpectedly" ([certification process](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/msi/app-certification-process)). Recommended: reserve the name with the other two (after counsel), submit when storytold/deckcraft#60 and the Windows startup crash are closed and printing exists, and re-check the limits paragraph below against `docs/gaps.md` on that day. The owner decides (see [the owner checklist](https://github.com/FACTHORYAI/page/blob/main/facthory/launch/owner-checklist.md), open questions).

## Blockers before this listing can be submitted

| # | Blocker | Owner |
| - | ------- | ----- |
| 1 | Counsel signs off "Facthory Deck" (W0 and the opposition against FACTHORY) | Owner |
| 2 | `https://facthory.com/deck` and the privacy policy page are live | Owner publishes; Claude can draft the pages |
| 3 | A signed Facthory Deck MSI (x64 and ARM64) on an immutable, versioned GitHub release URL | Claude (pipeline) and owner (signing identity) |
| 4 | ~~The in-app updater (W4) ships in that MSI~~ Done: FACTHORYAI/deck#5. The Store does not update MSI apps, so the updater must stay on in the Store's copy (it is: the Store installs the same MSI) | Resolved |
| 5 | The beta blockers above are closed | Upstream and Claude (fixes go upstream first) |
| 6 | Screenshots rendered from the branded build | Claude |

## Product name

| Field | Limit | Value |
| ----- | ----- | ----- |
| Product name | Must be a reserved name; up to 256 characters; no marketing or descriptive text (Policy 10.1.1) | `Facthory Deck` |

Never "Deck" alone, never with "PowerPoint" (§14.6).

## Short description (<!--n:short-->235<!--/--> characters; limit 1,000, keep under 270)

<!-- block:short -->
```text
Design slides and present them full screen, with themes, shapes, charts, transitions and animations. Facthory Deck opens and saves .pptx files, works fully offline, needs no account and collects no data about you. Free and open source.
```

## Description (<!--n:desc-->2,957<!--/--> characters; limit 10,000; plain text, no URLs or HTML)

<!-- block:desc -->
```text
Facthory Deck is a free, open-source presentation app for Windows. It opens and saves .pptx presentations, works fully offline and needs no account. The ribbon, slide panel, layouts and keyboard shortcuts work the way presenters expect.

WHAT YOU CAN DO TODAY
• Build decks: slide masters and eleven layouts with placeholders, eight original themes with colour and font schemes, sections, speaker notes, comments, headers and footers, and custom slide sizes.
• Draw: more than 150 preset shapes with adjustment handles, connectors that stay attached, freeform and curve tools, merged shapes, gradient, picture and pattern fills, and shadows, glow, soft edges and reflections.
• Write: in-place text editing with full font and paragraph formatting, bullets and numbering, columns, autofit, vertical text, fields and hyperlinks.
• Add content: pictures with crop and corrections, tables with styles, charts, basic diagrams, and audio and video (MP3, AAC, FLAC, Ogg, Opus, WAV, AIFF; H.264, HEVC, VP9 and AV1).
• Present: transitions, including shape-morphing transitions, entrance, emphasis, exit and motion-path animations, builds by paragraph, full-screen slide show, presenter view, a pen for drawing on slides, rehearsed timings and media playback.
• Share: export PDF (slides, notes pages or handouts, with selectable text), PNG and JPEG images, an animated GIF of the deck, and an outline.
• Recover: unsaved work is kept automatically and offered again after a crash.
• Automate: more than 200 commands, all available from a command-line tool and a built-in MCP server, so scripts and AI agents that you run on your own computer can build and edit presentations. No AI is built into the app.
• Dark mode.

PRIVATE BY DESIGN
Facthory Deck has no telemetry, no crash reporting, no advertising and no account. Your presentations stay on your computer, and the app does not send them anywhere. The only connection it makes on its own is a daily check with its release page on GitHub for a newer version.

GOOD TO KNOW
Facthory Deck is an early release and still maturing. Presentations made in other apps may not look exactly the same yet. Printing is not available yet: export a PDF and print that. SVG pictures do not display yet, fonts are limited to regular, bold and italic styles, and the presenter view does not yet move to a second display by itself. Legacy .ppt files, OpenDocument presentations and macro-enabled presentations cannot be opened; templates (.potx) and slide shows (.ppsx) open as presentations and are saved as .pptx. The interface is in English only. Keep a copy of important presentations while you try it, and tell us what does not work: every report helps.

OPEN SOURCE
Facthory Deck is open source under the MIT License or the Apache License 2.0, at your option. It is published by Bandpey GmbH (Facthory), Munich, and is based on DeckCraft by the ArtCraft team. Source code, release notes and the issue tracker are on GitHub.
```

Notes on the text:
- No Microsoft product name appears; formats are named by extension. Microsoft's feature names are avoided: "Morph" is written "shape-morphing transitions", SmartArt "basic diagrams", AutoRecover "unsaved work is kept automatically".
- ALAC is left out of the audio list on purpose (it is Apple's codec name; the README lists it and it can be added back).
- Limitations from `docs/gaps.md` (#4 SVG, #5 English only, #6 printing, #7 font faces, #9 presenter view on a second display) and `docs/file-format-parity.md` (no `.ppt`, `.odp` or `.pptm`; `.potx` and `.ppsx` written as `.pptx`). Re-check every sentence against `docs/gaps.md` on the day of submission, and drop the ones that are fixed.
- Deck's own file format becomes `.facthorydeck` in our build (`facthory/brand.toml`); the listing does not need to mention it.

## Product features (<!--lines:features-->10<!--/--> features, longest <!--max:features-->80<!--/--> characters; limit 20 features of 200 characters, no bullets)

<!-- block:features -->
```text
Opens and saves .pptx presentations; opens .potx templates and .ppsx slide shows
Slide masters, eleven layouts and eight original themes
More than 150 shapes, connectors, freeform drawing and merged shapes
Transitions and entrance, emphasis, exit and motion-path animations
Full-screen slide show with presenter view, pen and rehearsed timings
Pictures, tables, charts, audio and video on your slides
Exports PDF, PNG, JPEG, animated GIF and outlines
Works fully offline: no account, no telemetry, no crash reporting
Scripts and local AI agents can build slides through a CLI and an MCP server
Free and open source under MIT or Apache-2.0
```

## Search terms (<!--lines:keywords-->7<!--/--> terms, <!--words:keywords-->11<!--/--> unique words, longest <!--max:keywords-->14<!--/--> characters; limit 7 terms, 40 characters each, 21 unique words; Policy 10.1.3: no pricing terms, no other products' titles)

<!-- block:keywords -->
```text
presentation
slides
pptx editor
slide show
presenter view
animations
open source
```

Left out on purpose: "free" (pricing term), every Microsoft, Google, Apple or LibreOffice product name (Keynote, Impress and others), and "office". "slides" is a generic word, but Google's product is called Google Slides; replace it with "slideshow maker" if counsel prefers.

## Category (Properties page)

| Field | Value | Why |
| ----- | ----- | --- |
| Category | **Productivity** | |
| Secondary category | **Business**, subcategory blank | |

## System requirements

Properties page checkboxes:

| Item | Minimum | Recommended |
| ---- | ------- | ----------- |
| Keyboard | ✓ | ✓ |
| Mouse | ✓ | ✓ |
| Touch screen, camera, NFC, Bluetooth LE, telephony, microphone | — | — |
| Memory | leave blank until measured | leave blank until measured |
| DirectX | leave blank | DirectX 12 |
| Dedicated GPU memory, processor, graphics | leave blank | leave blank |

Do not tick "pen and ink" (the slide-show pen is driven by the mouse; Windows Ink is untested) or "tested to meet accessibility guidelines".

Additional system requirements, minimum (<!--lines:addmin-->3<!--/--> items, longest <!--max:addmin-->95<!--/--> characters; limit 11 of 200 characters):

<!-- block:addmin -->
```text
Windows 10 or Windows 11, 64-bit (x64 or ARM64)
A graphics adapter with DirectX 12 or OpenGL; older PCs fall back to a slower software renderer
Speakers or headphones for slides with audio or video
```

Recommended (<!--lines:addrec-->1<!--/--> item):

<!-- block:addrec -->
```text
A second display for presenter view
```

Memory and disk space: measure on the release build before filling these in.

## What's new in this version (limit 1,500 characters)

Leave blank on the first submission. Template for updates:

```text
Facthory Deck <version>

New
• <one line per user-visible addition>

Fixed
• <one line per user-visible fix>

Known issues
• <only if something new is known to be broken>

Full release notes are on GitHub under release v<version>.
```

## Copyright, licence terms, developer

| Field | Limit | Value |
| ----- | ----- | ----- |
| Copyright and trademark info (<!--n:copyright-->127<!--/--> chars) | 200 | see block |
| Applicable license terms (<!--n:license-->763<!--/--> chars) | 10,000, **required** | see block |
| Developed by (<!--n:devby-->64<!--/--> chars) | 255 | see block |

<!-- block:copyright -->
```text
© 2026 Bandpey GmbH. Based on DeckCraft, © 2026 ArtCraft Team and the DeckCraft contributors. Licensed under MIT OR Apache-2.0.
```

<!-- block:license -->
```text
Facthory Deck is free and open-source software. You may use, copy, modify and distribute it under the terms of either the MIT License or the Apache License, Version 2.0, at your option.

MIT License: https://github.com/FACTHORYAI/deck/blob/main/LICENSE-MIT
Apache License 2.0: https://github.com/FACTHORYAI/deck/blob/main/LICENSE-APACHE
Notices: https://github.com/FACTHORYAI/deck/blob/main/NOTICE
Third-party fonts and assets and their licences: https://github.com/FACTHORYAI/deck/blob/main/ATTRIBUTION.md

The software is provided "as is", without warranty of any kind, as both licences state. Facthory Deck is based on DeckCraft by the ArtCraft team; their copyright and licence notices are kept. The Facthory name and logos are not licensed under these terms.
```

<!-- block:devby -->
```text
Bandpey GmbH (Facthory), based on DeckCraft by the ArtCraft team
```

The upstream credit matches `LICENSE-MIT` and `NOTICE` ("Copyright (c) 2026 ArtCraft Team and the DeckCraft contributors"), checked 2026-10-25.

## Support info (Properties page)

| Field | Value |
| ----- | ----- |
| Does this product access, collect or transmit personal information? | **Yes** (Policy 10.5.1) |
| Privacy policy URL | `https://facthory.com/privacy/apps` (**to publish**) |
| Website | `https://facthory.com/deck` (**to publish**) |
| Support contact info | `https://github.com/FACTHORYAI/deck/issues` |
| Contact details (phone, address) | from [the owner checklist](https://github.com/FACTHORYAI/page/blob/main/facthory/launch/owner-checklist.md), step 3 |

## Screenshots

PNG, landscape, at least 1366 × 768 (render at 1920 × 1080 or 2560 × 1440), at most 50 MB, 1 required, up to 10, captions up to 200 characters, key content in the top two-thirds, no added logos or marketing text. Deck has no offscreen UI renderer; capture the branded app window through the control channel (`facthorydeck --sample --control <port>`, then the `ui.screenshot` method from `docs/control-protocol.md`), English interface, built-in sample deck only.

| # | Shows | Caption (longest <!--max:captions-->74<!--/--> chars) |
| - | ----- | ------- |
| 1 | Normal view of the sample deck: slide panel, a selected shape with handles, the Shape Format tab | `Design slides with themes, layouts and more than 150 shapes.` |
| 2 | Format Shape pane open on a gradient fill | `Fine-tune fills, outlines, shadows and effects in the Format Shape pane.` |
| 3 | Slide Sorter with transition badges | `Arrange slides and add transitions in the Slide Sorter.` |
| 4 | Animation pane with several effects on one slide | `Animate text and objects, by paragraph or all at once.` |
| 5 | Presenter view: current slide, next slide, notes, timer | `Present full screen, with your notes and the next slide in presenter view.` |
| 6 | Dark mode with a native chart on the slide | `Dark mode, with charts, tables and pictures on your slides.` |

<!-- block:captions -->
```text
Design slides with themes, layouts and more than 150 shapes.
Fine-tune fills, outlines, shadows and effects in the Format Shape pane.
Arrange slides and add transitions in the Slide Sorter.
Animate text and objects, by paragraph or all at once.
Present full screen, with your notes and the next slide in presenter view.
Dark mode, with charts, tables and pictures on your slides.
```

## Store logos

| Asset | Size (PNG, ≤ 50 MB) | Status for MSI apps | Source |
| ----- | ------------------- | ------------------- | ------ |
| 1:1 box art | 2160 × 2160 (or 1080 × 1080) | **Required** | Render the Facthory Deck icon SVG from `facthory/icons/` with resvg; no text in the bottom third |
| 2:3 poster art | 1440 × 2160 (or 720 × 1080) | Recommended | Same icon; "Facthory Deck" in the top two-thirds if text is used (contrast at least 4.5:1) |
| 1:1 app tile icon | 300 × 300 | Only if the MSI listing page offers the slot | `facthory/icons/app-icon/` render |

The icon must not resemble Microsoft's orange "P" (§14.5).

## Packages page

| Field | x64 package | ARM64 package |
| ----- | ----------- | ------------- |
| Package URL | `https://github.com/FACTHORYAI/deck/releases/download/v<version>/facthorydeck-<version>-windows-x64.msi` | `…/facthorydeck-<version>-windows-arm64.msi` |
| Architecture | x64 | arm64 |
| App type | MSI (`/qn`) | MSI |
| Languages | English (en-us) | English (en-us) |

The local Deck checkout has no `facthory-release.yml` yet (Page's builds signed x64 and ARM64 MSIs and drafts the GitHub release); W4 adds the same workflow to Deck before the first submission.

## Notes for certification (<!--n:notes-->1,435<!--/--> characters; limit 2,000)

<!-- block:notes -->
```text
Facthory Deck is a desktop presentation app delivered as a per-machine MSI; a UAC prompt during install is expected. No account, sign-in or server is needed and the app works fully offline.

How to test: start Facthory Deck from the Start menu. Create a new presentation or open the built-in sample deck, add a slide, insert a shape and a picture from a file, add a transition, then start the slide show (Esc ends it). Use File > Save As to save a .pptx file and File > Export to create a PDF. Printing is not available in this version; PDF export is the way to print.

Network: the app does not connect to any server of ours. If update checks are on, it asks GitHub's release feed for this app whether a newer version exists. Hyperlinks on slides open in the default browser after the user clicks them.

No generative AI is built in. The command-line tool facthorydeck-cli.exe, installed next to the app, includes an MCP server: a local automation interface that scripts or AI agents the user runs can use. It talks over standard input and output, and the app's optional control channel listens only on 127.0.0.1, only when started with --control, and requires a key.

Uninstall through Settings > Apps removes all installed files and registry entries. Per-user settings, logs and recovery copies the app created in %APPDATA%\Facthory Deck are left in place, as is usual for user data.

Contact: <support email>. Notes written <date>.
```
