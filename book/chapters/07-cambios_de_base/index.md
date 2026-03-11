# 📘 Capítulo 7: Cambios de Base

La misma información puede expresarse de maneras muy diferentes dependiendo del sistema de referencia elegido. Los **cambios de base** nos dan el poder de elegir la representación más conveniente para cada problema, simplificando cálculos y revelando estructuras ocultas.

---

## 🎯 Objetivo del capítulo

Comprender cómo cambian las coordenadas de un vector y la representación matricial de una transformación al cambiar de base, y dominar el uso de la matriz de cambio de base para realizar estas conversiones.

---

## 🔍 Contenidos

### 🟦 1. Concepto de cambio de base
Definición de base, coordenadas relativas a una base, y construcción de la matriz de cambio de base $P$ cuyas columnas son los vectores de la nueva base expresados en coordenadas estándar.  
Se estudian la inversa $P^{-1}$, la conversión de coordenadas $[\mathbf{v}]_\mathcal{B} = P^{-1}\mathbf{v}$, y cómo la representación matricial de una transformación cambia según $A_\mathcal{B} = P^{-1}AP$.

---

### 🟩 2. Ejemplos de cambios de base
Análisis detallado con cuatro ejemplos:
- Cambio de la base estándar a una base rotada en $\mathbb{R}^2$
- Cambio de base en $\mathbb{R}^3$
- Misma transformación lineal en dos bases diferentes
- Anticipación de diagonalización (base de autovectores)

---

## 💬 Reflexión final

El cambio de base es como cambiar el idioma en que describes el mismo objeto. El objeto no cambia — solo cambia cómo lo describes. Elegir la base adecuada puede convertir un problema difícil en uno trivial.

> "La base que eliges determina cómo ves el mundo. Elige sabiamente."

---

## 🧩 Sugerencia para el estudiante

> - Piensa en las columnas de $P$ como los nuevos "ejes" expresados en coordenadas estándar.
> - La inversión $P^{-1}$ te dice cómo traducir de coordenadas estándar a las nuevas.
> - Practica con bases ortogonales primero — son las más intuitivas.
