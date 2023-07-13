import patients
import appointments
import vets

if __name__ == "__main__":
    isActivate = True
    opTion = 0
    while (isActivate):
        print("╔═════════════════════════════════════════════╗")
        print("║   ¡ADMINISTRACIÓN DEL CENTRO VETERINARIO!   ║")
        print("╠═════════════════════════════════════════════╣")
        print("║        Seleccione una opción:               ║")
        print("║                                             ║")
        print("║      1. Gestión de Pacientes                ║")
        print("║      2. Gestión de Veterinarios             ║")
        print("║      3. Gestión de Citas Médicas            ║")
        print("║      4. Salir                               ║")
        print("║                                             ║")
        print("╚═════════════════════════════════════════════╝")
        opcion =int(input("-->"))
        if (opcion == 1):
            patients.LoadInfoPatients()
            patients.MainMenu()
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            isActivate = False