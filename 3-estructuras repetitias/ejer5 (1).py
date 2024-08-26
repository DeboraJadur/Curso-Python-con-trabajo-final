limite_inferior = int(input("Ingrese el límite inferior  "))
limite_superior = int(input("Ingrese el límite superior  "))
valor_entero = int(input("Ingrese un valor entero: "))


if limite_inferior <= valor_entero <= limite_superior:
    print("El valor entero está dentro del intervalo.")
else:
    print("El valor entero NO está dentro del intervalo.")