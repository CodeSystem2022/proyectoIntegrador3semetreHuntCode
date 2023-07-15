def mostrar_menu():
    print("Bienvenido al sistema:")
    print("1. Registrarse")
    print("2. Ingresar")
    print("3. Salir")

def registrar():
    # Registro de usuario

    print("Registro de usuario")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    email = input("Ingresa tu correo electrónico: ")
    password = input("Ingresa tu contraseña: ")


    print("¡Registro exitoso!")


def ingresar():
    # ingresar al sistema


    nombre = input("Ingrese su nombre: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre in usuarios and usuarios[nombre] == contraseña:
        print("¡Inicio de sesión exitoso!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")


usuarios = {}

opciones = {
    "1": registrar,
    "2": ingresar,
}

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion in opciones:
        opciones[opcion]()
    elif opcion == "3":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
