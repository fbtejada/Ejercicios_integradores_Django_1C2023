# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

def get_int():
    """Recursivo"""

    cadena=input("Ingrese un entero:")
    try:
        return int(cadena)
    except ValueError:
        return get_int()    # Denuevo si no pudo convertirlo en entero


def get_int_iter():
    """Iterativo"""

    while True:
        cadena=input("Ingrese un entero:")
        try:
            return int(cadena)
        except ValueError:
            pass    # Denuevo si no pudo convertirlo en entero

print("Recursivo.")
print(get_int())

print("Iterativo")
print(get_int_iter())
