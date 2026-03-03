# 📘 Capítulo: Espacio Fila, Espacio Columna y Dimensión

En este capítulo profundizaremos en la estructura interna de una matriz desde la perspectiva del álgebra lineal: **sus espacios fundamentales**.  
Veremos cómo las filas y columnas de una matriz no son solo números: forman **subespacios** que revelan información esencial sobre la matriz, sus transformaciones y los sistemas lineales asociados.

---

## 🎯 ¿Qué estudiaremos?

Este capítulo aborda tres conceptos clave:

---

### 🔹 1. Espacio fila
El **espacio fila** de una matriz es el subespacio generado por sus filas.  
Nos dice:

- qué combinaciones lineales pueden obtenerse a partir de las filas,
- cómo afectan los pivotes y la reducción por filas,
- cómo se relaciona con soluciones de sistemas lineales.

📘 Archivo: `espacio_fila_columna/espacio_fila.ipynb`

---

### 🔹 2. Espacio columna
El **espacio columna** es el conjunto de todas las combinaciones lineales de las columnas.  
Este subespacio corresponde al:

- **rango** de la matriz,
- imagen de la transformación lineal asociada,
- conjunto de vectores alcanzables por \(Ax\).

📘 Archivo: `espacio_fila_columna/espacio_columna.ipynb`

---

### 🔹 3. Dimensión
La **dimensión** es la cantidad mínima de vectores que generan un espacio vectorial.  
Analizaremos:

- dimensión del espacio fila y columna,
- relación fundamental:
  \[
  \dim(\text{espacio fila}) = \dim(\text{espacio columna}) = \text{rango}(A),
  \]
- conexión con sistemas homogéneos y el núcleo,
- métodos computacionales para calcular dimensión.

📘 Archivo: `espacio_fila_columna/dimension.ipynb`

---

## 🧠 ¿Por qué es importante este capítulo?

Los conceptos de fila, columna y dimensión están en el centro del álgebra lineal:

- Determinan el **rango** de una matriz  
- Explican cuándo un sistema tiene solución o no  
- Determinan si una transformación lineal "aprovecha" todo el espacio  
- Revelan estructura oculta en datos (PCA, compresión, machine learning)  
- Permiten entender la independencia lineal y subespacios en profundidad  

De hecho, el **rango** es uno de los invariantes más importantes en toda la teoría.

---

## 🧮 Enfoque del capítulo

Cada sección combina:

- definiciones formales,  
- interpretación geométrica,  
- ejemplos concretos,  
- visualizaciones 2D/3D,
- implementaciones computacionales con **NumPy** y **SymPy**,  
- ejercicios propuestos para consolidar aprendizaje.

Buscamos que entiendas **qué significan** estos espacios y también cómo **calcularlos** en la práctica.

---

## 🧬 Conexión con capítulos anteriores

| Capítulo anterior | Relación |
|------------------|----------|
| Matrices | Espacios fila y columna dependen de la estructura interna de A |
| Subespacios | Fila y columna son subespacios reales con bases propias |
| Determinantes | Rango y determinante están conectados mediante la dimensión |
| Sistemas lineales | El espacio columna determina si Ax=b tiene solución |

---

## 🚀 ¿Qué aprenderás al finalizar?

Serás capaz de:

- Determinar bases para el espacio fila y columna  
- Calcular la dimensión (rango) de una matriz  
- Relacionar espacio columna con existencia de soluciones  
- Interpretar geométricamente la imagen y el rango  
- Implementar en Python herramientas para calcular estos espacios  

---

## 📂 Navegación del capítulo

1. 👉 `espacio_fila.ipynb` — ¿Qué es el espacio fila?  
2. 👉 `espacio_columna.ipynb` — Imagen de una matriz  
3. 👉 `dimension.ipynb` — Rango, dimensión y teorema rango–nulidad  

Prepárate para ver a las matrices desde una perspectiva mucho más profunda.

---

> **“El espacio columna nos dice adónde puede llegar una matriz.  
> El espacio fila nos dice cómo se combinan sus ecuaciones.  
> La dimensión nos dice cuánta información contiene.”**

