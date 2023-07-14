# while True:
#    print("Seleccione el horario: ")
#     print("1. Mañana")
#     print("2. Tarde")
#     try:
#         option = int(input("-->  "))
#         if option == 1:
#             print("Seleccione la hora: ")
#             for i in range(len(morningHours)):
#                 print(f"{i + 1}. {morningHours[i]}")
#             while True:
#                 try:
#                     option = int(input("-->  "))
#                     if option >= 1 and option <= len(morningHours):
#                         print(f"La hora seleccionada es: {morningHours[option - 1]}")
#                         return morningHours[option - 1]
#                     else:
#                         print("Opción no válida")
#                 except ValueError:
#                     print("Opción no válida")
#         elif option == 2:
#             print("Seleccione la hora: ")
#             for i in range(len(afternoonHours)):
#                 print(f"{i + 1}. {afternoonHours[i]}")
#             while True:
#                 try:
#                     option = int(input("-->  "))
#                     if option >= 1 and option <= len(afternoonHours):
#                         print(f"La hora seleccionada es: {afternoonHours[option - 1]}")
#                         return afternoonHours[option - 1]
#                     else:
#                         print("Opción no válida")
#                 except ValueError:
#                     print("Opción no válida")
#         else:   
#             print("Opción no válida")
#     except ValueError:
#         print("Opción no válida")