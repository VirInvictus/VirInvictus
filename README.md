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

### books & calibre

- **[Bindery](https://github.com/VirInvictus/Bindery)** · comprehensively audit and repair broken epubs with a lightning-fast persistent Java daemon. native calibre db integration through `cquarry`, lossy watermark stripping, safe HTML tag unwrapping, and content damage flagging (ocr, foreign language). epubcheck-clean. `Python · tqdm` · *complete v0.14.0*
- **[Carrel](https://github.com/VirInvictus/Carrel)** · a single-user reading room for one curated calibre library. no login, `metadata.db` attached read-only at the connection, and calibre's own search grammar where upstream had none: `author:"King"` used to return 0 results, now 55. wings, a hierarchical category browser, ctrl-k over 6,975 destinations, and live statistics. code rides in a companion fork, [Carrel-calibre-web](https://github.com/VirInvictus/Carrel-calibre-web). `Python · CSS` · *shipping v0.9.2*
- **[CalibreQuarry](https://github.com/VirInvictus/CalibreQuarry)** · reads a calibre `metadata.db` raw, in read-only via `cquarry`. catalogs, audits, exports. no `calibredb`, no dependencies. `Python · stdlib` · *complete v3.11.0*
- **[cquarry](https://github.com/VirInvictus/cquarry)** · a lightweight, canonical python package providing read-only access to calibre's `metadata.db` and a full parser for calibre's search expression grammar. powers calibrequarry, hermitage, bindery, and carrel. `Python · stdlib` · *complete*

### music & audio

- **[Conservatory](https://github.com/VirInvictus/Conservatory)** · calibre for audio. a native linux manager that owns and moves your music, podcasts, and audiobooks on disk, all played from one libmpv queue. sqlite is the source of truth, with search via `vir-search` and UI styled by `vir-gtk`. `Rust · GTK4`
- **[Lattice](https://github.com/VirInvictus/Lattice)** · cli for music collectors. library trees, integrity checks, cover and tag audits. the filesystem is the source of truth. `Python` · *complete v4.14.0*
- **[deadbeef-cui](https://github.com/VirInvictus/deadbeef-cui)** · faceted, foobar2000-columns library browser plugin for the DeaDBeeF player. `C` · *complete v1.3.3*

### koreader

- **[Colophon](https://github.com/VirInvictus/Colophon)** · native statistics viewer for koreader. imports a copy of `statistics.sqlite3`, draws its own cairo charts, ships the reading analytics nobody else has. `Rust · GTK4` · *shipping v2.1.1*
- **[Dead Reckoning](https://github.com/VirInvictus/dead-reckoning-bookend-preset)** · navigation-cockpit preset for koreader's bookends plugin: session pace, chapter eta, projected finish date, chapter ticks on the progress bar. `Lua` · *complete*
- **[2-kobo-style-sleepscreen-banner-prettified](https://github.com/VirInvictus/2-kobo-style-sleepscreen-banner-prettified)** · koreader user patch: redraws the sleep screen as a kobo-style floating card over your cover, with a random highlight as a pull-quote. a prettified fork of zenixlabs' patch. `Lua` · *complete*
- **[1-timezone](https://github.com/VirInvictus/1-timezone)** · koreader user patch: forces a correct posix timezone inside the process (`setenv` + `tzset`), fixing the clock, time sync, and autowarmth on framework-less installs where no `TZ` is set. `Lua` · *complete*

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
