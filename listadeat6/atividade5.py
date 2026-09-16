estoque = {
    "Caneta": {"quantidade": 50, "preco": 2.50},
    "Caderno": {"quantidade": 20, "preco": 15.00},
    "Borracha": {"quantidade": 10, "preco": 1.00}
}


def atualizar_estoque(estoque, produto, quantidade_vendida):
    if produto in estoque:
        if estoque[produto]["quantidade"] >= quantidade_vendida:
            estoque[produto]["quantidade"] -= quantidade_vendida
            print(f"Venda realizada! {quantidade_vendida} unidade(s) de {produto} foram retiradas do estoque.")
        else:
            print("Erro: quantidade insuficiente em estoque.")
    else:
        print("Erro: produto não encontrado no estoque.")



atualizar_estoque(estoque, "Caneta", 5)



valor_total = 0

for produto, dados in estoque.items():
    valor_total += dados["quantidade"] * dados["preco"]

print("\nEstoque atualizado:")
for produto, dados in estoque.items():
    print(f"{produto}: {dados['quantidade']} unidades - R$ {dados['preco']:.2f}")

print(f"\nValor total em estoque: R$ {valor_total:.2f}")
