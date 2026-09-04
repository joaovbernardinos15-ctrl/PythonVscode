estoque = ['Arroz', 'Feijao', 'Macarrao']
print("Estoque:", estoque)


print("Digite o nome do produto que quer adicionar ao estoque: ")
estoque.append(input())

print("exibir o estoque em ordem alfabética:", sorted(estoque))

if 'Arroz' in estoque:
    print("Esse produto foi adicionado:", 'Arroz' in estoque)
else:
    print("exibir se já existe o mesmo produto no estoque:", 'Feijao' in estoque)
    produto = input("Digite o nome do produto que deseja adicionar ao estoque: ")
    estoque.append(produto)

    print("Estoque atualizado:", estoque)
    
 