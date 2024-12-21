#importacion y creacion de modulos
#un modulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas
#la importacion de modulos nos permite acceder a la funcionalidad definida en otros archivos y reutilizar codigos de manera eficiente
#podemos crear nuestros propios modulos para organizar y modularizar nuestro codigo
#python tiene una amplia biblioteca estandar de modulos que proporcionan funcionalidades adicionales, estan disponibles sin necesidad de instalarlos por separado

#importar modulos
#para importar un modulo se usa import, se puede importar completo o funciones especificas de un modulo
import math
resultado = math.sqrt(25)
print(resultado) #imprime 5.0

#importa el modulo math, utiliza la funcion sqrt que calcula la raiz cuadrada de 25.
#tambien se puede importar utilizando la sintaxis from modulo import funcion
from math import sqrt
resultado_dos = sqrt(25)
print(resultado_dos) #imprime 5.0

#math proporciona funciones matematicas como sqrt() raiz cuadrada, sin() seno, cos() coseno, etc
#random genera numero aleatorios, ramdom() numero aleatorio entre 0 y 1, randit() numero entero aleatorio en un rango, etc
#deletime permite trabajar con fechas y horas, detetime.now() fecha y hora actual, datetime.date() fecha, datetime() hora, etc


import random
#import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) #imprime un numero entero aleatorio entre 1 y 10

#fecha_actual = datetime.now()
#print(fecha_actual) #imprime la fecha y hora actual


#Creacion y utilizacion de modulos personalizados
#simplemente creamos un nuevo archivo python con el nombre deseado y definimos las funciones, clases y variables que queremos incluir en el modulo
import mi_modulo

mi_modulo.saludar('Juan') 
resultado_tres = mi_modulo.calcular_suma(5, 3)
print(resultado_tres) #imprime 8

#organizacion del codigo en módulos
#cuando el programa crece en tamaño y complejidad, es una buena practica organizar nuestro codigo en módulos separados segun su funcionalidad.
#permite tener un codigo mas legible y facil de mantener

import operaciones
import utilidades

resultado_cuatro = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f'El resultado de la suma es: {resultado}')

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f'Hola, {nombre}!')


#Paquetes
#es una forma de organizar modulos relacionados en una estructura jerarquica de directorios. Nos permiten agrupar modulos relacionados y evitar conflictos de nombres entre modulos

#crear y utilizar paquetes
#para crear un paquete, creamos un directorio con el nombre deseado y agregamos un archivo especial llamado __init__.py dentro del directorio
#este archivo puede estar vacio o contener codigo de inicializacion del paquete


from mi_paquete import modulo1, modulo2
modulo1.funcion1()
modulo2.funcion2()
#se importan los modulos 1 y 2 del paquete mi_paquete y se utilizan las funciones definidas en ellos

#la importacion y creacion de modulos ayuda a organizar y reutilizar codigo de manera eficiente, al modularizar nuestro codigo podemos mantener un cod mas legible, estructurado y facil de mantener

