class ReversorDeCadenas:
    def revertir_cadena(self, cadena):
        palabras = cadena.split()
        palabras_revertidas = palabras[::-1]
        cadena_revertida = " ".join(palabras_revertidas)
        return cadena_revertida


# Ejemplo de uso
reversor = ReversorDeCadenas()

cadena1 = "Hola Pythonista, seguimos adelante"
resultado1 = reversor.revertir_cadena(cadena1)
print("Resultado 1:", resultado1)

cadena2 = "Esta es otra cadena de prueba"
resultado2 = reversor.revertir_cadena(cadena2)
print("Resultado 2:", resultado2)