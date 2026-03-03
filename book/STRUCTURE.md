# Estructura del Proyecto

Este documento describe la organización del repositorio para que colaboradores puedan entender cómo está estructurado el libro y dónde agregar contenido nuevo.

---

## Directorio raíz

```
/
├── book/                    # Todo el contenido del libro
├── .github/
│   ├── workflows/           # Deploy automático a GitHub Pages
│   └── copilot-instructions.md
├── .gitignore
├── CITATION.cff             # Metadata de citación
├── CODEOWNERS               # Responsables del repositorio
├── CONTRIBUTING.md          # Guía para contribuir
├── LICENSE
├── README.md
├── requirements.txt         # Dependencias Python
└── WAIVER
```

---

## Directorio `book/`

```
book/
├── _config.yml              # Configuración de Jupyter Book (no borrar comentarios)
├── _toc.yml                 # Tabla de contenidos — controla qué se construye y en qué orden
├── intro.md                 # Página de inicio del libro
├── references.bib           # Bibliografía en formato BibTeX
├── references.md            # Página de referencias en el libro
├── credits.md               # Créditos del libro
├── changelog.md             # Registro de cambios
├── figures/                 # Imágenes y diagramas compartidos
├── chapters/                # Capítulos del libro
├── talleres/                # Talleres transversales
└── trash/                   # Archivos archivados (no se publican)
```

---

## Estructura de un capítulo

Cada capítulo sigue esta estructura estándar:

```
chapters/NN-nombre_capitulo/
├── index.md                 # Introducción teórica del capítulo
├── index_material.md        # Introducción a la sección de ejercicios (opcional)
├── teoria/                  # Notebooks de contenido teórico
│   ├── concepto.ipynb
│   ├── ejemplos.ipynb
│   └── ...
└── material/                # Notebooks de ejercicios y actividades
    ├── actividad_enganche.ipynb
    ├── quiz_conceptos.ipynb
    ├── ejercicios_computacionales.ipynb
    ├── ejercicios_teoricos.ipynb
    └── actividad_computacional.ipynb
```

### Convenciones de nombres

| Tipo | Patrón | Ejemplo |
|------|--------|---------|
| Carpeta de capítulo | `NN-nombre_descriptivo` | `03-matrices` |
| Notebook de teoría | `snake_case.ipynb` | `sistemas_homogeneos.ipynb` |
| Notebook de material | Nombre estándar (ver tabla abajo) | `quiz_conceptos.ipynb` |
| Archivos Markdown | `snake_case.md` | `index_material.md` |

### Notebooks de `material/` — nombres estándar

| Archivo | Propósito |
|---------|-----------|
| `actividad_enganche.ipynb` | Actividad inicial de motivación |
| `quiz_conceptos.ipynb` | Quiz de conceptos del capítulo |
| `ejercicios_computacionales.ipynb` | Ejercicios con código Python |
| `ejercicios_teoricos.ipynb` | Ejercicios teóricos/analíticos |
| `actividad_computacional.ipynb` | Actividad computacional integradora |
| `examen.ipynb` | Evaluación del capítulo (opcional) |

---

## Capítulos actuales

| Carpeta | Contenido |
|---------|-----------|
| `00-python` | Fundamentos de Python para álgebra lineal |
| `01-espacios_vectoriales_r2` | Espacios vectoriales en R² |
| `02-espacios_vectoriales_r3` | Espacios vectoriales en R³ |
| `03-matrices` | Matrices y sistemas de ecuaciones |
| `04-determinantes` | Determinantes y regla de Cramer |
| `05-espacio_fila_columna` | Espacio fila, columna y dimensión |
| `06-transformaciones_lineales` | Transformaciones lineales |
| `07-cambios_de_base` | Cambios de base |
| `08-autovalores_autovectores` | Autovalores y autovectores |

---

## Tabla de contenidos (`_toc.yml`)

El archivo `book/_toc.yml` controla qué archivos se incluyen en el libro publicado y en qué orden aparecen. **Todo archivo nuevo debe ser agregado aquí para que aparezca en el libro.**

Estructura del TOC:
```yaml
format: jb-book
root: intro.md

parts:
  - caption: "N. Nombre del capítulo"
    chapters:
      - file: chapters/NN-nombre/index.md
        sections:
          - file: chapters/NN-nombre/teoria/notebook.ipynb
      - file: chapters/NN-nombre/index_material.md
        sections:
          - file: chapters/NN-nombre/material/actividad_enganche.ipynb
```

---

## Build del libro

```bash
# Instalar dependencias
pip install -r requirements.txt

# Construir el libro
jupyter-book build book/

# Ver resultado
open book/_build/html/index.html   # macOS
xdg-open book/_build/html/index.html  # Linux

# Limpiar build anterior
jupyter-book clean book/
```

Para probar un notebook individual sin construir todo el libro:
```bash
jupyter nbconvert --to notebook --execute --inplace book/chapters/NN-capitulo/teoria/notebook.ipynb
```
