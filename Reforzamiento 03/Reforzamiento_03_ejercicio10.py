import mi_modulo


nombres, apellidos = mi_modulo.ingresar_nombres_apellidos()
print("Nombres:", nombres)
print("Apellidos:", apellidos)


tipo_seguro = mi_modulo.pedir_tipo_seguro()
print("Tipo de seguro:", tipo_seguro)


if mi_modulo.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")