"""
Eje 9: pedir numeros hasta que sea 111
"""

from typing import NoReturn

numero=0

while numero!=111:
    
   numero=int(input("Dame  numero:"))
   if numero==111:
       print("Tu numero es 111")
       break