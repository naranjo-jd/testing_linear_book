# 🧮 Capítulo: Matrices y Sistemas de Ecuaciones

En este capítulo exploraremos uno de los pilares del álgebra lineal: las **matrices**.  
Aprenderás qué son, cómo se construyen, cómo operan y cómo se relacionan con los **sistemas de ecuaciones lineales**.  

Además, verás cómo las matrices sirven como herramientas para representar transformaciones, resolver ecuaciones, y modelar fenómenos físicos, computacionales y de datos.

---

## 🎯 Objetivo general

Comprender las propiedades y operaciones fundamentales de las **matrices cuadradas** y su aplicación en la resolución de **sistemas lineales**, tanto homogéneos como no homogéneos, usando métodos algebraicos y computacionales.

---

## 🧭 Motivación

Las matrices permiten **organizar y operar con datos numéricos** de forma estructurada.  
En el álgebra lineal, cada matriz puede interpretarse como una **función lineal** que transforma vectores en otros vectores.  

Por ejemplo:
- Una matriz puede **rotar** o **escalar** un objeto en el plano o el espacio.  
- También puede representar un **sistema de ecuaciones lineales**.  
- En computación, las matrices son la base para el **aprendizaje automático**, la **gráfica por computadora** y la **simulación física**.

---

## 🧩 Contenidos del capítulo

Este capítulo está dividido en siete secciones progresivas, cada una enfocada en un aspecto esencial del trabajo con matrices.

---

### 🔹 1. Matrices $2 \times 2$

📘 Archivo: `matrices/matrices_2x2.ipynb`

> Introduce la estructura y operaciones básicas de las matrices cuadradas pequeñas.  
> Se presentan ejemplos geométricos en $\mathbb{R}^2$ y se estudian propiedades como determinante, traza y multiplicación.

---

### 🔹 2. Matrices $3 \times 3$

📘 Archivo: `matrices/matrices_3x3.ipynb`

> Amplía los conceptos a matrices tridimensionales, explorando su interpretación geométrica como **transformaciones en $\mathbb{R}^3$** y su relación con el producto cruz.

---

### 🔹 3. Matrices $n \times n$

📘 Archivo: `matrices/matrices_nxn.ipynb`

> Generaliza los conceptos para matrices de cualquier tamaño.  
> Se estudian operaciones, propiedades estructurales (identidad, triangularidad, simetría) y se introduce la noción de **determinante general**.

---

### 🔹 4. Aplicaciones de las matrices

📘 Archivo: `matrices/aplicaciones.ipynb`

> Muestra cómo las matrices se utilizan en **transformaciones lineales**, **geometría**, **gráficos 3D**, **redes neuronales** y **sistemas dinámicos**.  
> Incluye ejemplos de programación con Python y NumPy.

---

### 🔹 5. Sistemas homogéneos

📘 Archivo: `matrices/sistemas_homogeneos.ipynb`

> Estudia los sistemas de ecuaciones lineales de la forma $A\mathbf{x} = \mathbf{0}$ y su conexión con los **subespacios nulos (núcleo)** de una matriz.  
> Verás cómo resolverlos simbólica y computacionalmente.

---

### 🔹 6. Sistemas no homogéneos

📘 Archivo: `matrices/sistemas_no_homogeneos.ipynb`

> Se abordan los sistemas $A\mathbf{x} = \mathbf{b}$ con $\mathbf{b} \neq \mathbf{0}$ y los criterios de **existencia y unicidad** de soluciones.  
> Incluye métodos computacionales de resolución (reducción gaussiana, factorización LU).

---

### 🔹 7. Inversa y transpuesta

📘 Archivo: `matrices/inversa_transpuesta.ipynb`

> Se estudian dos operaciones fundamentales:
> - La **transpuesta**, que intercambia filas y columnas.  
> - La **inversa**, que invierte el efecto de una transformación lineal.  
>
> Además, se implementan algoritmos para calcularlas con Python y se analizan sus aplicaciones.

---

## 🧮 Competencias que desarrollarás

| Competencia | Descripción |
|:-------------|:-------------|
| **C1. Razonamiento algebraico** | Comprender la estructura y propiedades de las matrices. |
| **C2. Resolución de problemas** | Aplicar técnicas matriciales para resolver sistemas de ecuaciones. |
| **C3. Visualización geométrica** | Interpretar matrices como transformaciones lineales en el plano y el espacio. |
| **C4. Pensamiento computacional** | Implementar operaciones matriciales en Python usando NumPy. |

---

## 🧠 Conexión con capítulos anteriores

| Desde $\mathbb{R}^3$ | Hacia el estudio de matrices |
|:---------------------|:-----------------------------|
| Vectores y subespacios | Columnas de una matriz como vectores que generan subespacios |
| Combinaciones lineales | Representadas como multiplicación matriz–vector |
| Subespacios y núcleos | Interpretados como soluciones de sistemas lineales homogéneos |

> 💬 En este capítulo, los vectores dejan de actuar solos: las **matrices** serán el lenguaje con el que describimos cómo se combinan, transforman y relacionan entre sí.

---

## 💻 Herramientas computacionales

Durante este capítulo trabajaremos con:
- **NumPy** para operaciones matriciales.  
- **SymPy** para cálculos simbólicos (determinantes, inversas, rangos).  
- **Matplotlib** y **Plotly** para representar transformaciones geométricas.

---

## 🚀 Reflexión final

El estudio de las matrices es el puente entre la **geometría** y el **álgebra computacional**.  
A través de ellas, podrás resolver problemas de múltiples dimensiones, entender la estructura de los sistemas lineales y visualizar transformaciones complejas.

> “Las matrices son el lenguaje que traduce las relaciones lineales en operaciones numéricas y visuales.”

---

✅ **Próximo paso:**  
Comienza con la lección [**Matrices $2 \times 2$**](matrices_2x2.ipynb), donde aprenderás las operaciones básicas y su interpretación geométrica en el plano.
