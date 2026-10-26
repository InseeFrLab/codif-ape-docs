"""Post-render: write outline.json, the plan of the whole note for the left sidebar.

For each language, it lists the chapters in sidebar order, each with its
sections and sub-sections, as rendered by Quarto in the page's own table of
contents (nav#TOC). style/nav.html reads this file to build a single,
collapsible table of contents for the whole note.
"""

import json
import os
import re
from pathlib import Path

LANGS = ("en", "fr")

out_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))

SIDEBAR_LINK = re.compile(
    r'<a href="\.\./(?P<lang>en|fr)/(?P<file>[^"#]+\.html)"[^>]*class="sidebar-item-text sidebar-link[^"]*">\s*'
    r'<span class="menu-text">(?P<title>.*?)</span>',
    re.S,
)
TOC = re.compile(r'<nav id="TOC"[^>]*>(?P<body>.*?)(?:<div class="toc-actions">|</nav>)', re.S)
TOC_TOKEN = re.compile(r'<ul[^>]*>|</ul>|<a href="#(?P<id>[^"]+)"[^>]*>(?P<html>.*?)</a>', re.S)
SECTION_NUMBER = re.compile(r'<span class="header-section-number">.*?</span>\s*', re.S)


def chapters(lang):
    """Chapters in sidebar order, read from the rendered landing page."""
    index = (out_dir / lang / "index.html").read_text(encoding="utf-8")
    sidebar = index[index.index('id="quarto-sidebar"'):]
    return [
        (m["file"], m["title"].strip())
        for m in SIDEBAR_LINK.finditer(sidebar)
        if m["lang"] == lang
    ]


def sections(page):
    """Nested sections of a rendered page, from its table of contents."""
    m = TOC.search(page)
    if not m:
        return []
    root = []
    stack = [root]
    last = None
    for tok in TOC_TOKEN.finditer(m["body"]):
        text = tok.group(0)
        if text.startswith("<ul"):
            # The outer <ul> opens the top level; nested ones hang under the
            # last section seen.
            if last is not None:
                stack.append(last["children"])
        elif text == "</ul>":
            if len(stack) > 1:
                stack.pop()
        else:
            last = {
                "id": tok["id"],
                "title": SECTION_NUMBER.sub("", tok["html"]).strip(),
                "children": [],
            }
            stack[-1].append(last)
    return root


def numbered(page):
    """Whether the page numbers its sections (number-sections: true)."""
    return 'class="header-section-number"' in page


outline = {}
for lang in LANGS:
    number = 0
    items = []
    for file, title in chapters(lang):
        page = (out_dir / lang / file).read_text(encoding="utf-8")
        item = {"href": file, "title": title, "sections": sections(page)}
        if numbered(page):
            number += 1
            item["number"] = number
        items.append(item)
    outline[lang] = items

(out_dir / "outline.json").write_text(
    json.dumps(outline, ensure_ascii=False, indent=1), encoding="utf-8"
)
