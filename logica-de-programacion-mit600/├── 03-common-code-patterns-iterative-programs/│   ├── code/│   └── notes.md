## 1. Elementos básicos de la programación

1. **Tipos de datos fundamentales**

   * **Números** (enteros, reales)
   * **Cadenas de texto** (strings)
   * **Booleanos** (valores `True`/`False`, usados en condiciones)
2. **Operaciones asociadas**

   * Aritméticas: suma, resta, multiplicación, división, etc.
   * Sobre cadenas: concatenación (`+`), repetición (`*`).
   * Lógicas: `and`, `or`, `not` sobre booleanos.
3. **Comandos o sentencias**

   * **Asignación**: vincular un nombre a un valor (`x = 5`).
   * **Entrada/Salida**: `print()` para mostrar resultados, `input()` para leer datos.
   * **Estructuras de control**:

     * **Condicionales** (`if`/`else`) para ramificar flujo.
     * **Bucles** (`while`, `for`) para repetición de bloques de código.

---

## 2. Buenas prácticas de programación (“higiene” y “estilo”)

1. **Comentarios claros**: explicar el propósito de fragmentos de código.
2. **Disciplina de tipos**: verificar que los datos sean del tipo esperado antes de operar.
3. **Nombres descriptivos**: variables y funciones con nombres autoexplicativos.
4. **Pruebas exhaustivas**: testar todas las ramas del código (todas las condiciones posibles).
5. **Programación defensiva**:

   * Validar entradas del usuario (ej. números positivos).
   * Controlar errores internos (asumir que otras partes del programa pueden fallar).
   * Proporcionar mensajes útiles cuando algo no cumple los requisitos.

---

## 3. Programación iterativa

Se describen cinco pasos para diseñar un bucle de tipo **“while”**:

1. **Elegir la variable contadora** (“qué cambia en cada iteración”).
2. **Inicializarla fuera del bucle** (valor inicial).
3. **Definir el test de fin** (condición que detiene el bucle).
4. **Construir el bloque de código** que se repetirá (asegurándose de actualizar la variable).
5. **Acción al terminar** (por ejemplo, imprimir o devolver un resultado).

**Ejemplo:**

* Encontrar la raíz cuadrada de un entero perfecto haciendo una búsqueda lineal:

  ```python
  ans = 0
  while ans * ans < x:
      ans += 1
  print(ans)
  ```

---

## 4. Diagramas de flujo y simulación manual

1. **Diagramas de flujo**:

   * **Óvalos**: inicio y fin.
   * **Rectángulos**: asignaciones y operaciones.
   * **Diamantes**: pruebas condicionales.
   * **Trapecios**: entrada/salida.
2. **Simulación a mano**:

   * Seguir paso a paso valores de variables para verificar terminación y corrección (debugging sin ejecutar el código).

---

## 5. Análisis de complejidad

* **Programas de ramificación simple**: cada instrucción se ejecuta a lo sumo una vez ⇒ **complejidad constante** (O(1)).
* **Bucles dependientes de la entrada**: número de iteraciones crece con el tamaño de los datos ⇒ **complejidad lineal** (O(n)).
* Ejemplo: búsqueda de raíz cuadrada por incremento es O(√x).

---

## 6. Bucles “for” y colecciones

1. **Bucles `for`**

   * Recorren automáticamente cada elemento de una colección finita (listas, rangos, tuplas, cadenas).
   * Evitan inicializar y actualizar manualmente la variable contadora.
2. **Estructuras de datos compuestas**

   * **Tuplas**: secuencias ordenadas e inmutables (`(a, b, c)`).
   * **Listas** (similares a tuplas pero mutables): se definen con corchetes `[1, 2, 3]`.
   * **Slicing** (rebanado): `tupla[1:3]` devuelve los elementos en índices 1 y 2.
   * **Concatenación**: `tupla + (nuevo_elemento,)` o `lista + [nuevo_elemento]`.
3. **Ejemplos de uso**

   * **Divisores de un entero**:

     ```python
     divisores = ()
     for i in range(1, x):
         if x % i == 0:
             divisores += (i,)
     print(divisores)
     ```
   * **Procesamiento de cadenas** (strings como secuencias):

     ```python
     total = 0
     for c in str(número):
         total += int(c)
     print(total)
     ```

---

## 7. Cadenas de texto como colecciones

* Pueden **seleccionarse** (`s[0]`), **rebanarse** (`s[2:5]`) y **concatenarse** (`s1 + s2`).
* Permiten aplicar los mismos patrones de iteración para procesar dígitos, caracteres, palabras, etc.

---

## 8. Computabilidad y completitud de Turing

* Con estas construcciones básicas (asignación, condicionales, bucles y estructuras de datos), **cualquier algoritmo describible** puede implementarse ⇒ Python es **Turing-completo**.
* El reto práctico consiste en **componer** estos elementos para resolver problemas concretos de manera eficiente y mantenible.