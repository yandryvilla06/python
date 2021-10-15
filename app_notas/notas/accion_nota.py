import notas.nota as modelo


class Acciones:


    def crear(self,usuario):
      
        titulo=input("Dime titulo \n")
        descripcion=input("Dime descripcion \n")
       
        nota=modelo.Nota(usuario[0],titulo,descripcion)

        notas=nota.creacion()

        if notas[0]>=1:

            print("Se ha creado la nota exitosamente")
        
        else:

            print("Error en la creacion de la nota")

    
    
    def mostrar(self,usuario):

        nota=modelo.Nota(usuario[0],"","")
        notas_mostradas=nota.listar()

        if notas_mostradas[0]>=1:
              
           
         for nota in notas_mostradas[1]:
           
          #Nota importante no se xq razon si pongo print("id"+nota[0]) me da error
           print("*************************")
           print(f"ID NOTA {nota[0]}")
           print(nota[2])
           print(nota[3])
           print("*************************")
         

        else:

             print("No se pueden mostrar notas xq no hay ")
    
    def eliminar(self):

        id_bus=input("Escriba el ID de la nota a eliminar \n")
        
        filasborradas=modelo.Nota('','','').borrar(id_bus)

        if filasborradas>=1:
            print(f"La nota {id_bus} se ha eliminado exitosamente")
        
        else:

            print(f"Error al borrar la nota {id_bus}")

        





        
     
   
