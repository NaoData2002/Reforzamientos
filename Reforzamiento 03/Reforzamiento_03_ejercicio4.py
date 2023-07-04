def mostrar_cuadrados_entre_numeros():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    for numero in range(numero1 + 1, numero2):
        cuadrado = numero ** 2
        print(f"El cuadrado de {numero} es: {cuadrado}")


# Ejemplo de uso
mostrar_cuadrados_entre_numeros()