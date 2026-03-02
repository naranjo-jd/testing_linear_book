# Copilot Instructions

This is an educational Linear Algebra textbook built with Jupyter Book and TeachBooks. The book uses a Jupyter-based workflow with interactive Python exercises and theoretical content.

## Project Overview

- **Type**: Educational textbook (Linear Algebra in Spanish)
- **Build System**: Jupyter Book v1 with TeachBooks extensions
- **Deployment**: GitHub Pages via TeachBooks deploy workflow
- **Content**: Mix of Markdown files, Jupyter Notebooks (.ipynb), and Sphinx/MyST syntax

## Build and Test Commands

**Install dependencies** (run from repository root):
```bash
pip install -r requirements.txt
```

**Build the book locally**:
```bash
jupyter-book build book/
```

**Test a single notebook** (execute without building):
```bash
jupyter nbconvert --to notebook --execute --inplace book/chapters/XX-chapter/notebook.ipynb
```

**View the built book**:
After building, open `book/_build/html/index.html` in a browser.

**Clean build** (if needed):
```bash
jupyter-book clean book/
```

**Key build configuration**: Uses `_config.yml` in `book/` directory
- Notebooks execute during build with 30-second timeout per cell (adjust `timeout` in `execute` section if needed)
- Cache stored in `book/_build/.jupyter_cache/`
- Only files in `_toc.yml` are built (controlled by `only_build_toc_files: true`)

### Troubleshooting Build Issues

- **"Timeout" errors**: Increase `execute.timeout` in `book/_config.yml` for computationally intensive notebooks
- **Missing files in _toc.yml**: Verify paths point to `book/chapters/XX-chapter/` structure, not legacy paths
- **Stale build artifacts**: Run `jupyter-book clean book/` before rebuilding
- **Import errors**: Ensure dependencies from `requirements.txt` are installed (`pip install -r requirements.txt`)

## Architecture & Organization

### Directory Structure

```
book/
├── _config.yml          # Jupyter Book configuration (do not delete comments—they document settings)
├── _toc.yml             # Main table of contents (chapters/sections order)
├── intro.md             # Main introduction page
├── chapters/            # Numbered chapter directories
│   ├── 00-python/       # Chapter 0: Python fundamentals
│   │   ├── index.md
│   │   └── *.ipynb      # Theory and exercises
│   ├── 01-r2/           # Chapter 1: Vector spaces in R²
│   │   ├── teoria/      # Theoretical content
│   │   └── material/    # Exercises and activities
│   ├── 02-r3/           # Chapter 2: Vector spaces in R³
│   ├── 03-matrices/     # Chapter 3: Matrices and systems
│   ├── 04-determinantes/# Chapter 4: Determinants
│   └── 05-espacio_fila_columna/ # Chapter 5: Row/column spaces
├── figures/             # Images and diagrams
├── talleres/            # Workshop/activity notebooks
├── exercises/           # Standalone exercise files
└── references.bib       # Bibliography (BibTeX format)
```

### Content Patterns

Each major chapter (e.g., `chapters/01-r2/`, `chapters/03-matrices/`) follows this organization:
- `index.md`: Theory and conceptual explanations
- `index_material.md`: Activities and exercises (in some chapters)
- Theory notebooks in `teoria/` subdirectory (where applicable)
- Material notebooks in `material/` subdirectory containing:
  - `actividad_enganche.ipynb`: Hook/engagement activity
  - `quiz_conceptos.ipynb`: Concept quiz
  - `ejercicios_computacionales.ipynb`: Computational exercises
  - `ejercicios_teoricos.ipynb`: Theoretical exercises
  - `actividad_computacional.ipynb`: Computational activity
- Workshop notebooks in `talleres/` directory at book root

### Notebook Dependencies

Notebooks rely on standard Scientific Python stack:
- `numpy`: Numerical computations
- `matplotlib`: Plotting
- `ipywidgets`: Interactive elements
- `jupyterquiz`: Quiz functionality (via teachbooks)

## Key Conventions

### Markdown & Notebook Content

- **Language**: Spanish
- **Math syntax**: MyST-enabled `$...$` for inline, `$$...$$` for display math (dollarmath enabled)
- **Exercise blocks**: Use Sphinx directives for structured exercise markup
- **Toggle sections**: Use `{toggle}` directive for collapsible content
- **Cross-references**: Markdown link syntax `[text](file.md)` or relative paths

### File Naming

- Notebook files: `snake_case.ipynb` (e.g., `espacios_vectoriales.ipynb`)
- Markdown: `snake_case.md`
- Avoid spaces in filenames
- Keep Spanish accents in descriptive text, underscores in file names

### TeachBooks Extensions

The build process includes TeachBooks-specific features:
- **Image inversion**: Figures automatically inverted for dark mode (controlled by `inverter_all: true`)
- **Tooltip support**: Tooltips for figures, tables, Wikipedia/DOI links
- **Code examples**: Via `sphinx-code-examples` extension
- **Live code**: Via Thebe (requires `{thebe}` blocks in notebooks)

### MyST Extensions Enabled

In `_config.yml` parse section:
- `colon_fence`: Triple-colon syntax for directive blocks
- `dollarmath`: Math delimiters `$...$` and `$$...$$`
- `linkify`: Auto-detect URLs
- `substitution`: Variable substitution
- `tasklist`: Markdown task lists

## Editing Guidelines

### When Editing Content

1. **Content changes**: Edit `.ipynb` or `.md` files directly
   - For notebooks: ensure cells have proper output (or set `execute_notebooks: "force"` in _config.yml)
   - For Markdown: use MyST syntax

2. **Modifying structure**: Update `_toc.yml`
   - Add new chapter entries here, not elsewhere
   - Follow the `file:` and `sections:` hierarchy

3. **Bibliography**: Add entries to `references.bib`
   - Use BibTeX format
   - Reference from content using MyST citation syntax

4. **Configuration changes**: Edit `book/_config.yml`
   - Preserve all comments (they document what each setting controls)
   - Refer to linked documentation URLs for option details
   - Common changes: `author`, `html_baseurl`, `repository_url`, `repository_branch`

### Before Committing

- After build changes, verify: `jupyter-book build book/` completes without errors
- Check that `book/_build/html/index.html` renders correctly
- All referenced files in `_toc.yml` must exist

## GitHub Workflow

- Automatic deployment: Pushes to any branch trigger the TeachBooks deploy workflow (`.github/workflows/call-deploy-book.yml`)
- Workflow file location matters: changes to `book/`, `requirements.txt`, or the workflow file itself trigger deployment
- Build artifacts: Deployed to GitHub Pages (check repository settings for pages branch)
