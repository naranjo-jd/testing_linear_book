# 📘 Capítulo 8: Autovalores y Autovectores

Los **autovalores y autovectores** son quizás los conceptos más importantes y poderosos de toda el álgebra lineal. Son las "direcciones especiales" de una transformación, aquellas que no cambian de dirección al ser transformadas, solo se escalan.  
Aparecen en física, ingeniería, ciencias de datos, teoría de grafos, procesamiento de señales, y en la base de algoritmos como PageRank y PCA.

---

## 🎯 Objetivo del capítulo

Comprender el significado geométrico y algebraico de los autovalores y autovectores, aprender a calcularlos mediante el polinomio característico, y aplicar la diagonalización para simplificar potencias de matrices y analizar sistemas dinámicos.

---

## 🔍 Contenidos

### 🟦 1. Concepto de autovalores y autovectores
Definición: $A\mathbf{v} = \lambda\mathbf{v}$ donde $\lambda$ es autovalor y $\mathbf{v}$ es autovector.  
Interpretación geométrica: los autovectores son las direcciones que la transformación no rota (solo escala).  
Polinomio característico: $\det(A - \lambda I) = 0$.  
Diagonalización: $A = PDP^{-1}$ cuando existe una base de autovectores linealmente independientes.  
Implementación en Python con `np.linalg.eig()`.

---

### 🟩 2. Ejemplos de autovalores y autovectores
Cuatro ejemplos detallados:
- Matriz $2\times 2$ con autovalores reales distintos
- Matriz $3\times 3$ paso a paso
- Matriz simétrica (siempre diagonalizable, autovectores ortogonales)
- Aplicación: cadenas de Markov o introducción a PCA

---

## 💬 Reflexión final

Los autovectores son las "identidades" de una transformación lineal: las direcciones que persisten a pesar de la transformación. Encontrarlos es revelar la estructura más profunda de una matriz.

> "Los autovectores son los ejes naturales del universo de una transformación. Todo lo demás gira alrededor de ellos."

---

## 🧩 Sugerencia para el estudiante

> - Visualiza primero: los autovectores son vectores que no rotan, solo se estiran o comprimen.
> - El polinomio característico conecta el álgebra con el análisis.
> - La diagonalización $A = PDP^{-1}$ es el resultado más poderoso del capítulo.
