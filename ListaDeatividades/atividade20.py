lista_convidado_vip = ["João", "Maria", "José", "Ana", "Carlos", "Fernanda", "Paulo", "Juliana", "Rafael", "Camila", "Bruno", "Isabela", "Gustavo", "Larissa", "Felipe", "Mariana"]

print("Lista de convidados VIP:", lista_convidado_vip)

print("adicionar um convidado VIP à lista de convidados: ")
novo_convidado = input()
lista_convidado_vip.append(novo_convidado)
print("Lista de convidados VIP atualizada:", lista_convidado_vip)
print("---------")

print("remover um convidado VIP da lista de convidados pelo nome: ")
convidado_remover = input()
lista_convidado_vip.remove(convidado_remover)
print("Lista de convidados VIP atualizada:", lista_convidado_vip)
print("---------")

print("verificar se um convidado VIP está na lista de convidados: ")
convidado_verificar = input()
if convidado_verificar in lista_convidado_vip:
    print(f"{convidado_verificar} está na lista de convidados VIP.")
else:
    print(f"{convidado_verificar} não está na lista de convidados VIP.")
print("---------")