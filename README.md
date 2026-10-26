# codif-ape-docs

Technical note on INSEE's MLOps pipeline for the automatic coding of economic activity (APE / NAF / NACE), as a bilingual Quarto website.

Live site: <https://inseefrlab.github.io/codif-ape-docs/>

## Structure

- `index.qmd`: root page, redirects to `en/`, or to `fr/` if the reader last chose French
- `en/*.qmd`: English version
- `fr/*.qmd`: French version, with the same file names and the same anchors (`#sec-…`, `#tbl-…`, `fig-…`)
- `references.bib`: bibliography shared by both versions
- `style/styles.scss`: theme (Bootswatch `litera` with a few rules)
- `style/nav.html`: the single, collapsible table of contents in the left sidebar, and the EN | FR switch in the navbar, which swaps the page to the other language in place (same page, same section, no reload)
- `scripts/outline.py`: post-render script that writes `_site/outline.json`, the plan of the note (chapters, sections, sub-sections) read by `style/nav.html`
- `codif-ape-prez/`: submodule holding the presentations. It is **not** rendered here: the site links to <https://inseefrlab.github.io/codif-ape-prez/>.

Every change must be made in **both languages**.

## Authors

Each chapter lists its own authors in its front matter, shown under the title. Set them in both languages (`en/<chapter>.qmd` and `fr/<chapter>.qmd`):

```yaml
author:
  - name: Jane Doe
    affiliations:
      - Insee
  - name: John Doe
    affiliations:
      - Insee
      - CREST
```

Quarto also accepts `email`, `orcid`, `url` and `corresponding: true` for each author.

## Build locally

```bash
quarto preview
```

## Deployment

On each push to `main`, `.github/workflows/publish.yaml` renders the site and publishes it to the `gh-pages` branch. Under *Settings → Pages*, GitHub Pages must serve from the `gh-pages` branch.
