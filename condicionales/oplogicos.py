
edad=int(input("Dime tu edad :"))

if edad<18:

 print("eres menor para beber")

elif edad>=18 and edad<=21:

 print("puedes beber en USA y España")

else:

 print("Te jodiste no bebes")


pais=input("Dime tu pais : ")

if not(pais=="españa"):

 print("Tu pais no es España")

else:
 
 print("Tu pais es España")
