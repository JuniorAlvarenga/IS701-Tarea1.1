class Calculadora:
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            return "División por cero no permitida"
        return a / b

calculadora = Calculadora()

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

print(f"Suma: {a} + {b} = {calculadora.sumar(a, b)}")
print(f"Resta: {a} - {b} = {calculadora.restar(a, b)}")
print(f"Multiplicación: {a} * {b} = {calculadora.multiplicar(a, b)}")
print(f"División: {a} / {b} = {calculadora.dividir(a, b)}")
