import core
import validations
import os

dictPatients = {"data":[]}
contId = 0
showPatientSelected = ""

def LoadInfoPatients():
    global dictPatients
    if (core.checkFile("patients.json")):
        dictPatients = core.LoadInfo("patients.json")
    else:
        core.crearInfo("patients.json",dictPatients)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("pause")
    os.system("clear")
    global contId
    global showPatientSelected
    print("╔═══════════════════════════════════════════╗")
    print("║           ¡GESTIÓN DE PACIENTES!          ║")
    print("╠═══════════════════════════════════════════╣")
    print("║      Seleccione una opción:               ║")
    print("║                                           ║")
    print("║    1. Agregar Paciente                    ║")
    print("║    2. Buscar Paciente                     ║")
    print("║    3. Mostrar Información de el Paciente  ║")
    print("║    4. Volver al menú principal            ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    try:
        opcion =int(input("-->  "))
    except ValueError:
        print("Opción no válida. Por favor seleccione una opción válida.")
        MainMenu()
        
    if (opcion == 1):
        if (len(dictPatients['data']) >=1):
            contId = dictPatients['data'][-1]['id']+1
        else:
            contId = 1

        name = validations.validateName()
        age = validations.validateAge()
        owner = validations.validateOwner()

        animalType = typeOfPatient()

        data = {
            'id': contId,
            'name': name,
            'type': animalType,
            'breed': breedOfPatient(animalType),
            'age': age,
            'owner': owner,
            'clinicalHistory': []
        }

        core.crearInfo("patients.json",data)
        dictPatients["data"].append(data)

                
    elif (opcion == 2):
        showPatientSelected = searchPatient()
    elif (opcion == 3):
        if showPatientSelected != "":
            print(showPatientSelected)
            input('Presione una tecla para continuar... ')
        else:
            print("No se ha seleccionado ningún paciente.")
            input('Presione una tecla para continuar... ')
    elif (opcion == 4):
        isCliRun = False
    else:
        print("Opción no válida")
    if (isCliRun):
        MainMenu()

def searchPatient():
    while True:
        os.system("clear")
        print("╔═══════════════════════════════════════════╗")
        print("║          ¡BÚSQUEDA DE PACIENTES!          ║")
        print("╠═══════════════════════════════════════════╣")
        print("║      Seleccione una opción:               ║")
        print("║                                           ║")
        print("║    [N] Buscar Paciente por Nombre         ║")
        print("║    [R] Buscar Paciente por Raza           ║")
        print("║    [V] Volver al Menú Principal           ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        
        try:
            option = input("-->  ")
        except ValueError:
            print("Opción no válida. Por favor seleccione una opción válida.")
            input("Presione ENTER para continuar...")
        
        if (option == 'N' or option == 'n'):
            nameWanted = input("Ingrese el Nombre del paciente: ").upper()
            nameFound = False
            for i,j in enumerate(dictPatients["data"]):
                if (j['name'] == nameWanted):
                    print(f"{i + 1} Nombre: {j['name']} - Tipo: {j['type']} - Dueño: {j['owner']}")
                    selectedPatient = int(input("Seleccione el paciente: "))
                    selectedPatient -= 1
                    if selectedPatient >= 0 and selectedPatient <= len(dictPatients["data"]):
                        infoPatient = f"Nombre: {dictPatients['data'][selectedPatient]['name']} - Tipo: {dictPatients['data'][selectedPatient]['type']} - Dueño: {dictPatients['data'][selectedPatient]['owner']} - Raza: {dictPatients['data'][selectedPatient]['breed']} - Edad: {dictPatients['data'][selectedPatient]['age']}"
                        nameFound = True
                        return infoPatient
                    else:
                        print("Opción no válida")
                        searchPatient()
                    
            if (not nameFound):
                print("No se encontró ningún paciente con el nombre especificado.")
            input("Presione una tecla para continuar...")
            break
        elif (option == 'R' or option == 'r'):
            breedWanted = input("Ingrese la Raza del paciente: ").upper()
            breedFound = False
            for i in dictPatients["data"]:
                    if (j['breed'] == breedWanted):
                        print(f"Nombre: {i['name']} - Tipo: {i['type']} - Dueño: {i['owner']}")
                        selectedPatient = int(input("Seleccione el paciente: "))
                        selectedPatient -= 1
                        if selectedPatient >= 0 and selectedPatient <= len(dictPatients["data"]):
                                infoPatient = f"Nombre: {dictPatients['data'][selectedPatient]['name']} - Tipo: {dictPatients['data'][selectedPatient]['type']} - Dueño: {dictPatients['data'][selectedPatient]['owner']} - Raza: {dictPatients['data'][selectedPatient]['breed']} - Edad: {dictPatients['data'][selectedPatient]['age']}"
                                breedFound = True
                                return infoPatient
                        else:
                            print("Opción no válida")
                            searchPatient()

                    if (not breedFound):
                        print("No se encontró ningún paciente con la raza especificada.")
                    input("Presione una tecla para continuar...")
                    break

        elif (option == 'V' or option == 'v'):
                break
        else:
            print("Opción no válida")
            searchPatient()

def typeOfPatient():
    types = ['Perro', 'Gato', 'Ave', 'Reptil']

    for i, j in enumerate(types):
        print(f'{i+1}. {j}')

    selectType = int(input("Seleccione el tipo de animal: "))

    if (selectType >= 1 and selectType <=len(types)):
        saveType = types[selectType-1]
        print(f'El tipo de animal seleccionado es: {saveType}')
        return saveType
    else:
        print("Opción no válida")
        return typeOfPatient()

def breedOfPatient(saveType):
    dogBreeds = ['Labrador', 'Pug', 'Bulldog', 'Chihuahua', 'Pastor Alemán', 'Golden Retriever', 'Beagle', 'Poodle', 'Rottweiler', 'Boxer']
    catBreeds = ['Siamés', 'Maine', 'Persa', 'Ragdoll', 'Bengala', 'Siberiano', 'Abisinio', 'Burmés', 'Bosque de Noruega', 'Exótico']
    birdBreeds = ['Canario', 'Periquito', 'Cacatúa', 'Loro', 'Agapornis', 'Guacamayo', 'Cotorra', 'Ninfas', 'Inseparable', 'Diamante Mandarín']
    reptileBreeds = ['Tortuga', 'Iguana', 'Serpiente', 'Lagarto', 'Cocodrilo', 'Tortuga de agua', 'Tortuga de tierra', 'Tortuga de caja', 'Tortuga de orejas rojas', 'Tortuga de orejas amarillas']

    if (saveType == 'Perro'):
        for i, j in enumerate(dogBreeds):
            print(f'{i+1}. {j}')

        selectBreed = int(input("Seleccione la raza del perro: "))

        if (selectBreed >= 1 and selectBreed <=len(dogBreeds)):
            saveBreed = dogBreeds[selectBreed-1]
            print(f'La raza seleccionada es: {saveBreed}')
            return saveBreed
        else:
            print("Opción no válida")
            breedOfPatient(saveType)

    elif (saveType == 'Gato'):
        for i, j in enumerate(catBreeds):
            print(f'{i+1}. {j}')
        
        selectBreed = int(input("Seleccione la raza del gato: "))

        if (selectBreed >= 1 and selectBreed <=len(catBreeds)):
            saveBreed = catBreeds[selectBreed-1]
            print(f'La raza seleccionada es: {saveBreed}')
            return saveBreed
        else:
            print("Opción no válida")
            breedOfPatient(saveType)

    elif (saveType == 'Ave'):
        for i, j in enumerate(birdBreeds):
            print(f'{i+1}. {j}')
        
        selectBreed = int(input("Seleccione la raza del ave: "))

        if (selectBreed >= 1 and selectBreed <=len(birdBreeds)):
            saveBreed = birdBreeds[selectBreed-1]
            print(f'La raza seleccionada es: {saveBreed}')
            return saveBreed
        else:
            print("Opción no válida")
            breedOfPatient(saveType)
        
    elif (saveType == 'Reptil'):
        for i, j in enumerate(reptileBreeds):
            print(f'{i+1}. {j}')
        
        selectBreed = int(input("Seleccione la raza del reptil: "))

        if (selectBreed >= 1 and selectBreed <=len(reptileBreeds)):
            saveBreed = reptileBreeds[selectBreed-1]
            print(f'La raza seleccionada es: {saveBreed}')
            return saveBreed
        else:
            print("Opción no válida")
            breedOfPatient(saveType)