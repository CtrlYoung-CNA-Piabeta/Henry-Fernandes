# Tuplas

tup = (5, 'oi', True, 2.5)
# tup.append(6) - impossível pois tupla não muda (apenas manualmente)
# print(tup)

# Sets

unico = set()
# unico.add(5)
# print(unico)

# Dicionários

pessoa = {
    'nome': 'Henry',
    'idade': 20
}

# print(pessoa['nome'])

dic = {
    'nome': 'Henry',
    'idade': 20,
    'id': 1231234
}

if 'nome' in dic:
    print(dic['nome'])

print(dic['nome'])

for chave in dic.keys():
    print(chave)

for valor in dic.values():
    print(valor)

