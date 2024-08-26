try:
    primernumero= int(input("Por favor ingrese un numero: "))
    segundonumero= int(input("Por favor ingrese el segundo numero"))
    resultado= primernumero/segundonumero
    print("El resultado de la division es: ", resultado)

except ZeroDivisionError:
    print("Hay un error, no se puede dividir por cero")
except TypeError:
     print("Hay un error")