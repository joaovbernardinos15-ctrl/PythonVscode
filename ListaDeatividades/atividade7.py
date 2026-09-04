cores = ["vermelho", "verde", "azul"]

corindisponivel = ["amarelo", "roxo", "laranja"]

print("Cores disponíveis:")
for i in range(len(cores)):
    print(f"{i + 1} - {cores[i]}")
    
    print("--------------")
    
    print("Escolha uma cor para pintar a parede:")
    print("cores indisponíveis:")
    print(corindisponivel)