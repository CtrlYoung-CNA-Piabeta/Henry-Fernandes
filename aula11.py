# Calcular a média em uma lista
# Ex: [1, 2, 3, 4, 5] = 3

def media(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)
lista1 = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 , 9, 10]
print(media(lista1))