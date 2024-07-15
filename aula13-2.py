class Banco:
   saldo = 0

    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self):
        self.saldo -= valor

class Cc(Banco):
    def __init__(self):
        print('Cc')

    def pix(self, valor):
        if self.getSaldo() > valor:
            self.setSaldo(self, valor)

class Cp: