vector = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i+1}: "))
    vector.append(numero)
suma = sum(vector)
print(f"La suma de los elementos es: {suma}")
