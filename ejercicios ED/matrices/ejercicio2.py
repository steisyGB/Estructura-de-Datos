tamaño = 4
matriz = []

print("\nPor favor, ingresa los valores:")

for i in range(tamaño):
    fila = []
    for j in range(tamaño):
        if i == j:
            valor = float(input(f" [{i+1}][{j+1}]: "))
            fila.append(valor)
        else:
            valor = float(input(f" [{i+1}][{j+1}]: "))
            fila.append(valor)
    matriz.append(fila)

print("\nLa matriz ingresada es:")
for fila in matriz:
    print(fila)

