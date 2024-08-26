dicdedatos={
    "DNI":[],
    "Nombre":[],
    "Apellido":[],
    "Email":[],
    "Fechadenacimiento":[],
    "Lugarderesidencia":[],
}
archivo=open("trabajofinal.csv","r")
lineas = archivo.readlines()
print("A continuacion se mostraran los datos del archivo")
for linea in lineas:
    datos = linea.split(";")
    dicdedatos["DNI"].append(datos[0])
    dicdedatos["Nombre"].append(datos[1])
    dicdedatos["Apellido"].append(datos[2])
    dicdedatos["Email"].append(datos[3])
    dicdedatos["Fechadenacimiento"].append(datos[4])
    dicdedatos["Lugarderesidencia"].append(datos[5])
    print(datos)

archivo.close()


print("A continuacion se mostraran los datos cuyo apellido sea Gomez")
for linea in lineas:
    datos=linea.split(";")
    if datos[2] == "Gomez":
        print("EL DNI ES: " + datos[0])
        print("El nombre es: " + datos[1])
        print("El apellido es: " + datos[2])
        print("El email es: " + datos[3])
        print("La fecha de nacimiento es: " + datos[4])
        print("El lugar de residencia es: " + datos[5])
        
print("A continuación se realizará un nuevo archivo")
nuevoarch = open("dicdedatos.csv", "w")
for linea in lineas:
    datos = linea.split(";")
    if datos[5].strip() == "Santa Fe" or datos[5].strip() == "Cordoba":
        nuevoarch.write(datos[0] + ";" + datos[1] + ";" + datos[2] + ";" + datos[3] + ";" + datos[4] + ";" + datos[5])
        print(datos)
nuevoarch.close()



