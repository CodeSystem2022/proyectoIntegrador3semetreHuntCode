import webbrowser
import wget


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
def mostrar_menu_leyes():
    print("*** LEYES ****")
    print("1. Ley 19587/1972")
    print("2. Ley 24557/1995")
    print("3. Salir")
    print("*********")

def opcion_leyes_1():
    print("Ley de Higiene y Seguridad en el Trabajo. Condiciones de higiene seguridad que debe cumplir cualquier actividad en todo el territorio de la República Argentina.")
    # Aquí agregamos la opción 1 que es la ley 19587/1972

def opcion_leyes_2():
    print("Ley de prevención de riesgos del trabajo. Tiene por objetivo reducir la siniestralidad laboral a través de la prevención de los riesgos derivados del trabajo, y reparar los daños derivados de accidentes de trabajo y de enfermedades profesionales. Obligatoriedad de afiliación a una Aseguradora de Riesgos del Trabajo (ART) o de Autoasegurarse")
    # Aquí agregamos la opción 2, que es la ley 24557/1995

def mostrar_menu_resoluciones():
    print("*** RESOLUCIONES ****")
    print("1. Resolución SRT 230/2003")
    print("2. Resolución 299/2011 SRT")
    print("3. Resolución SRT 415/2002")
    print("4. Resolución SRT 295/2003")
    print("5. Resolución SRT 592/2004")
    print("6. Resolución SRT 103/2005")
    print("7. Resolución SRT 801/2005")
    print("8. Resolución SRT 463/2009")
    print("9. Resolución SRT 37/2010")
    print("10. Resolución SRT 20/2018")
    print("11. Salir")
    print("*********")

def opcion_resoluciones_1():
    print("Obligación de los empleadores asegurados y autoasegurados de denunciar todos los accidentes de trabajo y enfermedades profesionales a su ART y a la SRT. Obligación de investigar los accidentes mortales, enfermedades profesionales y los accidentes graves.")
    # Aquí cargamos la opicón 1, Resolución SRT 230/2003

def opcion_resoluciones_2():
    print("Adóptense las reglamentaciones que procuren la provisión de elementos de protección personal confiables a los trabajadores. (B.O. 30/03/2011).")
    # Aquí cargamos la opción 2, Resolución 299/2011

def opcion_resoluciones_3():
    print(" Registro de sustancias y agentes cancerígenos.")
    # Aquí cargamos la opción 3, Resolución 415/2002

def opcion_resoluciones_4():
    print(" Especificaciones técnicas sobre ergonomía, levantamiento manual de cargas y radiaciones. Anexo I (ergonomía) y Anexo II (radiaciones).")
    # Aquí cargamos la opción 4, Resolución 295/2003

def opcion_resoluciones_5():
    print("Reglamento para la Ejecución de Trabajos con Tensión.")
    # Aquí cargamos la opción 5, Resolución 592/2004

def opcion_resoluciones_6():
    print(" Sistemas de Gestión de la Seguridad y la Salud en el trabajo.")
    # Aquí cargamos la opción 6, Resolución 103/2005

def opcion_resoluciones_7():
    print(" Obligatoriedad del Sistema Globalmente Armonizado (SGA) de Clasificación y Etiquetado de Productos Químicos: enfoque internacional para la comunicación de peligros, clasificación de los peligros químicos, enfoque estandarizado para elementos de etiquetado y fichas de datos de seguridad.")
    # Aquí cargamos la opción 7, Resolución 801/2005

def opcion_resoluciones_8():
    print("Confección y presentación ante la ART del Relevamiento General de Riesgos Laborales (RGRL) sobre el estado de cumplimiento de la normativa vigente por parte del establecimiento.")
    # Aquí cargamos la opción 8, Resolución 463/2009, SRT 529/2009 y SRT 741/2010.

