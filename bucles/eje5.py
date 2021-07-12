"""
Eje 5:
programa que muestre todos los numeros entre dos numeros introducidos por teclado
"""

numero1=int(input("Dime numero 1 :"))
numero2=int(input("Dime numero 2 :"))

if numero1>numero2:
    for i in range(numero2,numero1+1):
        print(i)

else:
    for i in range(numero1,numero2+1):
        print(i)