lista = []
num_impares = 1
while len(lista) < 15:
    lista.append(num_impares)
    num_impares += 2
flotantes_repetidos = [1.1, 3.3, 5.5]
lista.append(flotantes_repetidos)
lista.insert(3,"String")
del lista[3]
print(lista)