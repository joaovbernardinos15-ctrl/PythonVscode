media = float(input("Digite a média do aluno: "))

if media >= 7.0:
    status = "Aprovado"
elif media >= 5.0:
    status = "Recuperação"
else: 
    status = "Reprovado"
    
print(f"O aluno está {status}.")