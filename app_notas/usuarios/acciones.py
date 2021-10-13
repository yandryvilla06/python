
import usuarios.usuario as modelo

class Acciones:

    def registro(self):


        print("De acuerdo vamos a Regisrarte en la app")
        nombre = input("Dime nombre\n")
        apellidos = input("Dime apellidos \n")
        email = input("Dime email \n")
        passwd = input("Dime password \n")

        """ Pedimos al usuario que introduzca por teclado los parametros, en el modulo usuario esta la clase Usuario la cual tiene un constructor 
        estos parametros seran pasados al parametro 
        """
        usuario=modelo.Usuario(nombre,apellidos,email,passwd)

        registro=usuario.registrar()

        
        """Registro me devuelve una lista con 2 parametros en la posicion[0] esta el numero de filas y em la [1] la lsiat del objeto usuario
           
           Lo que me quiere decir registro[0]>=1 es que si hay mas de 1 registro o uno solo , se ha insertado correctamente el objeto en la bdd

        """
        if registro[0]>=1:
            """registro[1].nombre el [1]  es debido a que en la pos[0] estan el numero de filas que devuelve el metodo registro esto devuelve el nombre del usuario """
            print(f"Hola  {registro[1].nombre} te has registrado correctamente")
        else:
            print("error no se ha registrado correctamente")

    def login(self):

        print("Bienvenido al sistema de login")

        try:

            email = input("Dime email \n")
            passwd = input("Dime password \n")

            usuario=modelo.Usuario('','',email,passwd)
            login=usuario.identificar()
       
            if email==login[3]:
                print(f"Bienvenido {login[1]} , te has registrado en el sistema")
                self.proximasAcciones(login)

        except Exception as e:
          
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto , intentalo mas tarde")  



    def proximasAcciones(self,usuario):

        accion=int(input("""
          
          -Acciones de nuestra appNotas \n
          -1 Crear Nota \n
          -2 Mostrar notas \n
          -3 Eliminar nota \n
          -4 Salir \n
         
        """))

        if accion==1:
            pass

        elif accion==2:
            pass

        elif accion==3:
            pass  
        elif accion==4:
            pass

        

                  