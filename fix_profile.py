with open("README.md", "r") as f:
    text = f.read()

# Add utilities section
utils = """
### desktop & utilities

- **[Atrium](https://github.com/VirInvictus/Atrium)** · a local-first, native linux task manager built on the Getting Things Done philosophy. getting your life in order should not require a subscription, an electron app, or an active internet connection. built on a single-writer sqlite worker with search powered by `vir-search` and a clean `vir-gtk` interface. `Rust · GTK4` · *shipping v0.70.0*
- **[Viaduct](https://github.com/VirInvictus/Viaduct)** · a fast, local-first rss reader that treats articles as text, not web pages. `Rust · GTK4` · *shipping v3.3.1*
- **[vir-search](https://github.com/VirInvictus/vir-search)** · a shared rust library for parsing calibre-style search expressions into a typed AST. used by Atrium and Conservatory. `Rust` · *complete v1.0.1*
- **[vir-gtk](https://github.com/VirInvictus/vir-gtk)** · a shared gtk4 styling library for native linux apps, extracting the Kanagawa theme engine. `Rust · GTK4` · *complete v1.0.1*
"""

if "### desktop & utilities" not in text:
    text = text.replace("### books & calibre", utils.strip() + "\n\n### books & calibre")

with open("README.md", "w") as f:
    f.write(text)

