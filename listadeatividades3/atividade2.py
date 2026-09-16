diario_classe = {}


aluno = input("Digite o nome do primeiro aluno: ")
nota = float(input("Digite a nota do primeiro aluno: "))
diario_classe[aluno] = nota


aluno = input("Digite o nome do segundo aluno: ")
nota = float(input("Digite a nota do segundo aluno: "))
diario_classe[aluno] = nota


aluno = input("Digite o nome do terceiro aluno: ")
nota = float(input("Digite a nota do terceiro aluno: "))
diario_classe[aluno] = nota


print("\nDiário da classe:")
print(diario_classe)


media = sum(diario_classe.values()) / len(diario_classe)

print(f"Média da turma: {media:.2f}")
