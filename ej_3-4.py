# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

cadena=input("Ingrese su cadena:")
lista=[]
lista=cadena.split()
frecuencias=[lista.count(palabra) for palabra in lista]
print(dict(zip(lista,frecuencias)))



# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.

def dict_frecuencias(cadena):
    """
    Recibe una cadena de caracteres y devuelve un diccionario con cada
    palabra que contiene y la cantidad de veces que aparece (frecuencia)
    """
    lista=[]
    lista=cadena.split()
    frecuencias=[lista.count(palabra) for palabra in lista]
    return dict(zip(lista,frecuencias))

print(dict_frecuencias("cadena cadena de caracteres y devuelve un diccionario con cada palabra que contiene y la cantidad de"))