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

def validateIdVet():
    while True:
        idVet = input("Ingrese el ID del Veterinario: ")
        if not idVet.isdigit():
            print("El ID debe ser un número entero válido")
        elif int(idVet) < 0:
            print("El ID debe ser positivo")
        else:
            return idVet
        
def validateFullNameVet():
    while True:
        nameVet = input("Ingrese el Nombre del Veterinario: ").upper()
        lastNameVet = input("Ingrese el Apellido del Veterinario: ").upper()
        if nameVet == "" or lastNameVet == "":
            print("El nombre no puede estar vacío")
        elif nameVet.isdigit() or lastNameVet.isdigit():
            print("El nombre no puede ser un número")
        else:
            return f'{nameVet} {lastNameVet}'