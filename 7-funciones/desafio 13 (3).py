def saludoyvalor(nombre, valor):
    try:
        valor = int(valor)
        if isinstance(nombre, str) and nombre.isalpha():
            if valor == 0:
                print("Hola", nombre)
            else:
                print("Chau", nombre)
        else:
            print("El nombre debe ser una cadena de texto que contenga solo letras.")
    except ValueError:
        print("Se produjo un error de valor.")
    except TypeError:
        print("Se produjo un error de tipo.")

nombre = input("Ingrese el nombre de la persona: ")
valor = input("Ingrese un valor entero: ")

saludoyvalor(nombre, valor)