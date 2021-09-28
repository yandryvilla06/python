"Leer el fichero personas.txt"

from io import open

fichero=open("personas.txt")
leer=fichero.readlines()
print(leer)
fichero.close()