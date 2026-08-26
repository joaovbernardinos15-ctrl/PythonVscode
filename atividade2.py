print("--- Mercado da Vila ---")

#Se o Usuário digitar um valor 0 ou com letra.
try:
    ouro = int(input("Quantas moedas de ouro você tem? "))
    quantidade_itens = int(input("Quantos itens deseja comprar? "))
    
except ValueError: #se o valor tiver errado e foi digitado com letra levará aqui
    print("Por favor, insira um número válido.")
else:
    if quantidade_itens <= 0: #se o valor for menor ou igual a 0 levará aqui
        print("A quantidade de itens deve ser maior que zero.")
    else:

        try:
         custo_unitario = ouro / quantidade_itens
        except ZeroDivisionError: #se o valor for 0 levará aqui
                     print("Não é possível dividir por zero.")
        else: #se tudo estiver correto, levará aqui
                     print(f"Cada item vai custar {custo_unitario} moedas de ouro.")
