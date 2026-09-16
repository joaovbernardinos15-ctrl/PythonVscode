convidados_noivo = ["João", "Maria", "Pedro"]
convidados_noiva = ["Maria", "Jose", "Ana"]

lista_unica = []
for nome in convidados_noivo + convidados_noiva:
    if nome not in lista_unica:
        lista_unica.append(nome)

print("Nomes sem repetir:")
print(lista_unica)