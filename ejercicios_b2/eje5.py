"""
eje 5.
Crear una lista con este contenido de la tabla
Accion   Aventuras          Deportes 
Gta      Assassins          Fifa21
COD      CRASH              PRO 21
PUGB     PRINCE OF PERSIA   PES 22

"""


diccionario=[
    {
    
      "categoria":"Accion",
      "juegos":["GTA","COD","PUGB"]
    
   },
   {
      "categoria":"Aventuras",
      "juegos":["Assasins","Crash","Prince of persia"]
   },

   {
       "categoria":"Deportes",
       "juegos":["FIFA","PRO 21","PES 22"]
   }

]

for categoria in diccionario:
       
       print(f" Categoria  {categoria['categoria']}")

       for juego in categoria['juegos']:

             print(f" Juegos  {juego}")


""" Repasamos la jugada 

Creamos una lista dentro de ella introducimos 3 diccionarios , nos rrecorremos 
la lista y en ella para ver los elementos de cada diccionario lo llamamos mediante
clave["elemento"]. En el segundo For nos rrecorremos las listas que estan metidas en el diccionario y vemos los juegos que hay 
    
"""