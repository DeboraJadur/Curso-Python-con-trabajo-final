print("Por favor ingrese las notas, recuerde que si la nota es 0 el programa finalizara")
listadenotas = []
nota= 1

while nota != 0:
    nota = int(input())
    if nota != 0:
        listadenotas.append(nota)

print("Las notas son:",listadenotas)