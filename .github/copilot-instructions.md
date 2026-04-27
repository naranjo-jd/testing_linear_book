# Copilot Instructions

This is an educational Linear Algebra textbook built with Jupyter Book and TeachBooks. The book uses a Jupyter-based workflow with interactive Python exercises and theoretical content.

## Project Overview

- **Type**: Educational textbook (Linear Algebra in Spanish)
- **Build System**: Jupyter Book v1 with TeachBooks extensions
- **Deployment**: GitHub Pages via TeachBooks deploy workflow
- **Content**: Mix of Markdown files, Jupyter Notebooks (`.ipynb`), and MyST/Sphinx syntax

## Build and Test Commands

**Install dependencies** (run from repository root):
```bash
pip install -r requirements.txt
```

**Build the book locally**:
```bash
jupyter-book build book/
```

**Test a single notebook** (execute without full build):
```bash
jupyter nbconvert --to notebook --execute --inplace book/chapters/XX-chapter/notebook.ipynb
```

**View the built book**:
Open `book/_build/html/index.html` in a browser.

**Clean build** (if needed):
```bash
jupyter-book clean book/
```

**Key build configuration**: `book/_config.yml`
- Notebook execution timeout per cell is set in `execute.timeout`
- Cache path: `book/_build/.jupyter_cache/`
- Only files listed in `_toc.yml` are built (`only_build_toc_files: true`)

### Troubleshooting Build Issues

- **Timeout errors**: Increase `execute.timeout` in `book/_config.yml`
- **Missing pages**: Ensure new files are referenced in `book/_toc.yml`
- **Stale artifacts**: Run `jupyter-book clean book/` before rebuilding
- **Import errors**: Reinstall dependencies from `requirements.txt`

## Architecture and Organization

### Directory Structure

```text
book/
├── _config.yml
├── _toc.yml
├── intro.md
├── chapters/
│   ├── 00-python/
│   ├── 01-espacios_vectoriales_r2/
│   ├── 02-espacios_vectoriales_r3/
│   ├── 03-matrices/
│   ├── 04-determinantes/
│   ├── 05-espacio_fila_columna/
│   ├── 06-transformaciones_lineales/
│   ├── 07-cambios_de_base/
│   └── 08-autovalores_autovectores/
├── figures/
├── talleres/
├── exercises/
└── references.bib
```

### Content Patterns (Current + Target)

- **Template pattern (Chapter 01)**: flat chapter directory with numbered notebooks (`01_*.ipynb`, `02_*.ipynb`, ...), integrated theory/examples/exercises/quizzes.
- **Legacy pattern (mostly Chapters 02-08 currently)**: split `teoria/` and `material/` with `index.md` + `index_material.md`.

When creating or restructuring chapter content, follow the **Chapter 01 template pattern**.

## Key Conventions

### Markdown and Notebook Content

- **Language**: Spanish
- **Math syntax**: `$...$` (inline) and `$$...$$` (display)
- **Exercise blocks**: Sphinx/MyST directives
- **Toggle sections**: `{toggle}` directives
- **Cross-references**: Relative markdown links
- **No emojis** in chapter content

### Chapter Numbering Structure (Template Chapters)

- For template chapters, use explicit hierarchical numbering in notebook headings.
- Notebook title (`#`) format: `C.S Título` (for example `# 1.3 Combinaciones Lineales`), where:
  - `C` = chapter number
  - `S` = section (notebook) number in that chapter
- Main in-notebook sections (`##`) format: `C.S.N. Título` (for example `## 1.3.4. Generado (Span)`), where:
  - `N` = section item number within the notebook
- Nested subsections (`###`) should continue the hierarchy when numbered (for example `### 1.6.4.1 ...`).
- Keep numbering consistent across all notebooks in a chapter and align chapter `index.md` contents with `_toc.yml`.

### File Naming

- Notebook files: `snake_case.ipynb`
- In template chapters: prefer numeric prefixes (for example `01_vectores.ipynb`)
- Markdown files: `snake_case.md`
- Avoid spaces in filenames

### Notebook Cell Tags (Important)

- Visualization code cells: `hide-input`
- Quiz generation cells: `remove-input`
- Interactive/widget initialization: `thebe-init`
- Combine tags where needed (for example quiz + live execution support)

### Interactivity on GitHub Pages

- Thebe is enabled in `book/_config.yml`.
- Interactive cells run after users activate **Live Code** from the rocket button.
- Interactive sections should still be pedagogically understandable without activation.

### TeachBooks and MyST Extensions

Commonly used:
- `sphinx_thebe` / Thebe live code integration
- `sphinx_jupyterbook_latex`
- `sphinx_togglebutton`
- `sphinx_design`
- `colon_fence`, `dollarmath`, `linkify`, `substitution`, `tasklist`

## Editing Guidelines

1. **Edit content** in `.ipynb` / `.md` using MyST-compatible syntax.
2. **Update `_toc.yml`** whenever files are moved, renamed, added, or deleted.
3. **Keep `_config.yml` comments**; they document deployment and build behavior.
4. **Use Chapter 01 as template** for chapter-level restructuring work.
5. **Verify references** so no stale paths to deleted legacy files remain.

## Before Committing

- Ensure `jupyter-book build book/` succeeds
- Confirm generated pages render correctly in `_build/html`
- Confirm all `_toc.yml` references point to existing files

## GitHub Workflow

- Deploy workflow: `.github/workflows/call-deploy-book.yml`
- Pushes affecting `book/`, `requirements.txt`, or workflow files trigger deployment
- Book is published via GitHub Pages
