# Repository Improvement Suggestions

Based on analysis of the project structure, here are concrete improvement suggestions organized by priority.

## 🎯 HIGH PRIORITY (Quick Wins)

### 1. **Clean up root book/ directory**
**Current issue**: Scattered files that should be organized
```
book/
├── borrador.txt                    ← unclear purpose, should be .gitignored
├── file_to_be_added_to_toc.md      ← descriptive filename (fix or delete)
├── exercises.md, syntax_exercises.md ← should be in docs/ folder
├── extensions.md                    ← should be in docs/
└── exercises/                       ← orphaned directory?
```

**Suggestion**:
```
book/
├── _config.yml
├── _toc.yml
├── intro.md
├── content/                 ← ALL chapter content here
│   ├── 01-python/
│   ├── 02-r2/
│   ├── 03-r3/
│   ├── 04-matrices/
│   ├── 05-determinantes/
│   ├── 06-espacio-fila-columna/
│   └── references/          ← references.md, credits.md, changelog.md
├── docs/                    ← instructional/meta content
│   ├── EXTENSION.md
│   └── SYNTAX.md
├── _build/                  ← gitignored (build output)
└── figures/
```

### 2. **Remove duplicate/unused files**
- `_toc2.yml` — delete if truly unused, or document its purpose
- `borrador.txt` — either commit as work-in-progress OR delete and move to a branch
- `file_to_be_added_to_toc.md` — rename to something meaningful or delete

### 3. **Fix inconsistent notebook naming**
**Current patterns** (inconsistent):
```
taller0(python_basico).ipynb        ← problematic: spaces + parentheses
quiz_conceptos.ipynb vs quiz_conceptos_1.ipynb  ← version numbering unclear
combinaciones_lineales.ipynb        ← under r3, not in material/ subfolder
independencia_lineal.ipynb          ← same issue
```

**Suggestion**: Adopt consistent pattern:
```
# Across all chapters, use this structure:
chapter/
├── index.md                         # Overview
├── material/                        # Student-facing content
│   ├── 01-actividad-enganche.ipynb
│   ├── 02-quiz-conceptos.ipynb
│   ├── 03-ejercicios-teoricos.ipynb
│   ├── 04-ejercicios-computacionales.ipynb
│   ├── 05-actividad-computacional.ipynb
│   └── 06-examen.ipynb
└── teoria/                          # Theory/reference content
    ├── conceptos-basicos.ipynb
    └── aplicaciones.ipynb
```

---

## 📋 MEDIUM PRIORITY (Better Organization)

### 4. **Standardize chapter organization**
Currently **inconsistent**:
- `python/` — flat, no material/teoria split
- `r2/` — has material/ + teoria/
- `r3/` — mixed (some files in root, some might be elsewhere)
- `matrices/` — flat, mixed content types

**Suggestion**: All chapters should follow the same pattern:
```
chapter-name/
├── index.md              # Intro/overview
├── index-material.md     # Links to exercises (optional)
├── material/             # Student exercises
└── teoria/               # Theory/reference notebooks
```

### 5. **Add STRUCTURE.md documentation**
Create a file explaining the organization so contributors understand:
```
book/
├── _config.yml
├── _toc.yml
├── STRUCTURE.md          ← Explains directory layout
├── content/
│   ├── 01-python/
│   └── ...
```

### 6. **Implement consistent numbering**
Make chapter order explicit in folder names:
```
content/
├── 01-python-basicos/
├── 02-espacios-vectoriales-r2/
├── 03-espacios-vectoriales-r3/
├── 04-matrices-sistemas/
├── 05-determinantes/
└── 06-espacio-fila-columna/
```

Benefits:
- Clear progression
- Easy to reorder
- Prevents ambiguity

---

## 🔧 LOWER PRIORITY (Polish)

### 7. **Rename chapter directories for clarity**
```
r2/ → espacios-vectoriales-r2/
r3/ → espacios-vectoriales-r3/
```
More descriptive and easier for translators/contributors to understand.

### 8. **Move root-level metadata**
```
book/ root should only have:
├── _config.yml
├── _toc.yml
├── intro.md
├── STRUCTURE.md
├── content/
└── figures/

Move to book/docs/:
├── references.md
├── credits.md
├── changelog.md
├── extensions.md  (or move to root-level docs/)
```

### 9. **Create .gitignore rules**
Ensure these are ignored:
```
book/_build/
book/.jupyter_cache/
borrador.txt
*.pyc
.DS_Store
```

### 10. **Add CONTRIBUTING.md**
Document:
- How to add new exercises
- Notebook naming conventions
- How to add chapters
- Where to edit references

---

## 📊 Summary Table

| Issue | Impact | Effort | Suggestion |
|-------|--------|--------|-----------|
| Root directory clutter | Low clarity | 15 min | Organize into `content/` |
| Inconsistent notebook naming | Confusing | 1 hour | Adopt `NN-name.ipynb` pattern |
| Duplicate `_toc2.yml` | Maintenance debt | 5 min | Delete or document |
| Unstructured chapters | Hard to scale | 2-3 hours | Standardize all chapters |
| No documentation of structure | Contributor friction | 30 min | Add STRUCTURE.md |
| Unclear file purposes | Clutter | 10 min | Delete `borrador.txt`, rename `file_to_be_added_to_toc.md` |

---

## 🚀 Recommended Implementation Order

1. **Start**: Delete/fix low-hanging fruit (`borrador.txt`, `_toc2.yml`, rename `file_to_be_added_to_toc.md`)
2. **Rename**: Use numbered chapter folders (`01-`, `02-`, etc.)
3. **Reorganize**: Move files into consistent `material/` + `teoria/` structure
4. **Document**: Create STRUCTURE.md explaining conventions
5. **Enhance**: Add CONTRIBUTING.md

---

## Next Steps

Consider:
- **Create a detailed refactoring plan** with specific steps?
- **Implement any of these changes** (restructuring)?
- **Create template files** (STRUCTURE.md, CONTRIBUTING.md)?
