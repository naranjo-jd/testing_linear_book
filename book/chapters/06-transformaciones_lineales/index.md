# 📘 Capítulo 6: Transformaciones Lineales

Las **transformaciones lineales** son el corazón del álgebra lineal: son funciones que respetan la estructura de los espacios vectoriales, preservando sumas y escalamientos. Entenderlas nos permite modelar rotaciones, reflexiones, proyecciones y deformaciones geométricas con una sola multiplicación matricial, unificando geometría y álgebra en un lenguaje poderoso que impregna la física, la computación gráfica, el aprendizaje automático y la ingeniería.

---

## 🎯 Objetivo del capítulo

Al finalizar este capítulo el estudiante será capaz de: identificar y verificar si una función es una transformación lineal, construir su matriz de representación a partir de la acción sobre la base estándar, calcular el núcleo y la imagen, aplicar el teorema rango-nulidad y clasificar la transformación como inyectiva, suprayectiva o biyectiva.

---

## 🔍 Contenidos

### 🟦 1. Concepto de transformación lineal

Una función $T: V \to W$ entre espacios vectoriales es una **transformación lineal** si satisface aditividad ($T(\mathbf{u}+\mathbf{v}) = T(\mathbf{u})+T(\mathbf{v})$) y homogeneidad ($T(c\mathbf{u}) = cT(\mathbf{u})$). Estas dos propiedades se pueden combinar en la condición $T(a\mathbf{u}+b\mathbf{v}) = aT(\mathbf{u})+bT(\mathbf{v})$. Se estudian los ejemplos canónicos (rotación, reflexión, escala, identidad, transformación cero) y el método sistemático para verificar linealidad.

---

### 🟩 2. Ejemplos y representación matricial

Toda transformación lineal $T: \mathbb{R}^n \to \mathbb{R}^m$ se puede representar como una multiplicación matricial $T(\mathbf{x}) = A\mathbf{x}$, donde las columnas de $A$ son las imágenes de los vectores de la base estándar. Se trabajan cuatro ejemplos detallados: rotación en $\mathbb{R}^2$, proyección ortogonal sobre una recta, transformación de cizallamiento (*shear*) y una transformación de $\mathbb{R}^3$ a $\mathbb{R}^2$ que ilustra reducción de dimensión con cálculo explícito de núcleo e imagen.

---

### 🟨 3. Núcleo, imagen y teorema rango-nulidad

El **núcleo** $\ker(T) = \{\mathbf{v} \in V : T(\mathbf{v}) = \mathbf{0}\}$ mide "cuánta información pierde" $T$, mientras que la **imagen** $\operatorname{Im}(T) = \{T(\mathbf{v}) : \mathbf{v} \in V\}$ describe el alcance de $T$. El **teorema rango-nulidad** establece que $\dim(\ker T) + \dim(\operatorname{Im} T) = \dim(V)$, una igualdad de profundo contenido geométrico y algebraico.

---

### 🟥 4. Transformaciones inyectivas, suprayectivas y biyectivas

$T$ es **inyectiva** si y solo si $\ker(T) = \{\mathbf{0}\}$; es **suprayectiva** si y solo si $\operatorname{Im}(T) = W$; y es **biyectiva** (invertible) si es ambas cosas a la vez. En términos matriciales esto se traduce en propiedades del rango y del determinante de la matriz asociada.

---

## 💬 Reflexión final

Las transformaciones lineales son el puente entre la geometría y el álgebra. Cada vez que una imagen se rota en un videojuego, que un modelo de aprendizaje automático ajusta sus pesos o que un ingeniero analiza vibraciones en una estructura, hay una transformación lineal trabajando en silencio. Aprender a leerlas y construirlas es aprender el idioma del álgebra moderna.

> "La geometría es el arte de razonar correctamente sobre figuras incorrectamente dibujadas."
> — Henri Poincaré

---

## 🧩 Sugerencia para el estudiante

> - Antes de memorizar fórmulas, dibuja: transforma un cuadrado unitario con cada transformación canónica y observa qué cambia y qué se conserva.
> - Cuando verifiques linealidad, prueba primero con vectores concretos para ganar intuición; luego haz la prueba algebraica general.
> - Relaciona siempre el núcleo con la "pérdida de información" y la imagen con el "alcance": esto hace que el teorema rango-nulidad sea obvio geométricamente.

