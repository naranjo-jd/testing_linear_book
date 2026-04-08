import json
import os

def review_cell_tags(filepath):
    """Detailed review of cell tags and interactive code."""
    print(f"\n{'='*80}")
    print(f"Reviewing: {os.path.basename(filepath)}")
    print(f"{'='*80}\n")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    cells = nb.get('cells', [])
    issues_found = False
    
    for idx, cell in enumerate(cells):
        cell_type = cell.get('cell_type', '')
        cell_num = idx + 1
        
        if cell_type == 'code':
            source = ''.join(cell.get('source', []))
            tags = cell.get('metadata', {}).get('tags', [])
            
            # Check for matplotlib plots without hide-input
            has_plot = any(pattern in source for pattern in ['plt.show()', 'plt.plot(', 'plt.scatter(', 'plt.arrow(', 'plt.figure('])
            has_widgets = any(pattern in source for pattern in ['@interact', 'interact(', 'FloatSlider', 'IntSlider', 'widgets.'])
            has_quiz = 'display_quiz' in source
            
            if has_plot and has_widgets:
                # Interactive visualization - code should be visible unless specifically hidden
                if 'hide-input' in tags or 'remove-input' in tags:
                    print(f"⚠️  Cell {cell_num}: Interactive widget with visualization")
                    print(f"    Tags: {tags}")
                    print(f"    Note: Interactive widgets typically should show code for learning")
                    print(f"    Source preview: {source[:150]}...")
                    print()
                    issues_found = True
            elif has_plot and not has_widgets:
                # Static visualization - should have hide-input
                if 'hide-input' not in tags and 'remove-input' not in tags:
                    print(f"❌ Cell {cell_num}: Static matplotlib visualization WITHOUT hide-input tag")
                    print(f"    Current tags: {tags}")
                    print(f"    Expected: ['hide-input']")
                    print(f"    Source preview: {source[:150]}...")
                    print()
                    issues_found = True
            
            if has_quiz:
                # Quiz cells should have remove-input
                if 'remove-input' not in tags:
                    print(f"❌ Cell {cell_num}: JupyterQuiz cell WITHOUT remove-input tag")
                    print(f"    Current tags: {tags}")
                    print(f"    Expected: ['remove-input']")
                    print(f"    Source preview: {source[:150]}...")
                    print()
                    issues_found = True
        
        elif cell_type == 'markdown':
            source = ''.join(cell.get('source', []))
            
            # Check for LaTeX issues
            # Look for common problems
            if '\\vec' in source or '\\mathbf' in source:
                # Check consistency
                has_vec = '\\vec{' in source
                has_mathbf = '\\mathbf{' in source
                if has_vec and has_mathbf:
                    print(f"⚠️  Cell {cell_num}: Inconsistent vector notation (both \\vec and \\mathbf used)")
                    print(f"    Consider using one consistently throughout")
                    print()
                    issues_found = True
            
            # Check for unmatched $ delimiters
            dollar_count = source.count('$')
            if dollar_count % 2 != 0:
                print(f"❌ Cell {cell_num}: Unmatched $ delimiter in markdown")
                print(f"    Found {dollar_count} dollar signs (should be even)")
                print(f"    Source preview: {source[:200]}...")
                print()
                issues_found = True
            
            # Check for double $$ issues
            if '$$' in source:
                parts = source.split('$$')
                if len(parts) % 2 == 0:
                    print(f"❌ Cell {cell_num}: Unmatched $$ delimiter in markdown")
                    print(f"    Found {len(parts)-1} double dollar signs (should be even)")
                    print()
                    issues_found = True
    
    if not issues_found:
        print("✓ No issues found")
    
    return issues_found

# Review all notebooks
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

total_issues = 0
for nb_path in notebooks:
    if os.path.exists(nb_path):
        if review_cell_tags(nb_path):
            total_issues += 1

print(f"\n{'='*80}")
print(f"Summary: Issues found in {total_issues} notebook(s)")
print(f"{'='*80}")
