import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        try:
            return math.pi * (self.radio ** 2)
        except TypeError:
            raise TypeError("El radio debe ser un valor numérico")

    def perimetro(self):
        try:
            return 2 * math.pi * self.radio
        except TypeError:
            raise TypeError("El radio debe ser un valor numérico")

    @staticmethod
    def pedir_radio():
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            return radio
        except ValueError:
            raise ValueError("El radio debe ser un valor numérico")

# Ejemplo de uso
try:
    radio1 = Circulo.pedir_radio()
    circulo1 = Circulo(radio1)
    area1 = circulo1.area()
    perimetro1 = circulo1.perimetro()
    print("Círculo 1:")
    print("Área:", area1)
    print("Perímetro:", perimetro1)

    radio2 = Circulo.pedir_radio()
    circulo2 = Circulo(radio2)
    area2 = circulo2.area()
    perimetro2 = circulo2.perimetro()
    print("Círculo 2:")
    print("Área:", area2)
    print("Perímetro:", perimetro2)

except ValueError as e:
    print("Error:", str(e))
except TypeError as e:
    print("Error:", str(e))