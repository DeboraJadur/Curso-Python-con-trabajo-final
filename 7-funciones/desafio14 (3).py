def funcdedivi(primernumero, segundonumero):
   try:
    resultado = primernumero / segundonumero
    print("El resultado de la división es:", resultado)
   except ZeroDivisionError:
    print("Hay un error, no se puede dividir por cero")
   except TypeError:
    print("Hay un error")

primernumero = int(input("Por favor ingrese el primer número: "))
segundonumero = int(input("Por favor ingrese el segundo número: "))

funcdedivi(primernumero, segundonumero)
