carrinho = []

while True:
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if produto.lower() == 'sair':
        break
    carrinho.append(produto)

print("Produtos no carrinho:")
for i in range(len(carrinho)):
    print(f"{i + 1} - {carrinho[i]}")