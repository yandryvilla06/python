""" crear una lista de contactos con nombre y movil"""

""" Ojo empieza desde la Pos=0 """
contactos=[
      ["yandry",618152241],
      ["rafael",651804402],
      ["shina",665691184]
]

""" mostramos el telefono de rafael"""

# print(contactos[1][1])

""" Mostramos toda la lista"""

# for nombre in contactos:
#     for telefono in nombre:
         
#              print(telefono)

""" Solo quiero mostrar el telefono de Shina"""

for contacto in contactos :
       for elemento in contacto:
        if contacto.index(elemento)== 0:
         nombre=elemento
         print(nombre)
        if contacto.index(elemento)==1:
         print("tel"+str(elemento))
        