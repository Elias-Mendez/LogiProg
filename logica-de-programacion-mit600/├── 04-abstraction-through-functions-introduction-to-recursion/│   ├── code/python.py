# Ejemplo 1: Función para calcular raíces cuadradas de enteros (números perfectos)
def sqrt(x):
    if x < 0:
        print("No es un cuadrado perfecto")
        return None
    ans = 0
    while ans * ans < x:
        ans += 1
    if ans * ans == x:
        return ans
    else:
        print("No es un cuadrado perfecto")
        return None

# Ejemplo 2: Resolución del problema de cerdos y pollos
def solve(legs, heads):
    for chickens in range(heads + 1):
        pigs = heads - chickens
        if 4*pigs + 2*chickens == legs:
            return pigs, chickens
    return None, None

def Barnyard():
    legs = int(input("Número de patas: "))
    heads = int(input("Número de cabezas: "))
    pigs, chickens = solve(legs, heads)
    if pigs is None:
        print("No hay solución")
    else:
        print(f"Cerdos: {pigs}, Pollos: {chickens}")

# Ejemplo 3: Extensión con arañas (problema subdeterminado)
def solve1(legs, heads):
    for spiders in range(heads + 1):
        for chickens in range(heads - spiders + 1):
            pigs = heads - spiders - chickens
            if spiders*8 + chickens*2 + pigs*4 == legs:
                return pigs, chickens, spiders
    return None, None, None

def Barnyard1():
    heads = int(input("Número de cabezas: "))
    legs = int(input("Número de patas: "))
    pigs, chickens, spiders = solve1(legs, heads)
    if pigs is None:
        print("No hay solución")
    else:
        print(f"Cerdos: {pigs}, Pollos: {chickens}, Arañas: {spiders}")

# Ejemplo 4: Detección de palíndromo (recursión)
def isPalindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])

# Ejemplo 5: Cálculo recursivo de la serie de Fibonacci
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)
