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

### desktop systems (rust & c)

- **[Atrium](https://github.com/VirInvictus/Atrium)** · a production-grade native linux task manager built on local-first SQLite. fuses the aesthetic calm of Things 3 with the power of OmniFocus and the strict data model of Org-mode. features a dual-path search engine (AST compiling to SQL fast-paths with in-memory fallbacks) and a bidirectional Org-mode sync that solves the "anti-echo" problem using nanosecond-precision `mtime` ring buffers. `Rust · GTK4 · Tokio` · *shipping v0.74.0*
- **[Framework](https://github.com/VirInvictus/Framework)** · high-performance, dual-engine document viewer (PDF, EPUB, CBR, Markdown). bypasses MuPDF's lack of thread-safety by spawning up to 8 isolated render instances with an atomic round-robin dispatcher. achieves zero-copy rendering by mapping MuPDF BGR bytes directly into Cairo/GTK4 surfaces. uses Linux Landlock LSM to sandbox WebKitGTK. `C17 · GTK4 · WebKitGTK` · *shipping v1.0.0*
- **[Viaduct](https://github.com/VirInvictus/Viaduct)** · a fast, local-first rss reader that treats articles as text, not web pages. an opinionated linux port of NetNewsWire's engine. uses a strict single-writer SQLite worker alongside a concurrent read pool to ensure background syncs never stutter the timeline UI. RSS is constrained inside a neutered WebKit sandbox (no JS, strict CSP, custom URI interceptors). `Rust · GTK4 · WebKitGTK` · *shipping v3.8.0*
- **[Conservatory](https://github.com/VirInvictus/Conservatory)** · "calibre for audio." inverts the player model to be database-canonical: the SQLite database owns the library, rendering folder templates and executing dry-run, undo-journaled filesystem moves. mutates libmpv audio filter graphs live to prevent clicking, and taps PipeWire for real-time FFT visualization. `Rust · GTK4 · libmpv` · *shipping v0.7.0*
- **[Hermitage](https://github.com/VirInvictus/Hermitage)** · a visually immersive gallery browser for calibre libraries. reads `metadata.db` strictly read-only, thumbnails and colour-quantizes covers on a background thread, and ships as a flatpak. `Python · GTK4` · *shipping v1.8.3*
- **[Topograph](https://github.com/VirInvictus/Topograph)** · a blazing-fast filesystem visualizer in the qdirstat tradition: gpu-accelerated qt6/qml over a rust scan core, styled in kanagawa dragon. `Rust · Qt6/QML (CXX-Qt)` · *shipping v0.3.1*

### domain tooling (python & cli)

- **[cquarry](https://github.com/VirInvictus/cquarry)** · canonical calibre database layer. a headless engine providing read-only SQLite access (escaping write-locks safely) and a pure-python recursive-descent parser that faithfully ports Calibre's search grammar (AST evaluation, boolean logic, accent folding) with **zero external dependencies**. `Python · stdlib-only` · *shipping v1.21.0*
- **[CalibreQuarry](https://github.com/VirInvictus/CalibreQuarry)** · CLI/TUI front-end for `cquarry`. goes beyond wrapper scripts by implementing deep data mining: extracting literal copyright-page text from book binaries to verify database ISBNs against reality. `Python · vir-tui` · *shipping v3.42.0*
- **[bindery-cli](https://github.com/VirInvictus/bindery-cli)** · deterministic EPUB repair tool. gates every modification behind W3C's `epubcheck` and executes atomic `os.replace` filesystem writes, with lossy watermark stripping protected by three strict safety nets (character conservation, tag balancing, and a `no_worse` check). `Python` · *shipping v0.40.0*
- **[raindrop-cli](https://github.com/VirInvictus/raindrop-cli)** · dependency-free Raindrop.io CLI. refuses heavy packages like `requests` or `rich`. hand-rolls `multipart/form-data` encoding, API rate-limiting, exponential backoff, and ANSI terminal rendering using only the Python standard library. `--dry-run` safety is strictly enforced at the lowest network layer. `Python · stdlib-only` · *shipping v0.6.1*
- **[AudiobookTools](https://github.com/VirInvictus/AudiobookTools)** · declarative tag-and-folder normalizer for audiobook libraries. dry-run by default, reversible `--apply` with an undo journal; never re-encodes, never deletes audio. `Python · mutagen` · *shipping v0.2.0*
- **[lattice-music](https://github.com/VirInvictus/lattice-music)** · CLI/TUI audit and visualization suite for music collections: ~20 read-only modes, with the cleaning/apestrip write brains folded into the package behind explicit opt-in modes. the filesystem is the source of truth; writes are dry-run by default and gated behind `--clean`/`--apestrip` plus `--apply`. `Python · mutagen · vir-tui` · *complete v5.4.0*
- **[dragon-agents](https://github.com/VirInvictus/dragon-agents)** · a local ZCode plugin shipping six read-only research subagents: repo cartography, doc-drift audits, downstream cascade checks, spec compliance, ci triage, and prose slop passes. `Markdown · Python` · *v0.1.1*
- **[Carrel](https://github.com/VirInvictus/Carrel)** · a single-user reading room contract for a curated calibre library. enforces ok-lab accessible typography, disables upstream features via hooks to prevent merge conflicts, and owns its CSS entirely. code rides in the companion fork, [Carrel-calibre-web](https://github.com/VirInvictus/Carrel-calibre-web). `CSS · docs` · *shipping v0.9.9*

### koreader & player plugins

- **[Colophon](https://github.com/VirInvictus/Colophon)** · native statistics viewer for koreader. imports a copy of `statistics.sqlite3`, draws its own cairo charts, ships the reading analytics nobody else has. `Rust · GTK4` · *shipping v2.4.0*
- **[Dead Reckoning](https://github.com/VirInvictus/dead-reckoning-bookend-preset)** · navigation-cockpit preset for koreader's bookends plugin: session pace, chapter eta, projected finish date. `Lua` · *complete*
- **[2-kobo-style-sleepscreen-banner-prettified](https://github.com/VirInvictus/2-kobo-style-sleepscreen-banner-prettified)** · koreader user patch: redraws the sleep screen as a kobo-style floating card over your cover. `Lua` · *complete*
- **[1-timezone](https://github.com/VirInvictus/1-timezone)** · koreader user patch: forces a correct posix timezone inside the process (`setenv` + `tzset`), fixing the clock on framework-less installs. `Lua` · *complete*
- **[deadbeef-cui](https://github.com/VirInvictus/deadbeef-cui)** · faceted, foobar2000-columns library browser plugin for the DeaDBeeF player. `C` · *complete v1.3.4*

### shared libraries & games

- **[vir-search](https://github.com/VirInvictus/vir-search)** · a shared rust library parsing calibre-style search expressions into a typed AST. used by Atrium and Conservatory. `Rust` · *active v1.4.2*
- **[vir-tui](https://github.com/VirInvictus/vir-tui)** · a lightweight python library providing a robust terminal ui (curses grid menus, pagers) without the bloat of textual. `Python` · *complete v2.3.0*
- **[vir-gtk](https://github.com/VirInvictus/vir-gtk)** · a shared gtk4 styling library for native linux apps, extracting the Kanagawa theme engine. `Rust · GTK4` · *active v1.4.0*
- **[Hearthfall](https://github.com/VirInvictus/Hearthfall)** · grimdark clan-survival for the terminal. seasonal turns, a fog-black map. engine is stdlib-only pure logic with no i/o, driven from a single seeded rng. `Python · Textual` · *shipping v0.27.0*
- **[opends](https://github.com/VirInvictus/opends)** · reverse-engineering toolkit for ssi's *dark sun* crpgs (1993–94): fourteen tools covering a disassembler for the undocumented gpl bytecode vm, gff/save editors, and exe map tooling. `Rust · Python`

the full codex, with screenshots and the long writeups, live at →
**[virinvictus.github.io](https://virinvictus.github.io)**

### elsewhere

- mastodon · [@Bdkl@mastodon.social](https://mastodon.social/@Bdkl)
- linkedin · [linkedin.com/in/bdkl](https://www.linkedin.com/in/bdkl/)
- now playing · [last.fm/user/bdkl__](https://www.last.fm/user/bdkl__)

`Rust · C · Python · GTK4 · SQLite · Meson`, with a soft spot for Ruby.

### support

if any of this is useful to you and you'd like to chip in:

- liberapay · [liberapay.com/bdkl](https://liberapay.com/bdkl/)
- bitcoin
  ```
  bc1qkge6zr45tzqfwfmvma2ylumt6mg7wlwmhr05yv
  ```
