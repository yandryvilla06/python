"""
ejercicio 1

Hacer un programa que tenga una lista de 8 numeros y haga 
lo siguiente:
-Recorrer la lista y mostrarla 
-Hacer funcion que rrecorra listas de numeros y devuelva un string
-Ordenarla y mostrarla
-Mostrar su longitud
-Buscar algun elemento (que el usuario pida por teclado)

"""


lista=[12,6,3,111,5,45,0,22]

for i in lista:
    print(str(i))

print("Procedemos a ordenarla")
lista.sort()
print(lista)
print("longitud de cadena es "+ str(len(lista)))
num=int(input(" Dime numero a buscar "))

if num in lista:
    print("Esta aqui")
else:
    print("No esta en la lista")