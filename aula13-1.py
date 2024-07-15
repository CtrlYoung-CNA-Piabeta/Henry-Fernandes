class Animal:
    def __init__(self):
        print('Animal Criado')
    
    def oQueE(self):
        print('Animal')

    def comer(self):
        print('Comendo...')

class Abelha(Animal):
    def __init__(self):
        print('Abelha Criado')
    
    def oQueE(self):
        print('Abelha')
    
    def bzz(self):
        print('Bzzz')