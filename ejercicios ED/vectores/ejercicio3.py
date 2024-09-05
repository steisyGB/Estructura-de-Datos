vector = []
for i in range(7):
    num = float(input(f"Ingrese el número {i+1}: "))
    vector.append(num)
mayor = max(vector)
print(f"El mayor número ingresado es: {mayor}")
