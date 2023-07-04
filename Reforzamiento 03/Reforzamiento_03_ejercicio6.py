class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Nota Final:", self.nota_final)

    def mensaje_aprobacion(self):
        if self.nota_final >= 11:
            mensaje = "¡Aprobado!"
        else:
            mensaje = "Reprobado"
        print(f"{self.nombre} ha obtenido una nota final de {self.nota_final}. {mensaje}")

# Ejemplo de uso
alumno1 = Alumno("Juan", 18, 15)
alumno1.imprimir_datos()
alumno1.mensaje_aprobacion()

alumno2 = Alumno("María", 20, 8)
alumno2.imprimir_datos()
alumno2.mensaje_aprobacion()

alumno3 = Alumno("Pedro", 19, 12)
alumno3.imprimir_datos()
alumno3.mensaje_aprobacion()