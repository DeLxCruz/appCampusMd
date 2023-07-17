import core
import validations
import os
from datetime import date


dictVets = {"data":[]}
showVetselected = ""

def LoadInfoVets():
    global dictVets
    if (core.checkFile("vets.json")):
        dictVets = core.LoadInfo("vets.json")
    else:
        core.crearInfo("vets.json",dictVets)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("pause")
    os.system("clear")
    global showvetselected
    print("╔═══════════════════════════════════════════════╗")
    print("║           ¡GESTIÓN DE VETERIANRIOS!           ║")
    print("╠═══════════════════════════════════════════════╣")
    print("║      Seleccione una opción:                   ║")
    print("║                                               ║")
    print("║    1. Agregar Veterinario                     ║")
    print("║    2. Buscar Veterinario                      ║")
    print("║    3. Mostrar Información de el Veterinario   ║")
    print("║    4. Volver al menú principal                ║")
    print("║                                               ║")
    print("╚═══════════════════════════════════════════════╝")

    try:
        opcion =int(input("-->  "))
    except ValueError:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        MainMenu()

    if (opcion == 1):

        idVet = validateIdVet()
        fullNameVet = validations.validateFullNameVet()
        age = validations.validateAge()
        professionalTitle = 'Doctor en Medicina Veterinaria'
        specialty = chooseSpecialty()
        regisrationDate = str(date.today())

        data = {
            'id': idVet,
            'name': fullNameVet,
            'age': age,
            'professionalTitle': professionalTitle,
            'specialty': specialty,
            'regisration date': regisrationDate,
            'schedule': "",
            'hours': "",
        }
        setSchedule(data)

        core.crearInfo("vets.json",data)
        dictVets["data"].append(data)

                
    elif (opcion == 2):
        showvetselected = searchVet()
    elif (opcion == 3):
        if showvetselected:
            print(showvetselected)
            input('Presione una tecla para continuar... ')
        else:
            print("No se ha seleccionado ningún Veterinario.")
    elif (opcion == 4):
        isCliRun = False
    else:
        print("Opción no válida")
    if (isCliRun):
        MainMenu()

def searchVet():
    while True:
        os.system("clear")
        print("╔═══════════════════════════════════════════════╗")
        print("║           ¡GESTIÓN DE VETERIANRIOS!           ║")
        print("╠═══════════════════════════════════════════════╣")
        print("║      Seleccione una opción:                   ║")
        print("║                                               ║")
        print("║    [N] Buscar Veterinario por Nombre          ║")
        print("║    [E] Buscar Veterinario por Especialidad    ║")
        print("║    [V] Volver al Menú Principal               ║")
        print("║                                               ║")
        print("╚═══════════════════════════════════════════════╝")
        option = input("-->  ")
        if (option == 'N' or option == 'n'):
            nameWanted = input("Ingrese el Nombre del Veterinario: ").upper()
            nameFound = False
            for i,j in enumerate(dictVets["data"]):
                if (j['name'] == nameWanted):
                    print(f"{i + 1} Nombre: {j['name']} - Tipo: {j['type']} - Dueño: {j['owner']}")
                    selectedPatient = int(input("Seleccione el Veterinario: "))
                    selectedPatient -= 1
                    if selectedPatient >= 0 and selectedPatient <= len(dictVets["data"]):
                        infoPatient = f"Nombre: {dictVets['data'][selectedPatient]['name']} - Tipo: {dictVets['data'][selectedPatient]['type']} - Dueño: {dictVets['data'][selectedPatient]['owner']} - Raza: {dictVets['data'][selectedPatient]['breed']} - Edad: {dictVets['data'][selectedPatient]['age']}"
                        nameFound = True
                        return infoPatient
                    else:
                        print("Opción no válida")
                        searchVet()
                    
            if (not nameFound):
                print("No se encontró ningún Veterinario con el nombre especificado.")
            input("Presione una tecla para continuar...")
            break
        elif (option == 'E' or option == 'e'):
            breedWanted = input("Ingrese la Raza del Veterinario: ").upper()
            breedFound = False
            for i in dictVets["data"]:
                    if (j['breed'] == breedWanted):
                        print(f"Nombre: {i['name']} - Tipo: {i['type']} - Dueño: {i['owner']}")
                        selectedPatient = int(input("Seleccione el Veterinario: "))
                        selectedPatient -= 1
                        if selectedPatient >= 0 and selectedPatient <= len(dictVets["data"]):
                                infoPatient = f"Nombre: {dictVets['data'][selectedPatient]['name']} - Tipo: {dictVets['data'][selectedPatient]['type']} - Dueño: {dictVets['data'][selectedPatient]['owner']} - Raza: {dictVets['data'][selectedPatient]['breed']} - Edad: {dictVets['data'][selectedPatient]['age']}"
                                breedFound = True
                                return infoPatient
                        else:
                            print("Opción no válida")
                            searchVet()

                    if (not breedFound):
                        print("No se encontró ningún Veterinario con la raza especificada.")
                    input("Presione una tecla para continuar...")
                    break

        elif (option == 'V' or option == 'v'):
                break
        else:
            print("Opción no válida")
            searchVet()

def validateIdVet():
    while True:
        idVet = input("Ingrese el ID del Veterinario: ")
        for i in dictVets["data"]:
            if idVet == i['id']:
                print("El ID ya existe, ingrese uno nuevo")
                break
            elif not idVet.isdigit():
                print("El ID debe ser un número entero válido")
                break
            elif int(idVet) < 0:
                print("El ID debe ser positivo")
                break
        else:
            return idVet

def chooseSpecialty():
    specialties = ['Cirugía veterinaria', 'Oncología Veterinaria', 'Dermatología Veterinaria', 'Medicina Interna Veterinaria', 'Oftalmología Veterinaria', 'Odontología Veterinaria', 'Neurología Veterinaria', 'Cardiología Veterinaria', 'Anestesiología Veterinaria', 'Rehabilitación y fisioterapia veterinaria', 'Nutrición Veterinaria', 'Etología Veterinaria']

    for i in range(len(specialties)):
        print(f"{i + 1}. {specialties[i]}")

    while True:
        try:
            option = int(input("Seleccione la especialidad: "))
            if option >= 1 and option <= len(specialties):
                print(f"La especialidad seleccionada es: {specialties[option - 1]}")
                return specialties[option - 1]
            else:
                print("Opción no válida")
        except ValueError:
            print("Opción no válida")

def setSchedule(data):
    morning = "maniana"
    afternoon = "tarde"
    morningHours = ["8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30"]
    afternoonHours = ["14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", '17:30']

    while True:
        print("Seleccione el horario: ")
        print("1. Mañana")
        print("2. Tarde")
        try:
            option = int(input("-->  "))
            if option == 1:
                data["schedule"] = morning
                data["hours"] = morningHours
                break
            elif option == 2:
                data["schedule"] = afternoon
                data["hours"] = afternoonHours
                break
        except ValueError:
            print("Opción no válida")