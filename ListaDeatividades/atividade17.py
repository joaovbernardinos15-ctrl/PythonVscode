nomes = ['Leonardo', 'Maria', 'José', 'Ana', 'Carlos', 'Fernanda', 'Paulo', 'Juliana', 'Rafael', 'Camila', 'Bruno', 'Isabela', 'Gustavo', 'Larissa', 'Felipe', 'Mariana']


print("ordem alfabética da lista de nomes:", sorted(nomes))

print("escolher um nome da lista aleatoriamente para ser representante do grupo: ")
import random
representante = random.choice(nomes)
print("O representante escolhido foi:", representante)