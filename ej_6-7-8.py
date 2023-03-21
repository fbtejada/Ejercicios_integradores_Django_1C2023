# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise ValueError("El nombre debe ser una String")

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
        else:
            raise ValueError("La edad debe ser un entero no negativo")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str)  and dni.isnumeric() and len(dni) >= 6:
            self.__dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de texto de 6 dígitos o más")

    def mostrar(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}")

    def es_mayor_de_edad(self):
        return self.__edad >= 18
    

print("\nPrueba clase Persona")
persona1 = Persona()
persona1.nombre='Federico'
persona1.edad=52
persona1.dni='123456'
persona1.mostrar()
print(persona1.es_mayor_de_edad())

# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.

class Cuenta:
    
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    @property
    def titular(self):
        return self.__titular

    @titular.setter    
    def titular(self, titular):
        self.__titular = titular
        
    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular.nombre}, Cantidad: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad

print("\nPrueba clase Cuenta")
cuenta1 = Cuenta(persona1,1000)
cuenta1.mostrar()

cuenta1.ingresar(100)
cuenta1.mostrar()

cuenta1.retirar(10)
cuenta1.mostrar()


# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.

class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property    
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
       
    def es_titular_valido(self):
        return self.titular().es_mayor_de_edad() and self.titular().edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Titular inválido. No puede retirar.")
    
    def mostrar(self):
        print(f"Cuenta Joven. Bonificación: {self.__bonificacion}%")


print("\nPrueba clase Cuenta Joven")
cuenta_joven1 = CuentaJoven(persona1,1000,10)
cuenta_joven1.mostrar()