"""
Ejercicio 2.Escribir un programa que añada valores a una lista 
mientras que su longitud sea menor a 120 y luego mostrar la lista 
extra; usar un while y for 
"""


lista=[]

while int(len(lista))<4:
    valor=input(" Dime valor ")
    lista.append(valor)
print(lista)