#Estructuras de catos
#permiten organizar y almacenar datos de manera mas eficiente en nuestros programas. Hay varias:
#listas, tuplas, diccionarios y conjuntos

#listas es una estructura de datos mutable y ordenada que permite almacenar una coleccion de elementos.
#los elementos pueden ser de dif tipos de datos y se encierran con [ ] separados por ,

#creacion
frutas = ['manzana', 'banana', 'naranja']
#acceso
print(frutas[0]) #muestra manzana
print(frutas[1]) #muestra banana
print(frutas[2]) #muestra naranja
#tambien se puede acceder desde el final unsando indices negativos
print(frutas[-1]) #muestra naranja
print(frutas[-2]) #muestra banana
print(frutas[-3]) #muestra manzana

#metodos de listas
# append(elemento) agrega un elemento al final de la lista
# insert(indice, elemento) inserta un elemento en la posicion especificada de la lista
# remove(elemento) elimina la primera aparicion de un elemento en la lista
# pop(indice) elimina y devuelve el elemento en una posicion especifica de la lista
# sort() ordena los elementos de la lista en orden ascendente
# reverse() invierte el orden de los elementos en la lista

frutasDos = ['manzana', 'banana', 'naranja']
frutasDos.append('pera')
print(frutasDos) #imprime manzana, banana, naranja y pera

frutasDos.insert(1, 'uva')
print(frutasDos) #imprime manzana, uva, banana, naranja, pera

frutasDos.remove('banana')
print(frutasDos) #imprime manzana, uva, naranja, pera

fruta_eliminada = frutasDos.pop(2)
print(frutasDos) #imprime manzana, uva y pera
print(fruta_eliminada) #imprime naranja

frutasDos.sort()
print(frutasDos) #imprime manzana, pera, uva

frutasDos.reverse()
print(frutasDos) #imprime uva, pera, manzana

#listas de comprension
#son una forma concisa de crear nuevas listas basadas en una secuencia existente. permite filtrar y transformar los elementos de una lista en una sola linea de codigo
numeros = [1, 2, 3, 4, 5]
cuadrados = [ x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados) #imprime 4, 16

#crea una lista llamada cuadrados que contiene los cuadrados de los numeros pares de la lista. la expresion x ** 2 eleva cada elemento al cuadrado y la condicion if x % 2 filtra los numeros pares


#tuplas
#estructura de datos inmutable y ordenada que permite almacenar una coleccion de elementos
#los elementos de la tupla se encierran entre () separados por ,
#creacion
punto = (3, 4)
#acceso
print(punto[0]) # imprime 3
print(punto[1]) #imprime 4
#a dif de las listas, las tuplas no se pueden modificar una vez creadas, no se pueden agregar, eliminar o cambiar elementos de una tupla existente
#son utiles cuando se necesita almacenar una coleccion de elementos que no debe modificarse, como coordenadas o datos de configuracion

#metodos de las tuplas
# count(elemento) devuelve el numero de veces que aparece un elemento en la tupla
# index(elemento) devuelve el indice de la primera aparicion de un elemento en la tupla. Se puede especificar inicio y fin de la busqueda
# len(tupla) no es un metodo pero es una funcion que devuelve la longitud de la tupla

mi_tupla = (1, 2, 3, 4, 2, 2)
print(mi_tupla.index(2)) #salida: 1
print(mi_tupla.index(2, 2)) #salida 4
print(mi_tupla.index(2, 2, 6)) #salida 4



#diccionarios
#estructura de datos mutables y no ordenada que permite almacenar pares de clave-valor. Cada elemento del diccionario consiste en una clave unica
# y su valor correspondiente. Se encierran entre {} y los pares clave-valor se separan con ,

#creacion
persona = {'nombre':'Juan', 'edad':'25', 'ciudad':'Madrid'}
#acceso
print(persona['nombre']) #imprime Juan
print(persona['edad']) #imprime 25
print(persona['ciudad']) #imprime Madrid

#se puede utilizar el metdo get() para obtener el valor de una clave, si no existe devuelve None

#metodos de los diccionarios
# keys() devuelve una vista de todas las claves del diccionario
# values() devuelve una vista de todos los valores del diccionario
# items() devuelve una vista de todos los pares clave-valor del diccionario
# update(otro_diccionario) actualiza el diccionario con los pares clave-valor de otro diccionario

#ejemplo
persona_dos = {'nombre':'Juan', 'edad':'25', 'ciudad':'Madrid'}
print(persona_dos.keys()) #dict_keys(['nombre', 'edad', 'ciudad'])
print(persona_dos.values()) #dict_values(['Juan', '25', 'Madrid'])
print(persona_dos.items()) #dict_items([('nombre', 'Juan'), ('edad', '25'), ('ciudad', 'Madrid')])

persona_dos.update({'profesion':'ingeniero'})
print(persona_dos) #imprime {'nombre': 'Juan', 'edad': '25', 'ciudad': 'Madrid', 'profesion': 'ingeniero'}



#Conjuntos (set)
#un conjunto es una estructura de datos mutables y no ordenada que permite almacenar una coleccion de elementos unicos. los conjuntos se encierran entre {} o se crean usando la funcion set()

#creacion y operaciones basicas
frutas_nueva = {'manzana', 'banana', 'naranja'}
numeros_nuevos = set([1, 2, 3, 4, 5])
#admiten operaciones matematicas de conjuntos como la union (|), la interseccion (&), diferencia(-) y diferencia semantica (^)

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union) #imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion) #imprime 3

diferencia = conjunto1 - conjunto2
print(diferencia) #imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica) #imprime {1, 2, 4, 5}

#metodos de los conjuntos
# add(elemento) agrega un elemento al conjunto
# remove(elemento) elimina un elemento del conjunto, si el elemento  no existe, genera un error
# discard(elemento) elimina un elemnto del conjunto si esta presente, si no existe, no hace nada
# clear() elimina todos los elementos del conjunto

#ejemplo
fruit = {'manzana', 'banana', 'naranja'}

fruit.add('pera')
print(fruit) #imprime {'manzana', 'banana', 'naranja', 'pera'}

fruit.remove('banana')
print(fruit) #imprime {'manzana', 'naranja', 'pera'}

fruit.discard('uva')
print(fruit) #imprime {'manzana', 'naranja', 'pera'}

fruit.clear()
print(fruit) #imprime set()
