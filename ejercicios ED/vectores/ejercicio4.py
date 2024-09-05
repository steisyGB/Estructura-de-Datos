vector = []
for i in range(8):
    num = float(input(f"por favor ingresar el número {i+1}: "))
    vector.append(num)
numP = sum(1 for num in vector if num > 0)
print(f"Hay {numP} números positivos en el vector.")
