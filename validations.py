def validateAge():
    while True:
        age = input("Ingrese la Edad del paciente: ")
        if not age.isdigit():
            print("La edad debe ser un número entero válido")
        elif int(age) < 0:
            print("La edad debe ser positiva")
        else:
            return age


def validateName():
    while True:
        name = input("Ingrese el Nombre del paciente: ").upper()
        if name == "":
            print("El nombre no puede estar vacío")
        else:
            return name

def validateOwner():
    while True:
        owner = input("Ingrese el Nombre del dueño del paciente: ").upper()
        if owner == "":
            print("El nombre no puede estar vacío")
        else:
            return owner
