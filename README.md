# VIR · INVICTVS

**the unconquered.** ex libris Brandon LaRocque.

programmer. curator. former chef. ten years in kitchens and mining camps before
*The C Programming Language*, read at night between shifts. now a computer
engineering student with a CS degree underway. the credential follows the practice.

i build **native linux desktop software for people who treat their library as
worth maintaining.** rust with gtk4, c built with meson, python where the standard
library reaches. it runs on your machine and answers to you.

```
no cloud.  no docker.  no electron.  no telemetry.  no accounts.  no vc.
your data on your disk: sqlite in WAL, single-writer worker, read-only pool, FTS5.
compile-time boundaries over code-review rules.  hard ceilings over soft benchmarks.
local-first, or it doesn't ship.
```

### shipping & done

- **[Atrium](https://github.com/VirInvictus/Atrium)** · native gnome task manager. org-mode internals (uuids, plain-text round-trip) under a Things 3 / OmniFocus surface, with a calibre-style search grammar. `Rust · GTK4` · *shipping v0.46.2*
- **[Framework](https://github.com/VirInvictus/Framework)** · native gnome document viewer for pdf, djvu, comics, and ebooks. mupdf and djvulibre under the fixed-layout formats; epub and mobi reflow natively through webkitgtk. `C · GTK4` · *shipping v0.79.0*
- **[Viaduct](https://github.com/VirInvictus/Viaduct)** · netnewswire ported to linux. single-writer sqlite, opml on disk, hard memory ceilings. past 1.0, tracking upstream. `Rust · GTK4` · *shipping v2.8.2*
- **[Colophon](https://github.com/VirInvictus/Colophon)** · native statistics viewer for koreader. imports a copy of `statistics.sqlite3`, draws its own cairo charts, ships the reading analytics nobody else has. `Rust · GTK4` · *shipping v2.0.1*
- **[Lattice](https://github.com/VirInvictus/Lattice)** · cli for music collectors. library trees, integrity checks, cover and tag audits. the filesystem is the source of truth. `Python` · *complete v4.10.1*
- **[CalibreQuarry](https://github.com/VirInvictus/CalibreQuarry)** · reads a calibre `metadata.db` raw, in read-only. catalogs, audits, exports. no `calibredb`, no dependencies. `Python · stdlib` · *complete v3.6.0*
- **[deadbeef-cui](https://github.com/VirInvictus/deadbeef-cui)** · faceted, foobar2000-columns library browser plugin for the DeaDBeeF player. `C` · *complete v1.3.3*
- **[Dead Reckoning](https://github.com/VirInvictus/dead-reckoning-bookend-preset)** · navigation-cockpit preset for koreader's bookends plugin: session pace, chapter eta, projected finish date, chapter ticks on the progress bar. `Lua` · *complete*
- **[Kobo-style Sleepscreen Banner](https://github.com/VirInvictus/2-kobo-style-sleepscreen-banner-prettified)** · koreader user patch: redraws the sleep screen as a kobo-style floating card over your cover, with a random highlight as a pull-quote. a prettified fork of zenixlabs' patch. `Lua` · *complete*
- **[1-timezone](https://github.com/VirInvictus/1-timezone)** · koreader user patch: forces a correct posix timezone inside the process (`setenv` + `tzset`), fixing the clock, time sync, and autowarmth on framework-less installs where no `TZ` is set. `Lua` · *complete*

### in the workshop

- **[Conservatory](https://github.com/VirInvictus/Conservatory)** · calibre for audio. a native gnome manager that owns and moves your music, podcasts, and audiobooks on disk, all played from one libmpv queue. sqlite is the source of truth. `Rust · GTK4`
- **[opends](https://github.com/VirInvictus/opends)** · reverse-engineering toolkit for ssi's *dark sun* crpgs (1993–94). a disassembler and byte-exact reassembler for the games' undocumented gpl bytecode vm, plus gff/sprite/save editors. bring your own gog copy. `Rust · Python`
- **[Hermitage](https://github.com/VirInvictus/Hermitage)** · read-only gallery browser for calibre libraries. `Python`
- **[calibre-web-kanagawa](https://github.com/VirInvictus/calibre-web-kanagawa)** · kanagawa dragon theme + curated read-only configuration for calibre-web: a web front-end that feels like a reading room, not a dashboard. code rides in a companion fork, [calibre-web-smallscope](https://github.com/VirInvictus/calibre-web-smallscope). `CSS · Python`
- **[AudiobookTools](https://github.com/VirInvictus/AudiobookTools)** · declarative tag-and-folder normalizer for an audiobook shelf. one catalogue drives both the embedded tags and the on-disk tree; dry-run by default, every apply reversible. `Python`
- **[Bindery](https://github.com/VirInvictus/Bindery)** + **[oceanstrip](https://github.com/VirInvictus/oceanstrip)** · repair broken epubs and strip producer watermarks, epubcheck-clean. `Python · stdlib`
- **Hearth** + **Haveli** · two-player, lan-only, offline digital board games on content-agnostic deterministic engines. hidden hands force a host-authoritative, per-seat-redacted network model. private while in development. `Godot · GDScript`
- **[Coffer](https://github.com/VirInvictus/Coffer)** · envelope budgeting over a plain-text hledger journal. actual budget's experience, hledger's data discipline; the journal is the database. atrium's sibling, for money. research stage. `Rust · GTK4`

the full twenty-four, with screenshots and the long writeups, live in the codex →
**[virinvictus.github.io](https://virinvictus.github.io)**

### elsewhere

- mastodon · [@Bdkl@mastodon.social](https://mastodon.social/@Bdkl)
- linkedin · [linkedin.com/in/bdkl](https://www.linkedin.com/in/bdkl/)
- now playing · [last.fm/user/bdkl__](https://www.last.fm/user/bdkl__)

`Rust · C · Python · GTK4 · SQLite · Meson`, with a soft spot for Ruby.

### support

if any of this is useful to you and you'd like to chip in:

```
bc1qkge6zr45tzqfwfmvma2ylumt6mg7wlwmhr05yv
```
