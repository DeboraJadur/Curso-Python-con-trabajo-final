with open("personas.csv") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        x = linea.split(',')
        print("A continuacion se mostraran los datos del archivo")
        print(x)



//Dado el archivo personas.csv (archivos de texto separado por comas), abrir el archivo con Python y utilizar el metodo split() para devolver cada linea del archivo por consola.