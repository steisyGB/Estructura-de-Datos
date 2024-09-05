print("Por favor, ingrese los valores: ")
matriz1 = []
for i in range(2):
    fila = []
    for j in range(2):
        valor = float(input(f" [{i+1}][{j+1}] : "))
        fila.append(valor)
    matriz1.append(fila)

print("\nPor favor, ingrese los valores: ")
matriz2 = []
for i in range(2):
    fila = []
    for j in range(2):
        valor = float(input(f" [{i+1}][{j+1}] : "))
        fila.append(valor)
    matriz2.append(fila)

resultado = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        resultado[i][j] = sum(matriz1[i][k] * matriz2[k][j] for k in range(2))

print("\nEl resultado de la multiplicación es:")
for fila in resultado:
    print(fila)
