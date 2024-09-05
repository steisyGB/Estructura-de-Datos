vector = []
for i in range(6):
    num = float(input(f"Ingrese el número {i+1}: "))
    vector.append(num)
vectorI = vector[::-1]
print(f"El vector invertido es: {vectorI}")
