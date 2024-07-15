lista = {1,3,2,3,4,5,1,5,7,6,8,3,4}
print(lista)

ddds = {
    '61': 'Brasilia',
    '71': 'Salvador',
    '11': 'São Paulo',
    '21': 'Rio de Janeiro',
    '32': 'Juiz de Fora',
    '19': 'Campinas',
    '27': 'Vitória',
    '31': 'Belo Horizonte',
}
entrada = input()
if entrada in ddds:
    print(ddds[entrada])
else:
    print("DDD não cadastrado")