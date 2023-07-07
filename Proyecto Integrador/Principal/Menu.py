from Controladores.Archivo_CRUD import crear_registro, actualizar_registro, obtener_registros, obtener_registro_por_id, eliminar_registro

while True:
    # Mostrar el menú
    print("------ MENÚ ------")
    print("1. Crear Registro de persona")
    print("2. Obtener registros")
    print("3. Obtener registros por id")
    print("4. Actualizar registro")
    print("5. Eliminar registro")
    print("6. Salir")

    # Pedir al usuario que ingrese una opción
    opcion = input("Selecciona una opción: ")

    # Evaluar la opción ingresada y llamar a la función correspondiente
    if opcion == "1":
        #idIndividuo = int(input("Ingrese el id de la persona: "))
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        contrasenia = input("Ingrese el contraseña de la persona: ")
        email = input("Ingrese el email de la persona: ")
        
        crear_registro(nombre, apellido, contrasenia, email)
    elif opcion == "2":
        print(obtener_registros())

    elif opcion == "3":
        idIndividuo = input("Ingrese el id de la persona a buscar: ")
        print(obtener_registro_por_id(idIndividuo))

    elif opcion == "4":
        idIndividuo = int(input("Ingrese el id de la persona a modificar: "))
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        contrasenia = int(input("Ingrese la contraseña de la persona: "))
        email = input("Ingrese el email de la persona: ")
        actualizar_registro(idIndividuo, nombre, apellido, contrasenia, email)

    elif opcion == "5":
        eliminar_registro(int(input("Ingrese el id de la persona que desea dar de baja: ")))

    elif opcion == "6":
        exit()
        break  # Salir del bucle while y finalizar el programa
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.\n")
