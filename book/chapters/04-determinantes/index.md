# 📐 Capítulo: Determinantes y Regla de Cramer

En este capítulo estudiaremos una de las herramientas más importantes del álgebra lineal: los **determinantes**.  
El determinante de una matriz no es solo un número: es una medida geométrica, algebraica e incluso computacionalmente significativa.

También aprenderás a resolver sistemas lineales mediante la **regla de Cramer**, un método elegante y directo basado en determinantes.

---

## 🎯 Objetivos del capítulo

Al finalizar este bloque podrás:

- Comprender el significado **geométrico** y **algebraico** de un determinante.
- Calcular determinantes de matrices \(2\times 2\), \(3\times 3\) y \(n\times n\).
- Aplicar propiedades fundamentales como expansión por cofactores, efectos del intercambio de filas, y factorización.
- Relacionar el determinante con:
  - invertibilidad de matrices,
  - volumen en espacios de dimensión \(n\),
  - orientación,
  - sistemas lineales.
- Resolver sistemas mediante la **regla de Cramer** cuando sea aplicable.

El enfoque será **conceptual, geométrico y computacional**, usando Python (NumPy y SymPy) para experimentar con determinantes y sistemas.

---

## 📂 Contenidos del capítulo

### 🔹 1. Determinantes: introducción y significado  
📘 Archivo: `determinantes/determinante_introduccion.ipynb`

> Introduce la idea del determinante, su motivación geométrica y su interpretación algebraica.  
> Incluye ejemplos visuales en 2D y 3D para comprender escalamiento de área y volumen.

---

### 🔹 2. Cálculo de determinantes  
📘 Archivo: `determinantes/determinante_calculo.ipynb`

> Aprenderás a calcular determinantes mediante:
> - fórmulas cerradas \(2\times2\) y \(3\times3\)  
> - expansión por cofactores  
> - propiedades del determinante  
> - métodos computacionales con Python  
>  
> Conexiones claras entre cálculo y geometría.

---

### 🔹 3. Propiedades fundamentales del determinante  
📘 Archivo: `determinantes/propiedades.ipynb`

> Analiza las propiedades estructurales que convierten al determinante en una herramienta poderosa:  
> - efecto de intercambiar filas o multiplicarlas  
> - factor de escala  
> - multiplicatividad: \(\det(AB)=\det(A)\det(B)\)  
> - relación con el rango e invertibilidad  
> - determinante de matrices especiales (triangulares, diagonales, ortogonales)

---

### 🔹 4. Regla de Cramer  
📘 Archivo: `determinantes/regla_cramer.ipynb`

> Explica la regla de Cramer como un método directo para solucionar sistemas lineales:  
> \[
> A\mathbf{x}=\mathbf{b},\quad \det(A)\neq 0
> \]  
>  
> Se incluyen ejemplos numéricos y simbólicos, interpretaciones geométricas y comparación con otros métodos de resolución.

---

### 🔹 5. Aplicaciones del determinante  
📘 Archivo: `determinantes/aplicaciones.ipynb`

> Muestra cómo los determinantes aparecen de forma natural en:  
> - cambio de variables en integrales múltiples  
> - transformaciones lineales que escalan áreas/volúmenes  
> - cálculo de volúmenes mediante productos cruz y mixtos  
> - análisis de estabilidad (autovalores, Jacobianos)

---

## 🧠 Conexión con capítulos anteriores

| Tema anterior | Relación |
|--------------|----------|
| Matrices | El determinante es una función clave sobre matrices cuadradas |
| Sistemas lineales | Determina existencia/unicidad de soluciones |
| Subespacios y núcleos | \(\det(A)=0\) ↔ presencia de dependencia lineal |
| Transformaciones | Escala áreas, volúmenes y refleja orientación |

---

## 🧮 Competencias que desarrollarás

| Competencia | Descripción |
|-------------|-------------|
| **C1. Cálculo matricial** | Computar determinantes en distintas dimensiones |
| **C2. Razonamiento geométrico** | Comprender escalamiento y orientación |
| **C3. Resolución de sistemas** | Aplicar profesionalmente la regla de Cramer |
| **C4. Pensamiento computacional** | Implementar determinantes y Cramer en Python |
| **C5. Análisis teórico** | Usar propiedades profundas del determinante |

---

## 💬 Reflexión inicial

El determinante no es solo una fórmula:  
es una herramienta que revela si una transformación deforma, aplasta, rota o invierte el espacio.

> **“El determinante mide cómo una transformación lineal cambia el espacio por dentro.”**

---

## 🚀 Siguiente paso

Comienza con la lección:  
👉 **Determinantes: Introducción y significado** (`determinante_introduccion.ipynb`)
