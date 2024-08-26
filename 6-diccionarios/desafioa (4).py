# Creamos el diccionario con listas vacías 
usuarios = {
    "nombres": [],
    "apellidos": [],
    "dni": []
}

tamanio = 3

# Leemos los datos y los agregamos al diccionario
for i in range(tamanio):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombres: ")
    apellido = input("Apellido: ")
    dni = input("Identificación: ")

    # Agregamos los datos a las listas correspondientes en el diccionario
    usuarios["nombres"].append(nombre)
    usuarios["apellidos"].append(apellido)
    usuarios["dni"].append(dni)

# Ahora devolveremos los valores en el diccionario y los mostramos
for i in range(tamanio):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios["nombres"][i])
    print("Apellido:", usuarios["apellidos"][i])
    print("DNI:", usuarios["dni"][i])

