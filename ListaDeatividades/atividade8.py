numeros = ["55", "10", "15", "20", "45", "30", "35", "40", "25", "50"]

print("Números na lista:")
for i in range(len(numeros)):
    print(f"{i + 1} - {numeros[i]}")
    
print("ordem alfabética:")
numeros.sort()
for i in range(len(numeros)):
    print(f"{i + 1} - {numeros[i]}")