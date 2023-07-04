class Calculadora:
    def __init__(self):
        self.resultado = 0

    def ingresar_numero(self):
        num = int(input("Ingrese un valor numérico: "))
        self.resultado = num

    def calcular_cubo(self):
        cubo = self.resultado ** 3
        return cubo

    def calcular_cuadrado_del_cubo(self):
        cubo = self.calcular_cubo()
        cuadrado_del_cubo = cubo ** 2
        return cuadrado_del_cubo


# Ejemplo de uso
calculadora = Calculadora()
calculadora.ingresar_numero()
cubo = calculadora.calcular_cubo()
cuadrado_del_cubo = calculadora.calcular_cuadrado_del_cubo()

print("El cubo del número ingresado es:", cubo)
print("El cuadrado del cubo es:", cuadrado_del_cubo)