#Funciones
#son bloques de codigo reutilizables que encapsulan tareas especificas y las ejecuta cuando sea necesario. Las funciones organizan nuestro cod, evitan repaticion y los programas se vuelven modulares y faciles de mantener

#definicion y llamada de funciones
#utilizamos la palabra clave def seguida del nombre de la funcion y ():
def saludo():
    print('¡Hola, mundo!')

saludo() #imprime '¡Hola, mundo!'   con el nombre de la funcion la llamamos

#parametros y argumentos
#las funciones pueden aceptar parametros, valores que se pasan a la funcion cuando se la llama. Se especifican dentro de () de la funcion
def saludar(nombre):
    print(f'¡Hola, {nombre}!')

#al llamar a la funcion le proporcionamos los argumentos en los parametros
saludar('Juan') #imprime '¡Hola, Juan!
saludar('Maria') #imprime '¡Hola, Maria!

#valores de retorno
#las funciones pueden devolver valores utilizando la plabara return. El valor de retorno puede ser utilizado por el cod que llama a la funcion
def suma(a, b):
    return a + b
resultado = suma(3, 4)
print(resultado) #imprime 7

#funciones anonimas (lambda)
#son funciones sin nombre definidas en una sola linea. Se utilizan para funciones pequeñas y concisas
cuadrado = lambda x: x ** 2
print(cuadrado(5)) #imprime 25

#alcance de las variables (local vs global)
#las variables definidas dentro de una funcion tienen un alcance local, solo son accesibles dentro de la funcion. Las variables definidas fuera de cualquier funcion tienen un alcance global y pueden ser accedidas desde cualquier parte del programa
def funcion():
    variable_local = 10
    print(variable_local) #accesible dentro de la funcion

variable_global = 20

def funcion2():
    print(variable_global) #accesible desde cualquier lugar

funcion() #imprime 10
funcion2() #imprime 20
print(variable_global) #imprime 20
#print(variable_local) #genera un error, porque no esta definida en este alcance

#funciones definidas por el usuario
def calcular_media(*numeros): #el * indica cualquier cantidad de argumentos posicionales adicionales pasados a la funcion se agruparan en tuplas
    suma = sum(numeros)   #almacena en una tupla todos los numeros porque usamos *antes de numeros
    cantidad = len(numeros)
    media = suma / cantidad
    return media
print('Media: ', calcular_media(10, 20, 30, 40))

def sumar_3(x):
    return x + 3

sumar = lambda x: x + 3 #funcion anonima de 1 linea que realiza alguna operacion simple y sencilla, se usa una sola vez
print('Sumarle 3 a un numero: ', sumar(5))


#documentacion de funciones (docstrings)
#documentar las funciones con docstrings que son cadenas de texto que describen el proposito, los parameros y el valor de
#retorno de una funcion. Se colocan inmediatamente despues de la def de la func y se encierra con triples comillas

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

#funciones con número variable de argumentos
#se permite definir funciones que acepten un numero variable de argumentos. Con el operador * antes del nombre del parametro
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3)) #imprime 6
print(suma_variable(4, 5, 6, 7)) #imprime 22