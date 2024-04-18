class Rectangulo:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2 
    
    def area(self):
        return self.v1 * self.v2 
    
v1 = int(input("Ingrese la base: "))
v2 = int(input("Ingrese la altura: "))

operacion = Rectangulo(v1,v2)
print(f'El área del rectangulo es: {operacion.area()}')
