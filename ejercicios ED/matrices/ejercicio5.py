filas = 3
columnas = 3

matriz = []
print("\nPor favor, ingresa los valores ")

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f" [{i+1}][{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nLa matriz ingresada es:")
for fila in matriz:
    print(fila)

diagonal = [matriz[i][i] for i in range(filas)]
print(f"\nLos elementos de la diagonal principal son: {diagonal}")