def opcion_resoluciones_9():
    print("Declaración de Agentes de Riesgo. Anualmente todo establecimiento está obligado a presentar el relevamiento de Agentes de Riesgos Laborales (RAR) a su Aseguradora de Riesgos de Trabajo (ART), a través del cual se informa a la misma el personal que se encuentra expuesto a algún agente de riesgo.")
    # Aquí cargamos la opción 9, Resolución SRT 37/2010 y SRT 81/2019

def opcion_resoluciones_10():
    print(" Programa de Prevención Específico para Pequeñas y Medianas Empresas (PYMES). Modificada por Res. SRT 48/2019.")
    # Aquí cargamos la opción 10, Resolución  SRT 20/2018 SRT

def mostrar_menu_decretos():
    print("*** DECRETOS ****")
    print("1. Decreto 1338/1996")
    print("2. Decreto 911/1996")
    print("3. Decreto 617/1997")
    print("4. Decreto 249/2007")
    print("5. Salir")
    print("*********")

def opcion_decretos_1():
    print("Regula los servicios de Medicina y de Higiene y Seguridad en el Trabajo, de carácter preventivo.")
    # Aquí cargamos la opción 1, Decreto 1338/1996

def opcion_decretos_2():
    print("Reglamento de Higiene y Seguridad para la Industria de la Construcción. Y Resol. SRT 231/96.")
    # Aquí cargamos la opción 2, Decreto 911/1996

def opcion_decretos_3():
    print("Reglamento en Higiene y Seguridad en el Trabajo para la Actividad Agraria.")
    # Aquí cargamos la opción 3, Decreto 617/1997

def opcion_decretos_4():
    print("Reglamento en Higiene y Seguridad en el Trabajo para la Actividad Minera.")
    # Aquí cargamos la opción 4, Decreto 249/2007

while True:
    mostrar_menu_leyes()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        opcion_leyes_1()
    elif opcion == "2":
        opcion_leyes_2()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

while True:
    mostrar_menu_resoluciones()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        opcion_resoluciones_1()
    elif opcion == "2":
        opcion_resoluciones_2()
    elif opcion == "3":
        opcion_resoluciones_3()
    elif opcion == "4":
        opcion_resoluciones_4()
    elif opcion == "5":
        opcion_resoluciones_5()
    elif opcion == "6":
        opcion_resoluciones_6()
    elif opcion == "7":
        opcion_resoluciones_7()
    elif opcion == "8":
        opcion_resoluciones_8()
    elif opcion == "9":
        opcion_resoluciones_9()
    elif opcion == "10":
        opcion_resoluciones_10()
    elif opcion == "11":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

while True:
    mostrar_menu_decretos()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        opcion_decretos_1()
    elif opcion == "2":
        opcion_decretos_2()
    elif opcion == "3":
        opcion_decretos_3()
    elif opcion == "4":
        opcion_decretos_4()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")


def mostrar_menu():
    print("*** MENÚ ****")
    print("1. Ver video de YouTube")
    print("2. Descargar archivo PDF")
    print("3. Salir")
    print("**********")

def reproducir_video():
    video_url = "https://youtu.be/fIdyuPmQiJo"  #Cargando VIDEO SOBRE CAPACITACIÓN - INDUCCIÓN A HIGIENE Y SEGURIDAD - RIESGOS Y ACCIDENTES
    webbrowser.open(video_url)

def descargar_pdf():
    pdf_url = "https://documentosboletinoficial.buenosaires.gob.ar/publico/PE-DIS-MAYEPGC-UGGOAALUPEEI-55-19-ANX.pdf"  # PDF  QUE MUESTRA LA CAPACITACIONES DE HIGIENE Y SEGURIDAD
    output_file = "archivo.pdf"  # Nombre del archivo de salida

    # Descargar el archivo PDF
    wget.download(pdf_url, out=output_file)
    print("Descarga completa")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        reproducir_video()
    elif opcion == "2":
        descargar_pdf()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")


