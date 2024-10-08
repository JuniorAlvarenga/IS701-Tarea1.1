class Rectangulo:
    def __init__(self, base, altura):
        Rectangulo.base = float(base)
        Rectangulo.altura = float(altura)
    def area(self):
        return self.altura * self.base
    def perimetro(self):
        return 2 * (self.altura + self.base)
    
rectangulo = Rectangulo(5,3)

area_rectangulo = rectangulo.area()
perimetro_rectangulo = rectangulo.perimetro()

print(f"El área del rectángulo es: {area_rectangulo}")
print(f"El perímetro del rectángulo es: {perimetro_rectangulo}")