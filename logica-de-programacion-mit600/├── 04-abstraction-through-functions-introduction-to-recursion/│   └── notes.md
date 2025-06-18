## 1. Contexto y motivación

* **Lenguaje Turing-completo:** Con los elementos básicos (asignación, condicionales, entrada/salida y bucles) ya se dispone de un lenguaje capaz de expresar cualquier algoritmo, aunque no necesariamente de forma legible ni mantenible.
* **Necesidad de ampliación:** Para resolver problemas reales de gran envergadura (miles o millones de líneas), se requiere añadir mecanismos de **decomposición** y **abstracción** que faciliten la organización del código y oculten detalles innecesarios.

---

## 2. Decomposición y abstracción mediante funciones

1. **Decomposición**

   * Consiste en dividir el programa en módulos independientes (funciones) que realicen tareas específicas.
   * Cada función actúa como un “ladrillo” reutilizable, aislando lógica y reduciendo duplicación de código.
2. **Abstracción**

   * Permite ocultar la implementación interna: el usuario de la función sólo necesita conocer su nombre, parámetros y valor de retorno.
   * Se apoya en la especificación (o contrato) de la función, escrita como docstring, que describe claramente comportamientos esperados e invariantes.

---

## 3. Sintaxis y semántica de funciones en Python

* **Definición**

  ```python
  def nombre_función(parámetros):
      """Docstring: descripción y contrato de la función."""
      cuerpo_de_la_función
      return valor
  ```

  * `def`: palabra clave para declarar una función.
  * `nombre_función`: identificador sensible a mayúsculas/minúsculas.
  * `(parámetros)`: lista de variables formales (puede estar vacía).
  * `return`: finaliza la ejecución de la función y envía un valor al entorno llamador.
  * Ausencia de `return` equivale a `return None`.
* **Ámbito de variables**

  * **Locales:** parámetros y variables declaradas dentro de la función no afectan al espacio global.
  * **Globales:** permanecen inalteradas tras la ejecución de la función.

---

## 4. Ejemplos de aplicación de funciones

### 4.1. Cálculo de raíces cuadradas (función `sqrt`)

* Se encapsula el algoritmo de aproximación en una función, evitando replicar el mismo bloque de código varias veces.
* Uso de `return` para devolver tanto el resultado como un valor especial `None` cuando la entrada no es válida.

### 4.2. Problema de granja (función `solve`)

* **Primer caso (cerdos y pollos):**

  1. Parámetros: número de cabezas y patas.
  2. Bucle `for` para “enumerar y comprobar” cada posible combinación.
  3. Retorno de la solución en forma de tupla `(cerdos, pollos)` o `(None, None)` si no hay solución.
* **Extensión (función `solve1`):**

  * Agrega un tercer animal (arañas), introduce bucles anidados para explorar más variables manteniendo la misma lógica modular.

---

## 5. Recursión como herramienta de descomposición

1. **Concepto**

   * Resolver un problema reduciéndolo a instancias más pequeñas de sí mismo más una o varias operaciones auxiliares.
   * Requiere un **caso base** (instancia trivial) y un **paso recursivo** que acorte el problema.
2. **Ejemplo de palíndromo (`isPalindrome`)**

   ```python
   def isPalindrome(s):
       if len(s) <= 1:
           return True
       if s[0] != s[-1]:
           return False
       return isPalindrome(s[1:-1])
   ```

   * **Caso base:** cadenas de longitud 0 o 1.
   * **Paso recursivo:** comparar primer y último carácter, y verificar recursivamente la subcadena intermedia.
3. **Ejemplo de números de Fibonacci (`fib`)**

   ```python
   def fib(n):
       if n <= 1:
           return 1
       return fib(n-1) + fib(n-2)
   ```

   * Define el enésimo número de Fibonacci como suma de los dos anteriores.
   * Ilustra la recursión múltiple, donde cada llamada genera dos subproblemas.

---

## 6. Conclusiones y buenas prácticas

* **Modularidad:** Fomenta la reutilización, la legibilidad y facilita las pruebas unitarias.
* **Especificación clara:** Incluye docstrings informativos que indiquen parámetros, valor devuelto y posibles excepciones.
* **Disciplina de retornos:** Todo camino de ejecución debería terminar en un `return`, evitando comportamientos indefinidos.
* **Elegir entre iteración y recursión:**

  * Problemas naturalmente secuenciales o de búsqueda exhaustiva suelen implementarse con bucles.
  * Problemas definidos de manera inductiva (estructuras de datos anidadas, definiciones recursivas) resultan más elegantes en recursión.