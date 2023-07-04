class DatosPersonales:
    def __init__(self):
        self.datos = {}

    def ingresar_nombre_apellido(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        self.datos["Nombre"] = nombre
        self.datos["Apellido"] = apellido

    def ingresar_edad(self):
        edad = int(input("Ingrese su edad: "))
        self.datos["Edad"] = edad

    def imprimir_resultados(self):
        print("Datos personales:")
        for clave, valor in self.datos.items():
            print(f"{clave}: {valor}")


# Ejemplo de uso
persona = DatosPersonales()
persona.ingresar_nombre_apellido()
persona.ingresar_edad()
persona.imprimir_resultados()