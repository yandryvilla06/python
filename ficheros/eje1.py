"""
En este ejercicio deberás crear un script llamado personas.py que lea los datos de un fichero de texto, que transforme cada fila en un diccionario y lo añada a una lista llamada personas. Luego rocorre las personas de la lista y paracada una muestra de forma amigable todos sus campos.

El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en texto plano (créalo previamente):


1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.

"""

from io import  open
import pathlib


fichero=open("personas.txt","w")


diccionario=[

    { "id":1,
      "nombre":"Carlos",
      "apellido":"Perez",
      "fecha":"05/06/1998"
    
    },

    { "id":2,
      "nombre":"Manuel",
      "apellido":"Heredia" ,
      "fecha":"20/08/1995"
    
    },

    {
        "id":3,
        "nombre":"Rosa",
        "apellido":"Campos",
        "fecha":"12/06/1961"

    },

    {

        "id":4,
        "nombre":"David",
        "apellido":"Garcia",
        "fecha":"25/07/2006"

    }



]


# print(diccionario)
# for elemento in diccionario:
#     print(f" ID  {elemento['id']} Nombre  {elemento['nombre']} Apellido  {elemento['apellido']} Fecha  {elemento['fecha']}")

fichero.writelines(str(diccionario))

fichero.close()