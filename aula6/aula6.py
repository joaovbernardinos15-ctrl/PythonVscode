cadastro = {'nome': 'bob', 'sobrenome': 'Sponja'}

cadastro['endereço'] = 'Fenda do Biquini'

cadastro['profissao'] = 'Chapeiro'

print(cadastro)

del cadastro['profissao']
cadastro['profissao'] = 'Cozinheiro'
print(cadastro)


print(cadastro.get('amigo'))


print(list(cadastro))

print(sorted(cadastro))

cadastro['amigo'] = 'Patrick Estrella'
cadastro['salario'] = 20

print(cadastro)

cadastro['mochila'] = ['Espatula', 'Aventual', 'Calça Quadrada extra']
print(cadastro)

for k,v in cadastro.items():
    print(f"{k}: {v}")