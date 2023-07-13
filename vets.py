import core
import validations
import os

dictVets = {"data":[]}
showVetselected = ""

def LoadInfovets():
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
    opcion =int(input("-->  "))
    if (opcion == 1):

        idVet = validations.validateIdVet()
        fullNameVet = validations.validateFullNameVet()
        age = validations.validateAge()
        professionalTitle = True
        specialty = True

        data = {
            'id': idVet,
            'name': fullNameVet,
            'age': age,
            'professionalTitle': professionalTitle,
            'specialty': specialty,
            'clinicalHistory': []
        }

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
    if (isCliRun):
        MainMenu()

def searchVet():
    while True:
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

def 
