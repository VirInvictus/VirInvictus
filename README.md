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

- **[Atrium](https://github.com/VirInvictus/Atrium)** · native linux task manager. org-mode internals (uuids, plain-text round-trip) under a Things 3 / OmniFocus surface, with a calibre-style search grammar. dropped libadwaita for its own kanagawa dragon stylesheet on plain gtk4. `Rust · GTK4` · *shipping v0.69.0*
- **[Framework](https://github.com/VirInvictus/Framework)** · tiling-first document viewer for pdf, djvu, comics, and ebooks. plain gtk4 under an owned kanagawa dragon stylesheet, portal-driven dark/light. mupdf and djvulibre under the fixed-layout formats; epub, mobi, and azw3 reflow natively through webkitgtk, keeping their publisher stylesheets. `C · GTK4` · *shipping v0.82.0*
- **[Viaduct](https://github.com/VirInvictus/Viaduct)** · netnewswire ported to linux. single-writer sqlite, opml on disk, hard memory ceilings. dropped libadwaita in v3.0.0 for its own flat design; runs on gnome, hyprland, and any wayland desktop. `Rust · GTK4` · *shipping v3.2.0*
- **[Colophon](https://github.com/VirInvictus/Colophon)** · native statistics viewer for koreader. imports a copy of `statistics.sqlite3`, draws its own cairo charts, ships the reading analytics nobody else has. `Rust · GTK4` · *shipping v2.1.0*
- **[Carrel](https://github.com/VirInvictus/Carrel)** · a single-user reading room for one curated calibre library. no login, `metadata.db` attached read-only at the connection, and calibre's own search grammar where upstream had none: `author:"King"` used to return 0 results, now 55. wings, a hierarchical category browser, ctrl-k over 6,975 destinations, and live statistics. code rides in a companion fork, [Carrel-calibre-web](https://github.com/VirInvictus/Carrel-calibre-web). `Python · CSS` · *shipping v0.9.1*
- **Haveli** · two-player, lan-only, offline digital card game on a content-agnostic deterministic engine. hidden hands force a host-authoritative, per-seat-redacted network model: the host validates every move and pushes each peer only the view its seat may see, because relaying moves would leak the deck order. an `rng_seed` plus a draw cursor replay any shuffle from state alone. 1.0 is the engine milestone, verified live across two machines; the presentation pass is 2.0. private while it carries a faithful transcription. `Godot · GDScript` · *shipping v1.0.0*
- **[Lattice](https://github.com/VirInvictus/Lattice)** · cli for music collectors. library trees, integrity checks, cover and tag audits. the filesystem is the source of truth. `Python` · *complete v4.10.2*
- **[CalibreQuarry](https://github.com/VirInvictus/CalibreQuarry)** · reads a calibre `metadata.db` raw, in read-only. catalogs, audits, exports. no `calibredb`, no dependencies. `Python · stdlib` · *complete v3.9.0*
- **[deadbeef-cui](https://github.com/VirInvictus/deadbeef-cui)** · faceted, foobar2000-columns library browser plugin for the DeaDBeeF player. `C` · *complete v1.3.3*
- **[Dead Reckoning](https://github.com/VirInvictus/dead-reckoning-bookend-preset)** · navigation-cockpit preset for koreader's bookends plugin: session pace, chapter eta, projected finish date, chapter ticks on the progress bar. `Lua` · *complete*
- **[Kobo-style Sleepscreen Banner](https://github.com/VirInvictus/2-kobo-style-sleepscreen-banner-prettified)** · koreader user patch: redraws the sleep screen as a kobo-style floating card over your cover, with a random highlight as a pull-quote. a prettified fork of zenixlabs' patch. `Lua` · *complete*
- **[1-timezone](https://github.com/VirInvictus/1-timezone)** · koreader user patch: forces a correct posix timezone inside the process (`setenv` + `tzset`), fixing the clock, time sync, and autowarmth on framework-less installs where no `TZ` is set. `Lua` · *complete*

### in the workshop

- **[Conservatory](https://github.com/VirInvictus/Conservatory)** · calibre for audio. a native linux manager that owns and moves your music, podcasts, and audiobooks on disk, all played from one libmpv queue. sqlite is the source of truth. `Rust · GTK4`
- **[opends](https://github.com/VirInvictus/opends)** · reverse-engineering toolkit for ssi's *dark sun* crpgs (1993–94). a disassembler and byte-exact reassembler for the games' undocumented gpl bytecode vm, plus gff/sprite/save editors. bring your own gog copy. `Rust · Python`
- **[Hermitage](https://github.com/VirInvictus/Hermitage)** · read-only gallery browser for calibre libraries. `Python`
- **[AudiobookTools](https://github.com/VirInvictus/AudiobookTools)** · declarative tag-and-folder normalizer for an audiobook shelf. one catalogue drives both the embedded tags and the on-disk tree; dry-run by default, every apply reversible. `Python`
- **[rd-cli](https://github.com/VirInvictus/rd-cli)** · dependency-free cli for raindrop.io *and* pinboard. full rest api coverage over stdlib `urllib`; designed ansi for humans and `--json` for scripts and agents, typed errors, rate-limit backoff, `--dry-run` on every write, blast-radius-gated confirmation prompts, and a two-way additive `rd sync` between the two services that dedups on a normalized url. `Python · stdlib`
- **[Bindery](https://github.com/VirInvictus/Bindery)** + **[oceanstrip](https://github.com/VirInvictus/oceanstrip)** · repair broken epubs and strip producer watermarks, epubcheck-clean. `Python · stdlib`
- **Hearth** · two-player, lan-only, offline worker-placement and polyomino-economy eurogame on the same content-agnostic engine shape as haveli. the home-board puzzle and a pure effect vocabulary the cards reuse are the distinctive parts. private while in development. `Godot · GDScript`
- **Catagotchi** · a cozy cat tamagotchi wrapped around a cookie-clicker-scale idle empire: five needs averaging into a mood multiplier that gates all income, endless generator ladders, six daily puzzle games on a seeded rotation, dungeons, a shared world market, two-layer prestige, and a story about a door that shouldn't exist. everything on screen is generated in code, art and music and sound alike; there are no asset files beyond one icon. `Godot · GDScript`
- **[Hearthfall](https://github.com/VirInvictus/Hearthfall)** · grimdark clan-survival for the terminal. seasonal turns, a fog-black map, and a finite clan split between foraging, exploring, and war. scouting reveals enemy composition, so the fun lives in the preparation rather than the swing. the engine is stdlib-only pure logic with no i/o and no rendering, driveable from a repl; every draw goes through one seeded rng, so a seed replays a run exactly. `Python · Textual`
- **Vestibule** · one-directional converter from an obsidian vault into org-mode that org-roam can index. the finding that makes it tractable: of 326 dataview blocks, 85 are backlinks org-roam already ships for free and ~200 are one templated block, leaving about ten real queries. the replacement query layer is sql over `org-roam.db`, adding no package. private. `Ruby · pandoc`
- **Foyer** · the shared front door to hearth and haveli. pick a game, find the other player on the lan, agree the setup, and foyer relaunches each side already connected. it is not an engine and holds no game rules, so it carries none of their copyrighted content and can stand on its own. `Godot · GDScript`
- **kanagawa-dragon-nvim-emacs** · faithful emacs `deftheme` port of kanagawa.nvim's dragon variant. maps every emacs 29+ tree-sitter `font-lock-*` face, so the same java buffer looks identical in doom and in nvim. an ert suite checks palette parity byte-for-byte against upstream. not yet public. `Emacs Lisp`

### on the drawing board

specs written, little or no code yet.

- **[Coffer](https://github.com/VirInvictus/Coffer)** · envelope budgeting over a plain-text hledger journal. actual budget's experience, hledger's data discipline; the journal is the database and any sqlite is a disposable cache. atrium's sibling, for money. the hard problem is a safe write-back path onto a file you also edit by hand. `Rust · GTK4`
- **dragon-themer** · one palette source of truth rendered through pure erb into every colour-bearing config on the machine, with independent per-group switching. nothing is written until every target renders and passes a syntax check; targets that can cost you a graphical session are verified after reload and auto-restored if the check fails. `Ruby · ERB`
- **project-void** · single-player party-based isometric crpg in the *dark sun* / *fallout 2* / *arcanum* lineage, on lethal *cairn* combat math. the engineering commitment is the engine; the reach, a tight 15–20-hour campaign, is the demonstration. `Godot · Lua · Ink`
- **project-yeschef** · character-driven grand-strategy restaurant sim in the *crusader kings 3* lineage. you play the general manager, not the cook. people are the system, rival gms are load-bearing, and there is no win condition. the former chef's project. `Godot · Lua · Ink`

the full thirty, with screenshots and the long writeups, live in the codex →
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
