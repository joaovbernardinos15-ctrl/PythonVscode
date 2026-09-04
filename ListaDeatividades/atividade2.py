nota1 = float(input( "Digite a primeira nota do aluno: " ))
nota2 = float(input( "Digite a segunda nota do aluno: " ))
nota3 = float(input( "Digite a terceira nota do aluno: " ))
nota4 = float(input( "Digite a quarta nota do aluno: " ))
media = (nota1 + nota2 + nota3 + nota4) / 4
status = ""

if media >= 7.0:
        status = "Aprovado Direto"
elif media >= 5.0:
        status = "Em Recuperação"
else:
    status = "Reprovado"
    print(f"Situação do estudante: {status} com média {media:.2f}")