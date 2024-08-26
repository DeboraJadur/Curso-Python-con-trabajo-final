mi_lista = ["Python", "C", "C++", "JavaScript", "Ruby", "Cobol", "Pascal", "Klotin", "HTML", "CSS"]

while True:
    try:
        pos = int(input("Ingrese la posición: "))
        print(mi_lista[pos])
        break 
     # Salgo si se ingresa un valor válido
    except IndexError:
        print("Escribió una posición fuera del rango")
    except ValueError:
        print("Escribió una posición erronea")
    finally:
        print("Muchas gracias")