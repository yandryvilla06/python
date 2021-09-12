"Programa que hac operaciones"

# def suma(**kwargs):
#     s = 0
#     for key, value in kwargs.items():
#         print(key, "=", value)
#         s += value
#     return print("LA SUMA TOTAL ES "+str(s))
    
# suma(a=3, b=10, c=3)

def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
         
         if value<0:
             print("Numero negativo " +str(value)+ " no se suma")
         else:
             s+=value
    return print("LA SUMA TOTAL ES "+str(s))
    
suma(a=-3, b=10, c=3)