nombre = 'Juan'
edad = 25
altura = 1.75
es_estudiante = True
#a = b = c = 10 #el mismo valor para las 3 variables

#operadores aritmeticos
#suma + suma dos valores
#resta - resta el segundo valor del primero
#multiplicacion * multiplica dos valores
#division / divide el 1 valor por el segundo y devuelve el resultando en flotante (con coma)
#division entera // idem al de arriba pero devuelve un valor entero
#modulo % devuelve el resto de la division entre el 1 valor y el 2
#exponenciacion ** eleva el primer valor a la potencia del segundo

a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
exponencial = a ** b

#operadores de comparacion
#igual a == True si ambos son iguales
#diferente de != True si los valores son diferentes
#mayor que > True si el primer valor es mayor al segundo
#menor que < True si el primer valor es menor al segundo
#mayor o igual que >= True si el primer valor es mayor o igual que el segundo
#menor o igual que <= True si el primer valor es menor o igual que el segundo
c = 10
d = 3

igual = a == b
diferente = a != b 
mayor_que = a > b
menor_que = a < b
mayor_o_igual = a >= b
menor_o_igual = a <= b

#operadores logicos
#AND (and) True si ambas condiciones son verdaderas
#OR (or) True si al menos una condicion es verdadera
#NOT (not) invierte el valor de una condicion, True si era falsa y False si era verdadera
e = 10
f = 3

resultado_and = (a > 5) and (b < 5)
resultado_or = (a > 15) or (b < 5)
resultado_not = not (a > 5)

#reglas de precedencia de operadores, ciertos operadores tienen prioridad sobre otros. La procedencia sigue este orden:
#parentesis
#exponencial
#multiplicacion / division
#suma / resta
#operadores de comparacion
#operadores lógicos
