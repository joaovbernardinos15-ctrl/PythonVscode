#Usei mediafinal para ser digitada pelo Usuário,
#O resultado sendo pra mostrar a nota final do aluno
mediafinal = float(input("Digite a sua média(): "))
resultado = "Media final: " + str(mediafinal)

#Usei If,elif,else para mostrar se o aluno foi aprovado ou 
# ficou em recuperação ou 
# reprovado, de acordo 
# com a nota digitada pelo usuário

if mediafinal >= 7.0:
    status = "Aprovado"
elif mediafinal >= 5.0:
    status = "Em recuperação"
else: 
    status = "Reprovado"    

#Usei a Print para mostrar o Resultado da nota final e pra mostrar os status do aluno, se 
# ele foi aprovado, 
# ficou em recuperação ou reprovado

print(resultado)     
print(f"O aluno está {status}.")     
        