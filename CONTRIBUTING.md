# Guía de Contribución

¡Gracias por tu interés en contribuir a este libro de Álgebra Lineal! Esta guía explica cómo agregar y modificar contenido correctamente.

---

## Primeros pasos

1. **Clona el repositorio** (o haz un fork si no tienes acceso directo):
   ```bash
   git clone https://github.com/abelalv/testing_linear_book.git
   cd testing_linear_book
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Crea una rama** para tus cambios:
   ```bash
   git checkout -b mi-contribucion
   ```

---

## Entender la estructura

Antes de contribuir, lee [`book/STRUCTURE.md`](book/STRUCTURE.md) para entender cómo está organizado el libro.

---

## Agregar contenido a un capítulo existente

### Nuevo notebook de teoría
1. Crea el archivo en `book/chapters/NN-capitulo/teoria/nombre.ipynb`
2. Agrega la entrada en `book/_toc.yml` dentro de las `sections:` del capítulo
3. Verifica que el notebook ejecuta correctamente:
   ```bash
   jupyter nbconvert --to notebook --execute --inplace book/chapters/NN-capitulo/teoria/nombre.ipynb
   ```

### Nuevo notebook de ejercicios
1. Crea el archivo en `book/chapters/NN-capitulo/material/nombre.ipynb`
2. Usa los nombres estándar donde sea posible (ver `STRUCTURE.md`)
3. Agrega la entrada en `book/_toc.yml`

---

## Agregar un capítulo nuevo

1. Crea la carpeta del capítulo con número secuencial:
   ```bash
   mkdir -p book/chapters/09-nuevo_capitulo/teoria
   mkdir -p book/chapters/09-nuevo_capitulo/material
   ```

2. Crea los archivos mínimos:
   - `book/chapters/09-nuevo_capitulo/index.md` — introducción del capítulo
   - `book/chapters/09-nuevo_capitulo/index_material.md` — introducción a ejercicios

3. Agrega el capítulo al final de `book/_toc.yml` (antes de "Referencias y créditos")

---

## Convenciones importantes

- **Idioma del contenido**: español
- **Nombres de archivos**: `snake_case` sin espacios ni acentos (ej. `espacios_vectoriales.ipynb`)
- **Matemáticas**: usar `$...$` para inline y `$$...$$` para display
- **No borrar** los comentarios de `book/_config.yml` — documentan cada configuración
- **No agregar** archivos directamente en la raíz de `book/chapters/NN-capitulo/` — todo debe ir en `teoria/` o `material/`

---

## Verificar antes de hacer commit

```bash
# Validar que _toc.yml tiene sintaxis correcta
python3 -c "import yaml; yaml.safe_load(open('book/_toc.yml'))" && echo "OK"

# Construir el libro completo
jupyter-book build book/

# Revisar que no hay errores en la salida
```

---

## Proceso de contribución

1. Haz tus cambios en una rama
2. Verifica que el libro construye sin errores
3. Haz commit con un mensaje descriptivo:
   ```bash
   git commit -m "feat: agrega notebook de eigenvalores al capítulo 08"
   ```
4. Abre un Pull Request hacia `main`
5. Espera revisión de `@abelalv` o `@naranjo-jd`

---

## Contacto

- **Autor principal**: Abel Alvarez — abel.alvarez@javerianacali.edu.co
- **Colaborador**: Juan Diego Naranjo — juand8@javerianacali.edu.co
