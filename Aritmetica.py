
class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    #Operacion Suma
    def sumar(self):
        return self.operandoA + self.operandoB

    #Operacion Resta
    def restar(self):
        return  self.operandoA - self.operandoB

    #Operacion Multiplicacion
    def multiplicar(self):
        return self.operandoA * self.operandoB

    #Operacion Division
    def dividir(self):
        return  self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5, 3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicacion: {aritmetica1.multiplicar()}')
print(f'Division: {aritmetica1.dividir():.2f}')
