
class CuentaBancaria:
    def __init__(self, titular, saldo = 0.0):
        self.titular = str(titular)
        self.saldo = float(saldo)  
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print(f"Fondos insuficientes. Saldo actual: {self.saldo}")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

cuenta = CuentaBancaria("Isaac Perez")


cuenta.depositar(500)
cuenta.retirar(200)

cuenta.depositar(300)
cuenta.retirar(100)
cuenta.mostrar_saldo()
cuenta.retirar(501)
