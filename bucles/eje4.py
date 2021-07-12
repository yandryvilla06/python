"""
Pedir 2 numeros al usuario y hacer todas las operaciones de la calculadora
"""

# numero2=int(input("Escriba segundo numero "))

numero1=0
numero2=0

while numero1<=0 :
    numero1=int(input("Escriba primer numero "))

while numero2<=0:
    numero2=int(input("Escriba segundo numero "))



operacion=input("elija operacion \n suma \n resta \n multiplicar \n dividir \t escriba operacion :")

if operacion=="suma":
    res=numero1+numero2
    print("El resultado es " + str(res))
elif operacion=="resta":
    if numero1>numero2 :
     res=numero1-numero2
     print("El resultado es " + str(res))
    else:
     res=numero2-numero1
     print("El resultado es " +  str(res))
elif operacion=="multiplicar":
    res=numero1*numero2
    print("El resultado es " + str(res))
elif operacion=="dividir":
    if numero1>numero2 :
        res=numero1/numero2
        print("El resultado es " +  str(res))
    else:
        res=numero2/numero1
        print("El resultado es " + str(res))
else:
     print("nada") 



