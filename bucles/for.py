#bucle 
# for variable in lista,diccionario,tupla:
# no se actualiza 

numero=int(input(" Dime numero y te dire su tabla de multiplicar "))

for i in range(1,11):
  
  print(f"{i}{'*'}{numero}{'='}{numero*i}")

