# VIR · INVICTVS

**the unconquered.** ex libris Brandon LaRocque.

programmer. curator. former chef. nearly twenty years in kitchens and mining 
camps before *The C Programming Language*, read at night between shifts. now a
computer engineering student with a CS degree underway. the credential follows 
the practice.

i build **native linux desktop software for people who treat their library as
worth maintaining.** my focus is on rich metadata, strict organization, and
local-first architectures—i try to carry librarian vibes into the codebase.
rust with gtk4, c built with meson, python where the standard library reaches.
it runs on your machine and answers to you.

```
no cloud.  no docker.  no electron.  no telemetry.  no accounts.  no vc.
your data on your disk: sqlite in WAL, single-writer worker, read-only pool, FTS5.
compile-time boundaries over code-review rules.  hard ceilings over soft benchmarks.
local-first, or it doesn't ship.
```

### applications
- **[Viaduct](https://github.com/VirInvictus/Viaduct)** · a fast, local-first rss reader that treats articles as text, not web pages. An opinionated Rust port of NetNewsWire `Rust · GTK4` · *shipping v3.3.1*

### books & calibre tooling

- **[CalibreQuarry](https://github.com/VirInvictus/CalibreQuarry)** · ultimately, a front-end for [cquarry](https://github.com/VirInvictus/cquarry). A handful of auditing and organizing tools for Calibre. `Python · tqdm` · *complete v3.19.0*
- **[Bindery](https://github.com/VirInvictus/Bindery)** · comprehensively audit and repair broken epubs with a lightning-fast persistent Java daemon. native calibre db integration through `cquarry`, lossy watermark stripping, safe HTML tag unwrapping, and content damage flagging (ocr, foreign language). epubcheck-clean. `Python · tqdm` · *complete v0.14.0*
- **[Carrel](https://github.com/VirInvictus/Carrel)** · a single-user reading room for one curated calibre library. no login, `metadata.db` attached read-only at the connection, and calibre's own search grammar where upstream had none: `author:"King"` used to return 0 results, now 55. wings, a hierarchical category browser, ctrl-k over 6,975 destinations, and live statistics. code rides in a companion fork, [Carrel-calibre-web](https://github.com/VirInvictus/Carrel-calibre-web). `Python · CSS` · *shipping v0.9.2*


### music & audio tooling

- **[Lattice](https://github.com/VirInvictus/Lattice)** · cli for music collectors. library trees, integrity checks, cover and tag audits. the filesystem is the source of truth. `Python` · *complete v4.14.0*
- **[deadbeef-cui](https://github.com/VirInvictus/deadbeef-cui)** · faceted, foobar2000-columns library browser plugin for the DeaDBeeF player. `C` · *complete v1.3.3*

### koreader

- **[Colophon](https://github.com/VirInvictus/Colophon)** · native statistics viewer for koreader. imports a copy of `statistics.sqlite3`, draws its own cairo charts, ships the reading analytics nobody else has. `Rust · GTK4` · *shipping v2.1.1*
- **[Dead Reckoning](https://github.com/VirInvictus/dead-reckoning-bookend-preset)** · navigation-cockpit preset for koreader's bookends plugin: session pace, chapter eta, projected finish date, chapter ticks on the progress bar. `Lua` · *complete*
- **[2-kobo-style-sleepscreen-banner-prettified](https://github.com/VirInvictus/2-kobo-style-sleepscreen-banner-prettified)** · koreader user patch: redraws the sleep screen as a kobo-style floating card over your cover, with a random highlight as a pull-quote. a prettified fork of zenixlabs' patch. `Lua` · *complete*
- **[1-timezone](https://github.com/VirInvictus/1-timezone)** · koreader user patch: forces a correct posix timezone inside the process (`setenv` + `tzset`), fixing the clock, time sync, and autowarmth on framework-less installs where no `TZ` is set. `Lua` · *complete*

### shared libraries
- **[cquarry](https://github.com/VirInvictus/cquarry)** · a lightweight, canonical python package providing read-only access to calibre's `metadata.db` and a full parser for calibre's search expression grammar. powers [CalibreQuarry](https://github.com/VirInvictus/CalibreQuarry), [Hermitage](https://github.com/VirInvictus/Hermitage), [Bindery](https://github.com/VirInvictus/Bindery), and [Carrel](https://github.com/VirInvictus/Carrel). `Python · stdlib` · *complete*
- **[vir-search](https://github.com/VirInvictus/vir-search)** · a shared rust library for parsing calibre-style search expressions into a typed AST. used by [Atrium](https://github.com/VirInvictus/Atrium) and [Conservatory](https://github.com/VirInvictus/Conservatory). `Rust` · *complete v1.0.1*
- **[vir-tui](https://github.com/VirInvictus/vir-tui)** · a lightweight python library providing a robust terminal ui (curses grid menus, pagers, prompts) for CLI tools without the bloat of textual. used by CalibreQuarry and Lattice. `Python` · *complete v1.0.0*
- **[vir-gtk](https://github.com/VirInvictus/vir-gtk)** · a shared gtk4 styling library for native linux apps, extracting the Kanagawa theme engine. `Rust · GTK4` · *complete v1.0.1*

### games & engines

- **[Hearthfall](https://github.com/VirInvictus/Hearthfall)** · grimdark clan-survival for the terminal. seasonal turns, a fog-black map, and a finite clan split between foraging, exploring, and war. scouting reveals enemy composition, so the fun lives in the preparation rather than the swing. the engine is stdlib-only pure logic with no i/o and no rendering, driveable from a repl; every draw goes through one seeded rng, so a seed replays a run exactly. `Python · Textual`
- **[opends](https://github.com/VirInvictus/opends)** · reverse-engineering toolkit for ssi's *dark sun* crpgs (1993–94). a disassembler and byte-exact reassembler for the games' undocumented gpl bytecode vm, plus gff/sprite/save editors. bring your own gog copy. `Rust · Python`

the full thirty, with screenshots and the long writeups, live in the codex →
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
