import datetime
from typing import AsyncContextManager

year=int(input("dime el año de tu nacimiento?"))

actual=datetime.datetime.now().year


if year>=actual:
  
  print("Es imposible el año mayor q el actual")

elif year==2010:
    print("Naciste en el mundial de españita")
else:
    print("No naciste en el mundial")
  
  
  
 