# 📚 Material de Estudio: Transformaciones Lineales

Esta sección reúne todas las actividades, ejercicios y evaluaciones del Capítulo 6. Sigue el orden propuesto para construir comprensión progresiva: primero la intuición, luego la teoría, y finalmente la práctica computacional.

---

## 🗺️ Mapa de actividades

| # | Actividad | Tipo | Habilidad principal |
|---|-----------|------|---------------------|
| 1 | Actividad de Enganche | Exploratoria | Intuición visual |
| 2 | Quiz de Conceptos | Evaluativa | Comprensión teórica |
| 3 | Ejercicios Computacionales | Práctica | Implementación Python |
| 4 | Ejercicios Teóricos | Práctica | Demostración algebraica |
| 5 | Actividad Computacional | Proyecto | Integración |

---

## 🟦 Actividad 1 — Actividad de Enganche

**Tipo:** Exploratoria — antes de definir formalmente una transformación lineal.

**Descripción:** A través de visualizaciones interactivas, el estudiante escala, rota y deforma figuras geométricas. Observa qué propiedades se conservan (líneas rectas, el origen) y cuáles no (longitud, ángulos). Esta experiencia establece la intuición necesaria para comprender la definición formal.

**Conceptos que activa:**
- Idea intuitiva de "función que transforma vectores"
- Diferencia entre transformaciones lineales y no lineales
- Observación de invariantes geométricas

**Tiempo estimado:** 20–30 minutos

---

## 🟩 Actividad 2 — Quiz de Conceptos

**Tipo:** Evaluativa formativa.

**Descripción:** Cinco preguntas que cubren los conceptos fundamentales del capítulo. Cada pregunta presenta un caso concreto y pide al estudiante razonar sobre linealidad, núcleo, imagen o aplicar el teorema rango-nulidad. Las respuestas están ocultas para permitir el trabajo individual antes de la verificación.

**Conceptos evaluados:**
1. Verificación de linealidad
2. Cálculo del núcleo
3. Determinación de la imagen
4. Aplicación del teorema rango-nulidad
5. Composición de transformaciones

**Tiempo estimado:** 30–40 minutos

---

## 🟨 Actividad 3 — Ejercicios Computacionales

**Tipo:** Práctica con Python.

**Descripción:** Cinco ejercicios de programación con código inicial (*starter code*) que el estudiante completa e interpreta. Se trabaja con NumPy, Matplotlib y en algunos casos SymPy para verificar resultados algebraicos.

**Ejercicios incluidos:**
1. Implementar una función de rotación general $T_\theta$ y probarla
2. Encontrar el núcleo de una matriz $3 \times 3$ usando descomposición SVD
3. Componer dos transformaciones y verificar $(AB)\mathbf{x} = A(B\mathbf{x})$
4. Verificar numéricamente que $f(x,y) = (x+y,\, xy)$ **no** es lineal
5. Construir la matriz de una transformación a partir de su acción sobre la base de $\mathbb{R}^3$

**Tiempo estimado:** 45–60 minutos

---

## 🟥 Actividad 4 — Ejercicios Teóricos

**Tipo:** Práctica de demostración y análisis algebraico (con verificación computacional).

**Descripción:** Cinco ejercicios de estilo lápiz-y-papel donde el estudiante demuestra propiedades, calcula espacios fundamentales y razona sobre inyectividad/suprayectividad. El código Python actúa como verificador de las respuestas analíticas.

**Ejercicios incluidos:**
1. Demostrar que $T(x,y,z) = (x+y,\, y+z,\, x+z)$ es lineal y hallar su matriz
2. Encontrar $\ker(T)$ e $\operatorname{Im}(T)$ de una matriz $3 \times 3$ analíticamente
3. Aplicar el teorema rango-nulidad y verificar $\dim(\ker) + \dim(\operatorname{Im}) = n$
4. Demostrar que la composición de dos transformaciones lineales es lineal
5. Determinar si una transformación es inyectiva, suprayectiva o biyectiva

**Tiempo estimado:** 50–70 minutos

---

## 🟪 Actividad 5 — Actividad Computacional (Proyecto)

**Tipo:** Proyecto integrador.

**Descripción:** Mini-proyecto **Motor de Transformaciones 2D** donde el estudiante construye la clase `TransformadorLineal2D` con métodos para rotar, reflejar y escalar polígonos. Se componen transformaciones, se visualizan los resultados lado a lado y se completa un reto final de animación.

**Habilidades integradas:**
- Programación orientada a objetos en Python
- Multiplicación y composición de matrices de transformación
- Visualización con Matplotlib
- Interpretación geométrica de transformaciones lineales compuestas

**Tiempo estimado:** 60–90 minutos

---

## 📐 Tabla de competencias del capítulo

| Competencia | Actividad que la desarrolla |
|-------------|----------------------------|
| Identificar y verificar linealidad | Enganche, Quiz, Ejercicios Teóricos |
| Construir la matriz de representación | Ejercicios Computacionales, Ejercicios Teóricos |
| Calcular núcleo e imagen | Quiz, Ejercicios Computacionales, Ejercicios Teóricos |
| Aplicar el teorema rango-nulidad | Quiz, Ejercicios Teóricos |
| Clasificar (inyectiva / suprayectiva) | Ejercicios Teóricos, Quiz |
| Componer transformaciones | Ejercicios Computacionales, Actividad Computacional |
| Visualizar transformaciones geométricamente | Enganche, Actividad Computacional |

---

## 💡 Recomendación de estudio

Completa primero la **Actividad de Enganche** sin revisar notas: el objetivo es activar intuición, no obtener respuestas perfectas. Luego estudia la teoría en `teoria/concepto.ipynb` y `teoria/ejemplos.ipynb`, y vuelve al **Quiz** para autoevaluarte. Finalmente, usa los ejercicios y el proyecto para consolidar y aplicar lo aprendido.

