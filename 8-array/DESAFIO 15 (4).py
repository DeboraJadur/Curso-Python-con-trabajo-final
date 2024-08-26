//Realizar un programa que cargue 4 personas con sus datos: nombre, apellido y edad.

Se debe almacenar en un diccionario y luego, recorrer ese diccionario y escribir en un archivo con extensión txt o csv.

Los datos de cada Persona, debe estar separado por comas (Dentro del archivo). 

Por Ejemplo: juan,perez,19//


NUM_ITERACIONES = 3
diccionariodepersonas={
    "nombre":[],
    "apellido":[],
    "edad":[]
}

for i in range(NUM_ITERACIONES):
    nombre=input("Ingrese un nombre: ")
    diccionariodepersonas["nombre"].append(nombre)
    apellido=input("Ingrese un apellido: ")
    diccionariodepersonas["apellido"].append(apellido)
    edad=input("Ingrese una edad : ")   
    diccionariodepersonas["edad"].append(edad)

arch=open ("diccionariodepersonas.txt","w")
for i in range(NUM_ITERACIONES):
    arch.write(diccionariodepersonas["nombre"][i]+",")
    arch.write(diccionariodepersonas["apellido"][i]+",")
    arch.write(diccionariodepersonas["edad"][i]+"\n")
arch.close()

for i in range(NUM_ITERACIONES):
    print(diccionariodepersonas["nombre"][i]+","+ diccionariodepersonas["apellido"][i]+","+diccionariodepersonas["edad"][i]+"\n")




