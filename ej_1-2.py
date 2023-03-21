# 1. Escribir una función que calcule el máximo común divisor entre dos números.
def gcd(a, b):
    """
    El maximo comun divisor entre dos números enteros es el entero mas grande que divide a ambos.
    Aquí más grande es en ambos sentidos, el del orden aritmético común y el del ordende la divisibilidad.
    Utilizamos el algoritmo de Euclides que dice que gcd(a,b)=gcd(r,b) donde r es el resto de dividir a por b
    de acuerdo con el algoritmo de división.
    Puede demostrarse facilmente utilizando el algoritmo de división y propiedades elementales de la divisibilidad.
    """
    if b == 0:
        return a
    return gcd(b, a % b)

# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números


def lcm(a, b):
    """
    El mínimo comun múltiplo de dos números enteros puede calcularse a partir del máximo común divisor
    teniendo en cuenta que a*b=gcd(a,b)*lcm(a,b) lo que es obvio del teorema de factorización única.
    """
    return (a * b) // gcd(a, b)


print("gcd's")
print(gcd(30, 25))
print(gcd(31, 25))

print("")

print("lcm's")
print(lcm(30, 25))
print(lcm(31, 25))
