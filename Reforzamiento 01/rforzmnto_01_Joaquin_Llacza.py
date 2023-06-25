"""
1.  El valor de ‘¡HI TuNombre!’ imprimirlo por pantalla, el texto debe ser un string y deberás guardarlo en una variable llamada mi_saludo. Tu nombre debe estar en otra variable.
2. Crea una variable tipo int. Luego, multiplica por 10 y restarle 10. Debes hacer todo estoo en dos pasos. Finalmente mostrar el resultado por pantalla.
3.  Crear una variable tipo string y poder luego sumarla con otra variable tipo int, para esto convertir una de las variables. Mostrar la suma en pantalla.
4. Hallar el volumen de una esfera, cada dato requerido para hallar el volumen debe estar en una variable. Mostrar el volumen por pantalla.
5. Crear un programa que partiendo de un sueldo en una variable, sepamos si es par o impar. Utilizar módulo y condicional.
6.  Calcular la media de 5 datos (floats), cada dato debe estar en una variable y la media también. Mostrar el resultado en pantalla.
7. De 3 números asignados (tú los propones) a 3 variables se pide hallar la suma de los valores de los módulos con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la suma.
8. Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con una lista vacía y otra con una lista vacía.
9. Elevar al exponente de 4 un número que su valor estará asignado a una variable y luego restar este mismo valor multiplicado por dos (usar pow). Mostrar el resultado en pantalla.
10. Crear un diccionario con los siguientes key: nombre, carrera, edad y año de nacimiento, mostrar en pantalla el valor de este diccionario.
11. Identificar que tipo de dato se obtiene al elevar un número a la exponente de 5 y luego dividirlo por 10. Mostrar el resultado en pantalla.
"""

ejercicio1 = "Ejercicio 1"
TuNombre = "Joaquin Llacza"
mi_saludo =f"¡HI {TuNombre}"
print(ejercicio1)
print(mi_saludo)
ejercicio2 = "Ejercicio 2"
variable_int = 10
operacion = 10 * 10 - 10
print(ejercicio2)
print(operacion)
ejercicio3 = "Ejercicio 3"
variable1_int = 50
variable1_str = "40"
int_int = variable_int + int(variable1_str)
str_str = variable1_str + str(variable1_int)
print(ejercicio3)
print(int_int)
print(str_str)
ejercicio4 = "Ejercicio 4"
volumen_esfera = 4/3*3.14*(5**3)
print(ejercicio4)
print(volumen_esfera)
ejercicio5 = "Ejercicio 5"
print(ejercicio5)
numero = int(input("Escriba un número: "))
if numero %2 == 0:
    print("El número es par")
else:
    print("El número es impar")
ejercicio6 = "Ejercicio 6"
print(ejercicio6)
dato = 100.234
dato1 = 1230.8329138
dato2 = 213.321321
dato3 = 123.32321
dato4 = 2193.88282
print("La media es: " + str(dato+dato1+dato2+dato3+dato4/5))
ejercicio7 = "Ejercicio 7"
numero = 100
numero1 = 200
numero2 = 300
suma = numero + 3
suma1 = numero1 + 5
suma2 = numero2 + 7
print(ejercicio7)
print("La suma número 1 es: ", suma, "\nLa suma número 2 es: ", suma1, "\nLa suma número 3 es: ", suma2)
ejercicio8 = "Ejercicio 8"
print(ejercicio8)
lista = []
lista1 = [100, 200, 300]
if len(lista) == 0:
    print("La lista está vacía.")
else:
    print("La lista no está vacía.")
if len(lista1) == 0:
    print("La lista está vacía.")
else:
    print("La lista no está vacía.")
ejercicio9 = "Ejercicio 9"
print(ejercicio9)
numero5 = 100
resultado_numero5 = pow(numero5, 4)
resultado_final = resultado_numero5 - (numero5 * 2)
print("El resultado es:", resultado_final)
ejercicio10 = "Ejercicio 10"
print(ejercicio10)
datos = {
    "nombre": "Joaquín",
    "carrera": "Ingeniería en Ciencia de Datos e Inteligencia Artificial",
    "edad": 20,
    "año de nacimiento": 2002
}
print(datos)
ejercicio11 = "Ejercicio 11"
numero6 = 1000
resultado = (numero6 ** 5) / 10
print(ejercicio11)
print("El resultado es:", resultado)