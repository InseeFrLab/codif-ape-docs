# codif-ape-docs

Technical note on INSEE's MLOps pipeline for the automatic coding of economic activity (APE / NAF / NACE), as a bilingual Quarto website.

Live site: <https://inseefrlab.github.io/codif-ape-docs/>

## Structure

- `index.qmd`: landing page (language choice)
- `en/*.qmd`: English version
- `fr/*.qmd`: French version, with the same file names and the same anchors (`#sec-…`, `#tbl-…`, `fig-…`)
- `references.bib`: bibliography shared by both versions
- `style/styles.scss`: theme
- `codif-ape-prez/`: submodule holding the presentations. It is **not** rendered here: the site links to <https://inseefrlab.github.io/codif-ape-prez/>.

Every change must be made in **both languages**.

## Build locally

```bash
quarto preview
```

## Deployment

On each push to `main`, `.github/workflows/publish.yaml` renders the site and publishes it to the `gh-pages` branch. Under *Settings → Pages*, GitHub Pages must serve from the `gh-pages` branch.
