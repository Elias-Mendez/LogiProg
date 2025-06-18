# ——— Expresiones básicas en el intérprete ———

# Suma de enteros
3 + 4
# → 7

# Concatenación de cadenas y réplica
"hola" * 3
# → "holaholahola"

"hola" + " mundo"
# → "hola mundo"



# ——— Conversión de tipos ———

# Para concatenar un número con una cadena hay que convertirlo explícitamente:
str(3) + " tres"
# → "3 tres"




# ——— Asignación de variables ———

# Evaluar la expresión del lado derecho y enlazarla al nombre
x = 3
y = x * x
print(y)
# → 9




# ——— Lectura de entrada por teclado ———

# (en Python 2)
entrada = input("Introduce un número: ")
print(entrada)






# ——— Condicional simple (par/impar) ———

x = 15
if x // 2 * 2 == x:
    print("par")
else:
    print("impar")





# ——— If sin else ———

x = "c"
b = "b"
if x < b:
    print("x precede a b")
# (no hay else: si la condición es falsa, no ocurre nada)






# ——— If con distinta indentación ———

x = "c"
b = "b"
if x < b:
    print("x precede a b")
print("Mon")
# Aquí, el segundo print siempre se ejecuta porque está al mismo nivel que el if.





# ——— If anidado: hallar el menor de tres valores ———

x, y, z = 10, 5, 8
if x < y:
    if x < z:
        print("x es el menor")
    else:
        print("z es el menor")
else:
    print("y es el menor")





# ——— Bucle while: acumulación (a modo de “potencia entera”) ———

x = 3
y = 0
iters_left = 3

while iters_left > 0:
    y = y + x
    iters_left = iters_left - 1

print(y)
# → 9  (equivale a x * 3)