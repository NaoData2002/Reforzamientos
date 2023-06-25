lista = []
for x in range(10):
    valor = float(input("Ingrese el valor: "))
    lista.append(valor)


suma = sum(lista)

media = suma / len(lista)

print("La suma es:", suma)

print("La media es:", media)