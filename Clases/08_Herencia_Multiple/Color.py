class Color:
    def __init__(self, color):
        self.__color = color 

    @property
    def color (self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value
    
    def __str__(self):
        return f'el color es: {self.color}'