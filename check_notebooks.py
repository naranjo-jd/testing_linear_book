import json
import sys
import os

def check_notebook(filepath):
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    cells = nb.get('cells', [])
    
    for idx, cell in enumerate(cells):
        cell_type = cell.get('cell_type', '')
        cell_num = idx + 1
        
        # Check code cells for tags
        if cell_type == 'code':
            source = ''.join(cell.get('source', []))
            tags = cell.get('metadata', {}).get('tags', [])
            
            # Check for matplotlib plots without hide-input
            if 'plt.' in source or 'matplotlib' in source:
                if 'plt.show()' in source or 'plt.plot' in source or 'plt.scatter' in source or 'plt.arrow' in source:
                    if 'hide-input' not in tags and 'remove-input' not in tags:
                        issues.append({
                            'cell': cell_num,
                            'type': 'tag',
                            'severity': 'warning',
                            'message': 'Matplotlib visualization without hide-input tag',
                            'tags': tags
                        })
            
            # Check for jupyterquiz without remove-input
            if 'display_quiz' in source or 'from jupyterquiz import display_quiz' in source:
                if 'remove-input' not in tags:
                    issues.append({
                        'cell': cell_num,
                        'type': 'tag',
                        'severity': 'warning',
                        'message': 'JupyterQuiz cell without remove-input tag',
                        'tags': tags
                    })
            
            # Check for widget code
            if 'ipywidgets' in source or 'widgets.' in source or '@interact' in source:
                issues.append({
                    'cell': cell_num,
                    'type': 'widget',
                    'severity': 'info',
                    'message': 'Interactive widget cell - verify visibility settings',
                    'tags': tags,
                    'source_preview': source[:100]
                })
    
    return issues

# Check each notebook
notebooks = [
    'book/chapters/01-espacios_vectoriales_r2/01_vectores.ipynb',
    'book/chapters/01-espacios_vectoriales_r2/02_operaciones.ipynb',
    'book/chapters/01-espacios_vectoriales_r2/03_combinaciones_lineales.ipynb',
    'book/chapters/01-espacios_vectoriales_r2/04_independencia_lineal.ipynb',
    'book/chapters/01-espacios_vectoriales_r2/05_subespacios.ipynb',
    'book/chapters/01-espacios_vectoriales_r2/06_rectas.ipynb',
    'book/chapters/01-espacios_vectoriales_r2/07_producto_punto.ipynb',
    'book/chapters/01-espacios_vectoriales_r2/08_ejercicios_capitulo.ipynb',
    'book/chapters/01-espacios_vectoriales_r2/09_examen.ipynb',
]

all_issues = {}
for nb_path in notebooks:
    try:
        if os.path.exists(nb_path):
            issues = check_notebook(nb_path)
            if issues:
                all_issues[nb_path] = issues
    except Exception as e:
        print(f'Error checking {nb_path}: {e}')

# Print results
print(json.dumps(all_issues, indent=2))
