nomes = ["Jack", "Charlie", "Bob", "Frank", "Eva", "David", "Ian", "Hannah", "Gra", "Alice"]

print("Nomes na lista:")
for i in range(len(nomes)):
    print(f"{i + 1} - {nomes[i]}")
    
print("ordem alfabética:")
nomes.sort()
for i in range(len(nomes)):
    print(f"{i + 1} - {nomes[i]}")