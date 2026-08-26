print("--- Cadastro na Plataforma ---")
idade_texto = input("Digite sua idade em números: ")
# Se o usuário digitar texto, o programa quebra aqui!
try:
    idade = int(idade_texto)
    if idade >= 18:
        print("Acesso liberado para a trilha avançada.")
    else:
        print("Acesso restrito.")
except ValueError:
    print("Por favor, insira um número válido.")
