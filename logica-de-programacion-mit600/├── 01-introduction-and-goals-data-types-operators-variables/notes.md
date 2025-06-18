### 1. Objetivos de aprendizaje

1. **Estratégicos (visión amplia)**

   * Facilitar la entrada a Course 6 a novatos en código.
   * Dar confianza a estudiantes de otras carreras para leer/escribir pequeños programas.
   * Comprender **qué puede y qué no puede** resolver la computación.
   * Aumentar la empleabilidad (prácticas y trabajos técnicos).

2. **Tácticos (competencias concretas)**

   * Usar las herramientas del *pensamiento computacional* para crear programas sencillos.
   * Leer y auditar código de terceros.
   * Conocer capacidades, límites y costes de los algoritmos.
   * Traducir problemas científicos a formulaciones programables.



### 2. Pensamiento computacional

| Concepto                     | Explicación                                                                                               |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Declarativo**              | Saber *qué* es algo (p. ej. √x es y tal que y² = x).                                                      |
| **Imperativo**               | Saber *cómo* obtenerlo (método de Herón para √x).                                                         |
| **Programa = receta**        | Secuencia de pasos + flujo de control.                                                                    |
| **Historia**                 | De máquinas de “programa fijo” (calculadora, *bombe* de Turing) a **programa almacenado** con intérprete. |
| **Teorema de Turing (1936)** | Con seis primitivas se puede programar todo lo computable → cualquier lenguaje ‘completo’ es equivalente. |



### 3. Lenguajes de programación – Clasificación rápida

1. **Alto vs. Bajo nivel**

   * Bajo: cerca del hardware (ensamblador).
   * Alto: primitivas ricas y abstracciones (Python).

2. **General vs. Específico**

   * General: C, Python.
   * Dirigido a dominio: MATLAB (álgebra lineal), SQL (consultas).

3. **Interpretado vs. Compilado**

   * Interpretado: ejecución directa del código fuente (Python).
   * Compilado: traducción previa a objeto máquina (C, Rust).

*Python* ➜ alto nivel, general, interpretado.



### 4. Sintaxis y semántica en programación

| Capa                   | Qué valida                                                     | Cuándo se detecta                   |
| ---------------------- | -------------------------------------------------------------- | ----------------------------------- |
| **Sintaxis**           | “Gramática” correcta                                           | Al compilar/interpretar             |
| **Semántica estática** | Tipos y estructuras coherentes                                 | A veces antes, a veces en ejecución |
| **Semántica plena**    | Conducta real al correr (resultados, bucles infinitos, fallos) | Solo en ejecución                   |

> **Estilo limpio + pruebas** = única defensa total contra errores semánticos que pasan los chequeos.



### 5. Primeros cimientos de Python vistos en clase

| Tema                         | Ejemplo                                                | Nota                                              |
| ---------------------------- | ------------------------------------------------------ | ------------------------------------------------- |
| **Tipos primitivos**         | `5` (int), `3.14` (float), `"hola"` (str)              | Diferenciar `"52"` de `52`.                       |
| **Operadores numéricos**     | `+  -  *  /  **  //  %`                                | `3/5 → 0` (int) vs. `3/5.0 → 0.6`.                |
| **Operadores sobre cadenas** | `"ha"*3 → "hahaha"`<br>`"foo"+"bar" → "foobar"`        | Python sobrecarga `*` y `+` con sentido distinto. |
| **Asignación**               | `nombre = "Eric"`                                      | “nombre” queda vinculado al valor `"Eric"`.       |
| **Errores ilustrados**       | Sintaxis: `52A` (sin comillas).<br>Tipo: `"52" * "7"`. | Python reporta y señala la línea.                 |



### 6. Idea central para llevarte

> **Aprender a programar = aprender a redactar recetas de solución.**
> Python es solo el lápiz; la destreza que cuenta es **pensar como científic@ computacional**, capaz de descomponer problemas, diseñar algoritmos y comprender sus límites.