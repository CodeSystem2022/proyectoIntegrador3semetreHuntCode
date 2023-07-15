def login():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    # Verificar las credenciales ingresadas
    if username == "admin" and password == "123789":
        print("Inicio de sesión exitoso.")

    else:
        print("Credenciales inválidas. Inténtelo nuevamente.")


# Llamada a la función de inicio de sesión
login()