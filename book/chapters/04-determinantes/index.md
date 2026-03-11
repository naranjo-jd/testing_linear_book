# 📐 Capítulo 4: Determinantes y Regla de Cramer

En este capítulo estudiaremos una de las herramientas más importantes del álgebra lineal: los **determinantes**.  
El determinante de una matriz no es solo un número: es una medida geométrica, algebraica e incluso computacionalmente significativa.

---

## 🎯 Objetivos del capítulo

Al finalizar este bloque podrás:
- Comprender el significado **geométrico** y **algebraico** de un determinante.
- Calcular determinantes de matrices $2\times 2$, $3\times 3$ y superiores.
- Aplicar propiedades: expansión por cofactores, efectos del intercambio de filas y factorización.
- Relacionar el determinante con invertibilidad, volumen, orientación y sistemas lineales.
- Resolver sistemas mediante la **regla de Cramer** cuando sea aplicable.

---

## 🧩 Contenidos del capítulo

### 🟦 1. Concepto de determinante

Introduce la idea del determinante, su motivación geométrica y su interpretación algebraica.  
Incluye ejemplos visuales en 2D y 3D para comprender el escalamiento de área y volumen.

---

### 🟩 2. Cálculo de determinantes

Aprenderás a calcular determinantes mediante fórmulas cerradas $2\times2$ y $3\times3$, expansión por cofactores y propiedades del determinante, con implementaciones en Python.

---

### 🟥 3. Regla de Cramer

Explica la regla de Cramer como método directo para solucionar sistemas lineales:

$$A\mathbf{x}=\mathbf{b},\quad \det(A)\neq 0$$

Incluye ejemplos numéricos y simbólicos, interpretaciones geométricas y comparación con otros métodos.

---

## 🧮 Competencias que desarrollarás

| Competencia | Descripción |
|:---|:---|
| **C1. Cálculo matricial** | Computar determinantes en distintas dimensiones. |
| **C2. Razonamiento geométrico** | Comprender escalamiento y orientación. |
| **C3. Resolución de sistemas** | Aplicar la regla de Cramer de forma apropiada. |
| **C4. Pensamiento computacional** | Implementar determinantes y Cramer en Python. |
| **C5. Análisis teórico** | Usar propiedades profundas del determinante. |

---

## 💬 Reflexión inicial

El determinante no es solo una fórmula:  
es una herramienta que revela si una transformación deforma, aplasta, rota o invierte el espacio.

> "El determinante mide cómo una transformación lineal cambia el espacio por dentro."

---

## 🧩 Sugerencia para el estudiante

> - Empieza por el significado geométrico antes de aprender fórmulas.
> - Comprueba con Python tus cálculos a mano usando `np.linalg.det()`.
> - Recuerda: $\det(A) = 0$ significa que la transformación colapsa el espacio.
