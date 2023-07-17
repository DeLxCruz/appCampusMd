import core
import validations
import vets
import patients
import datetime
import os

dictAppointments = {"data":[]}
dictVets = vets.dictVets
dictPatients = patients.dictPatients
contId = 0
showAppointmentselected = ""

def LoadInfoAppointments():
    global dictAppointments
    if (core.checkFile("appointments.json")):
        dictAppointments = core.LoadInfo("appointments.json")
    else:
        core.crearInfo("appointments.json",dictAppointments)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("pause")
    os.system("clear")
    global contId
    global showAppointmentselected
    print("╔═══════════════════════════════════════════╗")
    print("║            ¡GESTIÓN DE CITAS!             ║")
    print("╠═══════════════════════════════════════════╣")
    print("║      Seleccione una opción:               ║")
    print("║                                           ║")
    print("║    1. Agregar Cita                        ║")
    print("║    2. Cancelar Cita                       ║")
    print("║    3. Consultar Citas Por Fecha           ║")
    print("║    4. Consultar Citas Por Veterinario     ║")
    print("║    5. Volver al menú principal            ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    try:
        opcion =int(input("-->  "))
    except ValueError:
        print("Opción no válida. Por favor seleccione una opción válida.")
        MainMenu()
        
    if (opcion == 1):
        if (len(dictAppointments['data']) >=1):
            contId = dictAppointments['data'][-1]['id']+1
        else:
            contId = 1

        dateAppointment = validateDate()
        timeAppointment = validateTime()
        assignedVet = assignVet()
        patientId = searchPatient()

        data = {
            'id': contId,
            'date': dateAppointment,
            'time': timeAppointment,
            'assignedVet': {
                'id': assignedVet['id'],
                'name': assignedVet['name'],
            },
            'patientId': patientId,
        }

        if assignedVet['id'] in dictVets['data']:
            vet_data = dictVets['data'][assignedVet['id']]
        if 'calendar' not in vet_data:
            vet_data['calendar'] = []
        vet_data['calendar'].append({
            'id': data['id'],
            'date': data['date'],
            'time': data['time']
        })

        core.EditarData("vets.json",dictVets)
        core.crearInfo("appointments.json",data)
        dictAppointments["data"].append(data)


                
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        if showAppointmentselected != "":
            print(showAppointmentselected)
            input('Presione una tecla para continuar... ')
        else:
            print("No se ha seleccionado ningún Citas.")
            input('Presione una tecla para continuar... ')
    elif (opcion == 4):
        isCliRun = False
    else:
        print("Opción no válida")
    if (isCliRun):
        MainMenu()

def validateDate():

    while True:
        fecha_str = input("Ingrese una fecha (formato: DD/MM/AAAA): ")

        try:
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha.strftime("%d/%m/%Y")
        except ValueError:
                print("Fecha inválida. Intente nuevamente.")

def validateTime():
    while True:
        hora_str = input("Ingrese una hora (formato: HH:MM): ")

        try:
            hora = datetime.datetime.strptime(hora_str, "%H:%M").time()
            return hora.strftime("%H:%M")
        except ValueError:
                print("Hora inválida. Intente nuevamente.")

def assignVet():
    while True:
        global vetId
        try:
            vetId = input("Ingrese el ID del veterinario: ")
            if vetId in dictVets["data"]:
                print("Veterinario encontrado.")
                vetName = dictVets["data"][vetId]['name']
                print("Nombre: " + vetName)
                input('Presione una tecla para continuar... ')
                return {'id': vetId, 'name': vetName}
            else:
                print("Veterinario no encontrado. Intente nuevamente.")
        except ValueError:
            print("ID no válido. Intente nuevamente.")


def searchPatient():
    while True:
        patientId = input("Ingrese el ID del paciente: ")

        try:
            patientId = int(patientId)
            if patientId in dictPatients:
                print("Paciente encontrado.")
                print('Se ha agendado la cita con el veterinario ' + dictVets[vetId]['name'] + '.')
                input('Presione una tecla para continuar... ')
                return patientId
            else:
                print("Paciente no encontrado. Intente nuevamente.")
        except ValueError:
            print("ID no válido. Intente nuevamente.")