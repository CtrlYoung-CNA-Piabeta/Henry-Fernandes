class Carro():
    portas = 4
    marca = 'fiat'
    modelo = 'uno'
    cor = 'verde'
    motor = 'v12'
    extra = 'escada'
    velocidade = 0

    # Métodos da classe Carro
    def dar_partida(self):
        print('Sente o ronco do motor!')
    
    def acelerar(self):
        self.velocidade += 100
    
    def freiar(self):
        self.velocidade -= 100

# Exemplo
carro1 = Carro()
carro1.dar_partida()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
print(carro1.velocidade)
print("Olha o radar!")
carro1.freiar()
carro1.freiar()
print(carro1.velocidade)

# Atividade 1: Criar uma classe de Animal
class Animal():
    reino = 'animalia'
    superclasse = 'peixes'
    ordem = 'lamniformes'

# Método inicializador
    def __init__(self, especie, nome_comum):
        self.especie = especie
        self.nome_comum = nome_comum

    def __str__(self):
        return f"Este é um tubarão chamado {self.nome_comum} e pertence à espécie {self.especie}"

# Métodos da classe Animal
    def respirar(self):
        print('O tubarão-branco nada para continuar realizando sua troca gasosa.')
    
    def morder(self):
        print('O tubarão-branco morde com uma força monstruosa!')

# Exemplo
tubarao1 = Animal('c. carcharias', 'tubarão-branco')
tubarao1.respirar()
tubarao1.morder()
print(tubarao1)
