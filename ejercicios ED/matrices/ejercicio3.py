filas = 2
columnas = 3

matriz = []
print("\nPor favor, ingresa los valores :")

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f" [{i+1}][{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nLa matriz ingresada es: ")
for fila in matriz:
    print(fila)

transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

print("\nLa matriz transpuesta es: ")
for fila in transpuesta:
    print(fila)
