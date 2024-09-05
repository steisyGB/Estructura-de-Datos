vector = []
for i in range(10):
    num = float(input(f"Ingrese el número {i+1}: "))
    vector.append(num)
prom = sum(vector) / len(vector)
print(f"El promedio de los números es: {prom}")
