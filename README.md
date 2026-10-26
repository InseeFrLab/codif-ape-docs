# codif-ape-docs

Technical note on INSEE's MLOps pipeline for the automatic coding of economic activity (APE / NAF / NACE), as a bilingual Quarto website.

Live site: <https://inseefrlab.github.io/codif-ape-docs/>

## Structure

- `index.qmd`: root page, redirects to `en/` or `fr/` (the reader's last choice, otherwise their browser's language)
- `en/*.qmd`: English version
- `fr/*.qmd`: French version, with the same file names and the same anchors (`#sec-…`, `#tbl-…`, `fig-…`)
- `references.bib`: bibliography shared by both versions
- `style/styles.scss`: theme (Bootswatch `litera` with a few rules)
- `style/lang-switch.html`: EN | FR switch in the navbar, which opens the same page and section in the other language
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
