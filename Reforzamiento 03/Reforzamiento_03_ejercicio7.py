class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def bonificacion(self):
        bonificacion = self.sueldo * 0.2
        return bonificacion

# Ejemplo de uso
persona1 = Persona("Juan", 25, 50000)
persona1.mostrar_datos()
if persona1.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
print("Bonificación:", persona1.bonificacion())

persona2 = Persona("María", 17, 40000)
persona2.mostrar_datos()
if persona2.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
print("Bonificación:", persona2.bonificacion())