class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo: "))

    def calcular_impuesto(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.1
            return impuesto
        else:
            return 0

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)
        print("Impuesto a pagar:", self.calcular_impuesto())

# Ejemplo de uso
empleado = Empleado()
empleado.mostrar_informacion()
