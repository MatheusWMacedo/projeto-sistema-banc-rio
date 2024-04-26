class Saque:
    def __init__(self,saldo, valor):
        self._saldo = saldo
        self._valor = valor

    def depositar(self, valor):
        if valor > 0:
           self._saldo += valor
           return self._saldo
             

class Deposito:
    pass

s = Saque(560, 89)
print(s.depositar( 0.1))