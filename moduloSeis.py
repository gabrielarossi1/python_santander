#manejo de errores y excepciones
#Se pueden manejar los errores de manera controlada utilizando el manejo de excepciones. Nos permite capturar y manejar errores especificos sin que el programa se detenga abruptamente

#errores comunes

#error de sintaxis (SyntaxError)
#ocurre cuando el cod no sigue las reglas de sintaxis de python, como olvidar los : despues de una declaracion

#def mi_funcion()    arroja error porque faltan los :
    #print('¡Hola!')

#error de nombre (NameError)
#ocurre cuando se hace referencia a una variable o funcion que no ha sido definida
#print(variable_no_definida)

#error de tipo (TypeError)
#cuando se realiza una operacion con tipos de datos incompatibles, como intentar sumar un numero y una cadena
#resultado = 5 + '10'

#error de indice(IndexError)
#cuando se intenta acceder a un indice fuera del rango valido de una lista o secuencia
#lista = [1, 2, 3]
#print(lista[3]) #el indice 3 esta fuera del rango


#manejo de excepciones
#permite capturar y manejar errores de manera controlada utilizando try, except y finally

#Try
#el bloque Try contiene el cod que puede generar una excepcion, si ocurre una excepcion dentro del bloque try, el flujo de ejecucion se transfiere al bloque except correspondiente
try:
    #cod que puede generar una excepcion
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print('Error: Division por cero')

#Except
#el bloque except especifica el tipo de excepcion que se desea capturar y manejar. Puede tener multiples bloques except para manejar diferentes tipos de excepciones
#try:
    #cod que puede generar una excepcion
    #resultado = 10 / 0
    #print(resultado)
#except ZeroDivisionError:
    #print('Error: Division por cero')
except ValueError:
    print('Error:  Valor invalido')


#Finally
#es opcional y se ejecuta siempre, independientemente de si ocurrio o no la excepcion. Se utiliza para tareas de limpieza o liberacion de recursos
#try:
    #cod que puede generar una excepcion
    #archivo = open('archivo.txt',  'r')
    #realiza operaciones con el archivo
#except FileNotFoundError:
    #print('Error: Archivo no encontrado')
#finally:
    #archivo.close() #cierra el archivo siempre incluso si no ocurre la excepcion


#excepciones personalizadas
#se pueden crear excepciones, para situaciones especificas en el programa
#se debe crear una clase que herede de la clase bas exception o de una subclase

#def funcion():
    #cod que puede generar una excepcion personalizada
    #if condicion:
        #raise Exception('descripcion del error')
    
#try:
    #funcion()
#except Exception as e:
    #print(f'Error: {str(e)}')
