#Le pido dos numeros  Crear un programa principal (main) que ejecute las siguientes funciones:

1-     “Dado dos números enteros retornar el máximo.”

2-     “Dado un número A y un segundo número B, enteros, retornar la potencia de A elevado a la B.”

Crear un módulo con las funciones anteriores.

El programa principal debe importar el módulo.

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
import funciones
print("El numero mayor es: ")
print(funciones.encontrarmax(num1,num2))



# Le pido dos números para calcular la potencia
numA = int(input("Ingrese el número base: "))
numB = int(input("Ingrese el número exponente: "))

import funciones
print("La potencia del numero calculado sera: ")
print(funciones.calcularpotencia(numA,numB))