# VIR · INVICTVS

**the unconquered.** ex libris Brandon LaRocque.

programmer. curator. former chef. nearly twenty years in kitchens and mining 
camps before *The C Programming Language*, read at night between shifts. now a
computer engineering student with a CS degree underway. the credential follows 
the practice.

i build **native linux desktop software for people who treat their library as
worth maintaining.** my focus is on rich metadata, strict organization, and
local-first architectures; i try to carry librarian vibes into the codebase.
rust with gtk4, c built with meson, python where the standard library reaches.
it runs on your machine and answers to you.

```
no cloud.  no docker.  no electron.  no telemetry.  no accounts.  no vc.
your data on your disk: sqlite in WAL, single-writer worker, read-only pool, FTS5.
compile-time boundaries over code-review rules.  hard ceilings over soft benchmarks.
local-first, or it doesn't ship.
```

### books & collections

- **[cquarry](https://github.com/VirInvictus/cquarry)** · the canonical calibre database layer: read-only SQLite access that escapes write-locks safely, plus a pure-python recursive-descent parser that ports Calibre's search grammar faithfully, accent folding included. zero external dependencies, ever. `Python · stdlib-only` · *shipping v1.29.2*
- **[CalibreQuarry](https://github.com/VirInvictus/CalibreQuarry)** · cli/tui front-end for `cquarry`, built for deep data mining rather than wrapper duties: it extracts literal copyright-page text from book binaries to verify database ISBNs against reality. `Python · vir-tui` · *shipping v3.94.0*
- **[bindery-cli](https://github.com/VirInvictus/bindery-cli)** · a deterministic EPUB repair tool, at its 1.0: the observatory's final cycle ended with zero fatal books, and the spec's stability contract keeps the flag surface additive-only. every modification gates behind W3C's `epubcheck`, writes are atomic `os.replace`, and the lossy watermark strip carries three safety nets. `Python` · *shipping v1.2.8*
- **[lattice-music](https://github.com/VirInvictus/lattice-music)** · cli/tui audit and visualization suite for music collections: ~30 read-only modes over a filesystem-as-source-of-truth library. the maintenance writes live behind explicit opt-in flags, dry-run by default until `--apply` says otherwise. `Python · mutagen · vir-tui` · *complete v6.6.0*
- **[raindrop-cli](https://github.com/VirInvictus/raindrop-cli)** · a dependency-free raindrop.io cli that refuses `requests` and `rich` alike: multipart encoding, rate limiting, backoff, and ANSI rendering, all hand-rolled on the standard library. `--dry-run` safety is enforced at the lowest network layer. `Python · stdlib-only` · *complete v0.7.0*

### ports & reverse engineering

- **[Quire](https://github.com/VirInvictus/Quire)** · a soulver-style notepad calculator where prose and math share one plain-text sheet: sentences with quantities answer through an embedded dimension-checked engine (`the stock solution measures 2 mol/L` answers `2 molar`). line references resolve both ways, renumber themselves, and the sheet re-evaluates in the frame you type in. `Rust · GTK4 · numbat` · *shipping v1.5.7*
- **[Docket](https://github.com/VirInvictus/Docket)** · a native gtk4 editor for the taskpaper format, clean-room faithful: files stay plain text any editor can open, while docket makes them fold, filter, and query like an outliner without ever taking the text away. `Rust · GTK4 · sourceview5` · *shipping v1.1.3*
- **[Commonplace](https://github.com/VirInvictus/Commonplace)** · a linux port of the notational velocity line: one search field that finds notes and becomes them when nothing matches, over a plain folder of files. the headless engine carries nvALT's exact admission, rename, and collision semantics with no inverted index by design (10k notes per keystroke in microseconds), plus the metadata-tag and wiki-link graph with rename rewriting. `Rust · GTK4` · *shipping v0.6.1*
- **[opends](https://github.com/VirInvictus/opends)** · a reverse-engineering toolkit for ssi's *dark sun* crpgs (1993–94): seventeen tools spanning a disassembler for the undocumented gpl bytecode vm, gff/save editors, and audio, midi, and exe map tooling. `Rust · Python` · *active*

### everything else

- [Atrium](https://github.com/VirInvictus/Atrium) · production-grade native task manager; Things 3's calm over a strict local-first SQLite core. `Rust · GTK4 · Tokio` · *shipping v0.77.0*
- [Framework](https://github.com/VirInvictus/Framework) · dual-engine document viewer (pdf, epub, cbr, markdown); eight isolated MuPDF instances, zero-copy rendering, WebKit under Landlock. `C17 · GTK4 · WebKitGTK` · *shipping v1.0.2*
- [Viaduct](https://github.com/VirInvictus/Viaduct) · local-first rss reader that treats articles as text; a linux port of NetNewsWire's engine. `Rust · GTK4 · WebKitGTK` · *shipping v4.4.4*
- [Conservatory](https://github.com/VirInvictus/Conservatory) · "calibre for audio": the SQLite database owns the library, the filesystem follows it. `Rust · GTK4 · libmpv` · *shipping v0.10.1*
- [Hermitage](https://github.com/VirInvictus/Hermitage) · visually immersive gallery browser for calibre libraries, strictly read-only, ships as a flatpak. `Python · GTK4` · *shipping v1.8.8*
- [Topograph](https://github.com/VirInvictus/Topograph) · filesystem size explorer in the qdirstat tradition; a squarified cushion treemap on one GPU geometry node. `Rust · Qt6/QML (CXX-Qt)` · *archived · complete at v0.4.1*
- [dragon-agents](https://github.com/VirInvictus/dragon-agents) · zcode plugin: thirty-eight research subagents plus eight skills, twenty-six read-only, one multimodal judge, ten under chartered write fences. `Markdown · Python` · *shipping v1.6.2*
- [Carrel](https://github.com/VirInvictus/Carrel) · a single-user reading-room contract for a curated calibre library; owns its CSS entirely. code in the companion fork, [Carrel-calibre-web](https://github.com/VirInvictus/Carrel-calibre-web). `CSS · docs` · *shipping v0.9.10*
- [AudiobookTools](https://github.com/VirInvictus/AudiobookTools) · declarative tag-and-folder normalizer for audiobook libraries; dry-run by default, undo-journaled, never deletes audio. `Python · mutagen` · *archived · complete at v0.3.0*
- [whisker-street](https://github.com/VirInvictus/whisker-street) · a discord stock market where the members are the stocks; the market must be boring to exploit. `Python · discord.py` · *active v0.8.0*
- [Colophon](https://github.com/VirInvictus/Colophon) · native statistics viewer for koreader; imports a copy of `statistics.sqlite3` and draws its own cairo charts. `Rust · GTK4` · *shipping v2.6.2*
- [saforums.koplugin](https://github.com/VirInvictus/saforums.koplugin) · reads the something awful forums on e-ink: persisted-cookie login, unread counts, continue-at-unread; scraped by written contract against synthetic fixtures. `Lua` · *active v0.5.4*
- [Dead Reckoning](https://github.com/VirInvictus/dead-reckoning-bookend-preset) · koreader bookends preset: session pace, chapter eta, projected finish date. `Lua` · *complete v1.0.0*
- [2-kobo-style-sleepscreen-banner-prettified](https://github.com/VirInvictus/2-kobo-style-sleepscreen-banner-prettified) · koreader user patch: the sleep screen redrawn as a kobo-style floating card over your cover. `Lua` · *complete v2.1.4*
- [1-timezone](https://github.com/VirInvictus/1-timezone) · koreader user patch: forces a correct posix timezone inside the process. `Lua` · *complete v1.0.0*
- [deadbeef-cui](https://github.com/VirInvictus/deadbeef-cui) · faceted, foobar2000-columns library browser plugin for DeaDBeeF. `C` · *complete v2.2.1*
- [vir-search](https://github.com/VirInvictus/vir-search) · shared rust library parsing calibre-style search expressions into a typed AST; used by Atrium and Conservatory. `Rust` · *complete v1.4.3*
- [vir-tui](https://github.com/VirInvictus/vir-tui) · lightweight python terminal ui: curses grid menus and pagers without textual's bloat. `Python` · *complete v2.5.0*
- [vir-gtk](https://github.com/VirInvictus/vir-gtk) · shared gtk4 styling library extracting the Kanagawa theme engine. `Rust · GTK4` · *complete v1.5.0*
- [Hearthfall](https://github.com/VirInvictus/Hearthfall) · grimdark clan-survival for the terminal; a stdlib-only pure-logic engine on one seeded rng. `Python · Textual` · *archived · complete at v0.28.0*
- [hex](https://github.com/VirInvictus/hex) · discworld mud plugin suite for blightmud: gmcp vitals, quow searches with tt_dw semantics, room awareness. `Lua · Python` · *active*

the full codex, with screenshots and the long writeups, live at →
**[virinvictus.github.io](https://virinvictus.github.io)**

### elsewhere

- mastodon · [@Bdkl@mastodon.social](https://mastodon.social/@Bdkl)
- linkedin · [linkedin.com/in/bdkl](https://www.linkedin.com/in/bdkl/)
- now playing · [last.fm/user/bdkl__](https://www.last.fm/user/bdkl__)

`Rust · C · Python · GTK4 · SQLite · Meson`, with a soft spot for Ruby.

### support

if any of this is useful to you and you'd like to chip in:

- github sponsors · [github.com/sponsors/VirInvictus](https://github.com/sponsors/VirInvictus)
- liberapay · [liberapay.com/bdkl](https://liberapay.com/bdkl/)
- bitcoin
  ```
  bc1qkge6zr45tzqfwfmvma2ylumt6mg7wlwmhr05yv
  ```
