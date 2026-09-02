score_total = 0
rodadas = 3
for i in range(rodadas):
    while True:
        entrada = input(f"Rodada {i+1}: Digite os pontos ganhos ou 'pular': ")
        if entrada == 'pular':
         print("Rodada pulada.")
        break

else:
    try:
        score_total += int(entrada)
        print(f"Score atualizado: {score_total}")
        
       
    except:
        print("Erro! Por favor, digite um número inteiro válido.")
# O while continuará rodando, pedindo a entrada novamente