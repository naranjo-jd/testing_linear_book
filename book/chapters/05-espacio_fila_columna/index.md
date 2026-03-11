# 📘 Capítulo 5: Espacio Fila, Espacio Columna y Dimensión

En este capítulo profundizaremos en la estructura interna de una matriz: **sus espacios fundamentales**.  
Las filas y columnas de una matriz forman **subespacios** que revelan información esencial sobre la matriz, sus transformaciones y los sistemas lineales asociados.

---

## 🎯 ¿Qué estudiaremos?

---

### 🟦 1. Espacio fila

El **espacio fila** de una matriz es el subespacio generado por sus filas.  
Nos dice qué combinaciones lineales pueden obtenerse a partir de las filas, cómo afectan los pivotes y la reducción por filas, y cómo se relaciona con soluciones de sistemas lineales.

---

### 🟩 2. Espacio columna

El **espacio columna** es el conjunto de todas las combinaciones lineales de las columnas.  
Corresponde al **rango** de la matriz, la imagen de la transformación lineal asociada y el conjunto de vectores alcanzables por $A\mathbf{x}$.

---

### 🟥 3. Dimensión y rango

La **dimensión** es la cantidad mínima de vectores que generan un espacio vectorial.  
Analizaremos la relación fundamental:

$$\dim(\text{espacio fila}) = \dim(\text{espacio columna}) = \text{rango}(A)$$

y la conexión con sistemas homogéneos y el núcleo mediante el teorema rango–nulidad.

---

## 🧠 ¿Por qué es importante este capítulo?

- Determinan el **rango** de una matriz.
- Explican cuándo un sistema tiene solución o no.
- Revelan estructura oculta en datos (PCA, compresión, machine learning).
- Permiten entender la independencia lineal y subespacios en profundidad.

---

## 🧮 Competencias que desarrollarás

| Competencia | Descripción |
|:---|:---|
| **C1. Espacios fundamentales** | Determinar bases para el espacio fila y columna. |
| **C2. Dimensión y rango** | Calcular la dimensión de un subespacio matricial. |
| **C3. Existencia de soluciones** | Relacionar el espacio columna con la consistencia de $A\mathbf{x}=\mathbf{b}$. |
| **C4. Pensamiento computacional** | Implementar en Python herramientas para calcular estos espacios. |

---

## 💬 Reflexión final

> "El espacio columna nos dice adónde puede llegar una matriz.  
> El espacio fila nos dice cómo se combinan sus ecuaciones.  
> La dimensión nos dice cuánta información contiene."

---

## 🧩 Sugerencia para el estudiante

> - Relaciona el espacio columna con la imagen de una transformación lineal.
> - Usa la forma escalonada reducida para encontrar bases de estos espacios.
> - Aplica el teorema rango–nulidad para verificar tus resultados.
