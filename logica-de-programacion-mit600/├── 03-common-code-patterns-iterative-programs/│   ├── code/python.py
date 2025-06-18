# 1. Búsqueda de la raíz cuadrada de un entero perfecto (búsqueda lineal con while)

x = input("enter a perfect square: ")
ans = 0
while ans * ans < x:
    ans += 1
print(ans)





# 2. Versión defensiva (validación de entrada y comprobación de cuadrado perfecto)

if x < 0:
    print("Error: número negativo")
else:
    ans = 0
    while ans * ans < x:
        ans += 1
    if ans * ans != x:
        print("No es un cuadrado perfecto")
    else:
        print(ans)





# 3. Obtención de todos los divisores de un entero (bucle while)

i = 1
while i < x:
    if x % i == 0:
        print(i)
    i += 1




# 4. Recolección de divisores en una tupla (bucle for + concatenación de tuplas)

divisores = ()
for i in range(1, x):
    if x % i == 0:
        divisores += (i,)
print(divisores)






# 5. Suma de los dígitos de un número (iteración sobre la cadena de dígitos)
numero = input("Introduce un número: ")
digits = 0
for c in str(numero):
    digits += int(c)
print(digits)