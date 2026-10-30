# Switching to Facthory Deck

Facthory Deck is a free, open-source presentation app for macOS, Windows and Linux. It opens and
saves `.pptx` decks, has the ribbon and shortcuts you already know, presents with transitions,
animations and presenter view, and runs entirely on your computer: no account, no subscription,
no telemetry, and it works offline.

This guide is for people moving over from Microsoft PowerPoint. It covers installing, opening your
decks, what is the same, what is different or missing today, and where to get help.

> **Facthory Deck is alpha, heading for beta.** That is upstream's own rating, and we follow it. You
> can build a deck, open and save `.pptx`, present with transitions, animations, media and presenter
> view, and export a PDF, but depth and fidelity have known gaps (section 4) and there is no
> printing yet. Keep the originals of decks that matter, and rehearse with Facthory Deck before
> you present from it.

Facthory Deck is based on DeckCraft by the ArtCraft team.

> **Draft note (remove before publishing):** add Facthory's own fidelity result here once W6
> reports it: "On Facthory's test set of N real-world decks, X% open, save and reopen without
> visible change."

## 1. Install

Download from [facthory.com/deck](https://facthory.com/deck) or the
[GitHub releases](https://github.com/FACTHORYAI/deck/releases/latest). Each release lists a
SHA-256 checksum for every file; the downloads page explains how to check one.

| System | File | How |
| ------ | ---- | --- |
| **macOS** 11 or later, Apple silicon or Intel | `facthorydeck-<version>-macos-universal.dmg` | Open the DMG and drag Facthory Deck to Applications. Signed and notarized by Bandpey GmbH; macOS only asks the usual first-launch question for downloaded apps. |
| **Windows** 10 or later (x64), Windows 11 on ARM | `facthorydeck-<version>-windows-x64.msi` or `…-windows-arm64.msi` | Run the installer. It installs for you alone without administrator rights; its first page also offers an installation for everyone on the computer, which asks for them. Signed by Bandpey GmbH. |
| **Linux** x86_64 or ARM64 | `.AppImage`, `.deb`, `.rpm` or `.tar.gz` | See below. |

On Linux:

```sh
# AppImage: runs on most distributions, no install needed
chmod +x facthorydeck-<version>-linux-x86_64.AppImage && ./facthorydeck-<version>-linux-x86_64.AppImage

# Debian, Ubuntu, Mint, Pop!_OS
sudo apt install ./facthorydeck-<version>-linux-x86_64.deb

# Fedora, openSUSE
sudo dnf install ./facthorydeck-<version>-linux-x86_64.rpm
```

Use `aarch64` in place of `x86_64` on ARM64 machines. The Linux builds need glibc 2.35 or newer
(Ubuntu 22.04, Debian 12, Fedora 36 or newer) and ALSA for sound.

The Microsoft Store listing is coming soon.

> **Draft note:** Flatpak comes through Flathub (W10, with the sandboxed builds); add its row then.

**You can keep Microsoft Office installed.** The installers offer Facthory Deck under "Open with"
for `.pptx`, `.potx` and `.ppsx` without taking over your defaults.

## 2. Open your decks

- **File › Open**, drag a file onto the window, or right-click a file and choose **Open With ›
  Facthory Deck**.
- Opens and saves: `.pptx`.
- Opens: `.potx` templates and `.ppsx` shows (they are saved back as ordinary presentations).
  Opening a `.ppsx` with Facthory Deck from the file manager on Windows or Linux starts the slide
  show; **File › Open** opens it for editing.
- Facthory Deck also has its own format, `.facthorydeck`, which keeps everything the app can do.
  Use `.pptx` for anything you share.
- Exports: PDF (slides, notes pages, or handouts with 1 to 9 slides per page, with selectable
  text), PNG or JPEG images of slides, an animated GIF of the deck, and the outline as text.
  **Insert › Slides from Outline…** builds slides from a text or Markdown outline.
- Not yet: legacy `.ppt`, macro-enabled `.pptm`, and OpenDocument `.odp`.

### Make Facthory Deck your default

Facthory Deck has no in-app button for this yet; use your system's settings.

- **Windows**: right-click a `.pptx`, choose **Open with › Choose another app**, select Facthory
  Deck and tick **Always**.
- **macOS**: select a `.pptx` in Finder, choose **File › Get Info**, pick Facthory Deck under
  **Open with**, then click **Change All**.
- **Linux**: in your file manager, **Properties › Open With › Set as default**, or run:

  ```sh
  xdg-mime default com.facthory.deck.desktop \
    application/vnd.openxmlformats-officedocument.presentationml.presentation
  ```

## 3. What looks and works the same

- **The ribbon.** Home, Insert, Draw, Design, Transitions, Animations, Slide Show, Review and View,
  with contextual tabs such as Shape Format, and a customisable Quick Access Toolbar. Weighted
  over 191 presentation features the project tracks, Facthory Deck covers **84%**, and **92% of
  the 72 most important ones** (measured;
  [docs/parity-checklist.md](https://github.com/FACTHORYAI/deck/blob/main/docs/parity-checklist.md)).
- **Building decks.** Slide masters and layouts with placeholders that inherit position and
  formatting, themes with colour and font schemes, sections, speaker notes, comments, headers and
  footers, custom slide sizes, Slide Sorter.
- **Drawing.** 150+ preset shapes with adjust handles, connectors that stay attached, freeform and
  scribble, merge shapes, gradient, picture and pattern fills, shadows, glow, soft edges and
  reflections, WordArt, icons.
- **Content.** Pictures with crop and corrections, tables with styles, charts, SmartArt basics,
  audio and video (MP3, AAC, FLAC, WAV, Ogg, Opus; H.264, HEVC, VP9, AV1).
- **Presenting.** Transitions including Morph; entrance, emphasis, exit and motion-path
  animations with by-paragraph builds; full-screen slide show; presenter view with notes, timer and
  clock; pen and laser pointer; See All Slides and zoom; rehearse timings; custom shows; media
  playback. The slide show and presenter view cover **68%** of the tracked features (measured;
  [docs/slideshow-parity.md](https://github.com/FACTHORYAI/deck/blob/main/docs/slideshow-parity.md)).
- **Keyboard.** The common shortcuts of the Mac version are bound: new slide, duplicate,
  group and ungroup, bold, italic, underline, alignment, font size, list levels, Format Painter,
  the Font dialog, start the show from the beginning or the current slide, and switching views
  ([docs/ui-parity.md](https://github.com/FACTHORYAI/deck/blob/main/docs/ui-parity.md)). Ctrl
  takes the place of ⌘ on Windows and Linux.
- **Proofing.** Spelling as you type, a thesaurus and AutoCorrect. Spelling uses the Hunspell
  dictionaries already on your system (most Linux desktops have them); none are bundled yet, so on
  Windows, and anywhere no dictionary is installed, only common misspellings are caught. There is
  no grammar check.
- **AutoRecover** keeps unsaved work if the app quits unexpectedly.

## 4. What is different or missing today

These come from the project's own gap list
([docs/gaps.md](https://github.com/FACTHORYAI/deck/blob/main/docs/gaps.md)) and parity documents.

- **Not yet proven on real-world decks.** Upstream tests `.pptx` with decks it builds itself;
  corporate templates, SmartArt, newer chart types and embedded fonts from real decks are still
  largely untested.
- **Saving drops a few things.** Media playback options and the animation "rewind when done"
  setting are lost on save. Templates and shows are saved as ordinary presentations.
- **No printing yet.** Export a PDF and print that.
- **PDF export** keeps text selectable, but draws each slide's artwork as a high-resolution
  picture rather than as vector shapes, so files are larger.
- **SVG pictures** show as their built-in fallback picture, and SVG files can't be inserted yet.
- **Fonts**: only regular, bold and italic faces are drawn, so light, medium and semibold headings
  common in modern templates show in the wrong weight. Fonts embedded in a deck are used, except
  for one compressed format (MicroType Express), which falls back to a stand-in.
- **Presenter view** opens wherever your system puts it; move it to your own screen yourself
  before you start.
- **Animations**: 64 of PowerPoint's roughly 190 effects so far; the Animation Pane's preview plays
  the whole slide.
- **Charts**: editing a chart's data grid and some chart elements are partial. **SmartArt** editing
  is basic.
- **No video export** (MP4); the animated GIF has one frame per slide, without transitions or
  builds.
- **English only.** The interface is not translated yet.
- **Windows**: ribbon key tips (Alt sequences) are not there yet, and a startup crash on some
  Intel UHD graphics is still open. If the app doesn't start, see the troubleshooting note on the
  [downloads page](https://facthory.com/deck).

Upstream's own estimates, for orientation: about **62%** ready for someone who uses the core
features, about **53%** for a typical presenter's weekly work (estimates;
[ROADMAP.md](https://github.com/FACTHORYAI/deck/blob/main/ROADMAP.md)).

## 5. Fonts

Microsoft's fonts are not included. Facthory Deck ships open fonts with the same measurements as
the common Office fonts, so text fits its boxes as it did in PowerPoint:

- **Carlito** for Calibri, **Caladea** for Cambria, **Liberation Sans, Serif and Mono** for Arial,
  Times New Roman and Courier New.
- Its own themes use open fonts it also ships (Inter, Lato, Montserrat, Open Sans, Roboto and
  others), plus Japanese and Arabic fonts.
- **Fonts installed on your computer are used too.** If a deck asks for a font you have, Facthory
  Deck uses it.
- If a deck uses a font you don't have and that isn't embedded in the file, text may reflow.
  Install the font, or embed fonts in PowerPoint before sending. Aptos, the newer Microsoft 365
  default, has no open font with the same measurements, so text in Aptos can reflow slightly.

## 6. Sharing files back and forth

Save as `.pptx` and send the file as usual: people who use Microsoft PowerPoint open it as any
other presentation. Masters and layouts, themes, shapes, tables, charts, transitions, animations,
media, notes, comments, sections and links travel both ways.

To keep round trips smooth:

- Keep the original of an important deck until you have compared it once.
- Check video and audio settings (start automatically, loop, trim) after a deck has been saved by
  Facthory Deck.
- Send a PDF when the deck must look exactly the same everywhere.
- If you present from someone else's computer, take the `.pptx` and a PDF.

## 7. Working together

Facthory Deck is a desktop app for working with Office files on your computer. **It does not do
real-time co-editing**, and it does not join co-authoring sessions in Microsoft 365. Share files
as above, and use comments to review.

To work together, use [Facthory's workspace](https://facthory.com), where your team's projects
and docs live and are edited together. Opening and saving files directly in Facthory projects is
planned.

## 8. Automation: CLI and MCP

Every action in Facthory Deck is a command with a stable id that scripts and AI agents can run.

- **Command line** (`facthorydeck-cli`):

  ```sh
  facthorydeck-cli convert talk.pptx talk.pdf           # also .png, .jpg, .gif, .txt or .md (outline)
  facthorydeck-cli render talk.pptx --all slides/       # every slide as a PNG
  facthorydeck-cli run --in talk.pptx --cmd 'slide.new={"layout":"titleOnly","title":"Hello"}' --save talk.pptx
  facthorydeck-cli commands format.                     # list commands
  ```

- **MCP server** for local AI agents, headless or connected to the window you are looking at:

  ```sh
  claude mcp add facthory-deck -- facthorydeck-cli mcp
  facthorydeck --control 7990 &   # then let the agent drive the open app:
  claude mcp add facthory-deck-app -- facthorydeck-cli mcp --connect 7990
  ```

  Keep a headless agent to chosen folders with `--automation-read-root DIR
  --automation-write-root DIR`.

Where the CLI is: on Linux the `.deb` and `.rpm` install `facthorydeck-cli` on your `PATH` (the
`.tar.gz` has it in `bin/`); on Windows it is in `C:\Program Files\Facthory Deck\` (add that folder
to `PATH` to call it by name); on macOS it is inside the app,
`/Applications/Facthory Deck.app/Contents/MacOS/facthorydeck-cli`, and also a separate download,
`facthorydeck-cli-<version>-macos-universal.zip`. Details:
[docs/mcp.md](https://github.com/FACTHORYAI/deck/blob/main/docs/mcp.md).

## 9. Getting help

- **Report a problem or ask for help** on the File tab or in About, or [open an issue on
  GitHub](https://github.com/FACTHORYAI/deck/issues). Search first; someone may have hit it too.
- Attach the log file: `~/.config/facthorydeck/logs/` on Linux,
  `~/Library/Application Support/Facthory Deck/logs/` on macOS, `%APPDATA%\Facthory Deck\logs\` on
  Windows.
- Never attach a confidential deck to a public issue; describe it or make a small sample.

## FAQ

**Is it ready for my next important presentation?** Try it first. Open the deck, save it,
reopen it and run through it in Facthory Deck before the day. Facthory Deck is alpha, heading for
beta.

**Is it really free?** Yes. Facthory Deck is open source under MIT or Apache-2.0, with no
subscription and no paid tier.

**Do I need an account?** No. Nothing to sign in to.

**Does it send my data anywhere?** No. It works offline and has no telemetry or crash reporting.

**Can I use it next to Microsoft Office?** Yes. Installing it changes none of your defaults.

**Can I print handouts?** Not directly yet: export handouts or notes pages as a PDF and print the
PDF.

**Can I open my old `.ppt` files?** Not yet. Save them as `.pptx` in PowerPoint first.

**Can several people edit one deck at the same time?** Not in Facthory Deck. Use Facthory's
workspace for that (section 7).

**How do I update?** Facthory Deck checks for a new version once a day, downloads it in the
background and installs it when you quit (or right away with **Restart now**); your settings are
kept. Linux `.deb` and `.rpm` installs update with your package manager.

---

Microsoft, Microsoft Office, Microsoft 365 and PowerPoint are trademarks of the Microsoft group of
companies. Facthory Deck is not affiliated with, sponsored or endorsed by Microsoft. Facthory Deck
is published by Bandpey GmbH.
