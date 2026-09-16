estoque = {
    'Maçã': 10,
    'Banana': 20,
    'Laranja': 15
}

fruta = input("Digite a fruta que deseja: ")

if fruta in estoque:
    print(f"Você pegou a fruta {fruta}.")
    print(f"Existe essa quantidade no estoque: {estoque[fruta]}")
else:
    print("Essa fruta não está no estoque.")
