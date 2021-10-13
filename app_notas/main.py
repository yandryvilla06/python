from usuarios import acciones
""" Importamos de nuestro paquete usuarios el modulo acciones"""

opc = int(
    input(
        f"Bienvenido al asistente Notas \n Eliga una opcion \n 1-Registro \n 2-Login \n"
    )
)

""" De nuestras acciones nos posiciones en la clase Acciones()"""
accion=acciones.Acciones()

if opc == 1:

    """ Si se elige uno se realiza la accion de login() localizada en nuestro modulo acciones"""
    accion.registro()
    



elif opc == 2:
    """ Si se elige dos se realiza la accion de login() localizada en nuestro modulo acciones"""

    accion.login()
    accion.proximasAcciones()
   

else:

    print("La accion no existe en nuestro sistema ")
