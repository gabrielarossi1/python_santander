#Entradas/salidas
#la entrada y salida nos permite interactuar con el usuario y manipular archivos. Se puede solicitar informacion, mostrar resultados en pantalla y leer o escribir datos en archivos externos

#entrada de datos del usuario:
#funcion input
nombre = input('Ingresa tu nombre: ')
edad = input('Ingrese tu edad: ')
print('Hola, ' + nombre + '!')
print('Tienes ' + edad + ' años.')

#la cadena input siempre devuelve una cadena de texto, si se quiere trabajar con numeros se debera agregar int o float

edad_dos = int(input('Ingrese su edad: '))
if edad >= 18:
    print('eres mayor de edad')
else:
    print('eres menor de edad')


#Salida de datos
#con print, como venimos trabajando

nombre_dos = 'Juan'
edad_tres = 25
print(f'hola, mi nombre es {nombre} y tengo {edad} años.')
#las variables se incrustan dentro de la cadena utilizando {} y se precede la cadena con la letra f para indicar que es una f-string


#Lectura y escritura de archivos
#se puede leer y escribir datos en archivos externos, abrir archivos de diferentes modos:
#lectura ('r'), escritura ('w') o anexar ('a') y realizar operaciones de lectura y escritura

#lectura de archivos
#para leer un archivo primero se debe abrir con la funcion open() en modo de lectura ('r'), luego podemos leer el contenido del archivo utilizando metodos como read() o readlines()
#archivo = open('datos.txt', 'r')
#contenido = archivo.read()
#print(contenido)
#archivo.close()

#se abre el archivo 'datos.txt' en modo de lectura utilizando open(). se lee todo el contenido del archivo con read() y se almacena en la variable contenido, se muestra en pantalla y se cierra el archivo con close()


#escritura de archivos
#para escribir datos en un archivo, lo abrimos en modo de escritura ('w') utilizando la funcion open(). Si el archivo no existe, se crea automaticamente, si existia, se sobrescribe el contenido
archivo = open('datos.txt', 'w')
archivo.write('Hola, mundo!')
archivo.close()
#se abre el archivo datos.txt en modo de escritura utilizando open(), luego se escribe la cadena Hola, mundo en el archivo utilizando el metodo write() y se cierra con close()
#es importante cerrar los archivos luego de utilizarlos para liberar los recursos del sistema
#tambien se puede utilizar with para manejar la apertura y cierre de archivos de manera automatica
#with open('datos.txt', 'r') as archivo:
    #contenido = archivo.read()
    #print(contenido)
#con with se cierra automaticamente una vez que sale del bloque with, incluso si ocurre una excepcion


