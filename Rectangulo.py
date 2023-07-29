class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura



#base_str = input("Proporciona la base: ")
#base = int(base_str)
base = int(input("Proporciona la base: "))
#altura_str = input("Proporciona la altura: ")
#altura = int(altura_str)
altura = int(input("Proporciona la altura: "))

#Creamos un objeto Rectangulo con la data obtenido por teclado
rectangulo1 = Rectangulo(base,altura)
print(f'El area del rectangulo es {rectangulo1.calcular_area()}')