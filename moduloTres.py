#Estructuras de control
#las mas comunes son condicionales y bucles

#Condicionales
#if
#se utiliza para ejecutar un bloque de código si una condicion es verdadera

edad = 18
if edad >= 18:
    print('Eres mayor de edad')

#if - else
#nos permite especificar un bloque de código alternativo que se ejecutara si la condicion del if es falsa
edad_dos = 15
if edad_dos >= 18: 
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

#if-elif-else
#permite especificar multiples condiciones y bloques de códigos alternativos
calificacion = 85
if calificacion >= 90:
    print('Excelente')
elif calificacion >= 80:
    print('Muy bueno')
elif calificacion >= 80:
    print('Bueno')
else:
    print('Necesita mejorar')

edad_tres = 70
if edad_tres < 18:
    print('Eres menor de edad')
elif edad_tres >= 18 and edad_tres < 60:
    print('Eres un adulto')
elif edad_tres > 15:
    print('Mayor de 15 años')
elif edad_tres == 60:
    print('Feliz 60 cumpleaños')
else:
    print('Eres adulto mayor')


#bucles y loops
#for para iterar una secuencia o cualcuier objeto iterable
frutas = ['manzana', 'banana', 'naranja']
for fruta in frutas:
    print(fruta)

#while para repetir un bloque de codigo mientras una condicion sea verdadera
#corta cuando se vuelve falso
contador = 0
while contador < 5:
    print(contador)
    contador += 1

print('Numeros del 1 al 5 multiplicados por 2 con bucle for: ')
for numero in range (1, 6):   #toma numeros del 1 al 5 inclusive, en ese rango
    print(numero * 2)

print('\nNumeros del 1 al 5 multiplicados por 2 con bucle while: ')
contadores = 1
while contadores <= 5:
    print(contadores * 2)
    contadores += 1 #condicion de salida


#control de bucles
#break para salir prematuramente de un bucle
cont = 0
while True:
    print(cont)
    cont += 1

    if cont == 5:
        break

#continue para saltar el resto del bloque de codigo dentro de un bucle y pasar a la sig iteración
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#pass es una operacion nula que no hace nada. se usa como marcador de posicion cuando se requiere una instruccion
#sintacticamente pero no se desea realizar ninguna operacion
for i in range(5):
    pass


