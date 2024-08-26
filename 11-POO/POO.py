class Calculadora:
    def __init__(self):
        pass
    
    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero")
        except TypeError:
            print("Error: Los operandos deben ser números")

calculadora = Calculadora()

try:
    primer_numero = int(input("Por favor ingrese un número: "))
    segundo_numero = int(input("Por favor ingrese el segundo número: "))

    print("Suma:", calculadora.sumar(primer_numero, segundo_numero))
    print("Resta:", calculadora.restar(primer_numero, segundo_numero))
    print("Multiplicación:", calculadora.multiplicar(primer_numero, segundo_numero))
    print("División:", calculadora.dividir(primer_numero, segundo_numero))

except ValueError:
    print("Error: Ingrese un número válido")
