class Persona: 
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad,sueldo):       # añadimos el sueldo del empleado
        super().__init__(nombre, edad)
        self._sueldo = sueldo

if __name__ == "__main__":
    empleado1  = Empleado("carlos",25,28000)

    print(empleado1._nombre)
    print(empleado1._edad)
    print(empleado1._sueldo)