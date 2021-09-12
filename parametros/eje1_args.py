

# FUNCION CON *ARGS

def tabla(*args):

    for n in args:
       print(f"TABLA DEL{n} ")  
       for i in range(1,11):
          
         print(f"{n}*{i}={n*i}")


tabla(2,3)



