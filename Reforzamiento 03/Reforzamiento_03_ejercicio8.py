class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        contacto = {
            "Nombre": nombre,
            "Teléfono": telefono,
            "Email": email,
            "DNI": dni
        }
        self.contactos.append(contacto)
        print("Contacto agregado exitosamente.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print("Nombre:", contacto["Nombre"])
                print("Teléfono:", contacto["Teléfono"])
                print("Email:", contacto["Email"])
                print("DNI:", contacto["DNI"])
                print("")

    def buscar_contacto_por_dni(self, dni):
        for contacto in self.contactos:
            if contacto["DNI"] == dni:
                print("Resultado de la búsqueda:")
                print("Nombre:", contacto["Nombre"])
                print("Teléfono:", contacto["Teléfono"])
                print("Email:", contacto["Email"])
                print("DNI:", contacto["DNI"])
                return
        print("No se encontró ningún contacto con el DNI especificado.")

# Ejemplo de uso
agenda = Agenda()
agenda.agregar_contacto("Juan Pérez", "123456789", "juan@example.com", "12345678")
agenda.agregar_contacto("María López", "987654321", "maria@example.com", "87654321")
agenda.mostrar_contactos()

agenda.buscar_contacto_por_dni("12345678")
agenda.buscar_contacto_por_dni("87654321")
agenda.buscar_contacto_por_dni("99999999")