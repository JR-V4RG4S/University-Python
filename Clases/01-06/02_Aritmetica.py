class Aritmetica:
    def __init__(self, v1, v2):
        self.v1 = v1 
        self.v2 = v2
    
    def sumar(self):
        return self.v1 + self.v2
    
    def restar(self):
        return self.v1 - self.v2

    def multiplicar(self):
        return self.v1 * self.v2
    
    def dividir(self):
        return self.v1 / self.v2

operacion = Aritmetica(5,3)

print(f'La suma es: {operacion.sumar()}')
print(f'La resta es: {operacion.restar()}')
print(f'La multiplicación es: {operacion.multiplicar()}')
print(f'La división es: {operacion.dividir():.2f}') # :.2f = para mostrar 2 decimales
