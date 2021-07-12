"""
Ejercicio7.Hacer un programa que muestre todos los numeros impares entre dos
numeros que decida el usuario

"""

from typing import Container


numero1=int(input("Dime numero 1 :"))
numero2=int(input("Dime numero 2 :"))



if numero1>numero2: 
    while numero2<=numero1:
        if numero2%2!=0:
         print(numero2)
        numero2+=1

else:
    while numero1<=numero2:
        if numero1%2!=0:
         print(numero1)
        numero1+=1
    