""" EJE10: Pedir la nota de 15 alumnos y sacar cuantos han aprobado y cuantos han suspendido"""

aprobados=0
suspensos=0
for i in range(0,15):
    nota=int(input("Dime la nota del alumno"))   
    
    if nota>5:
        aprobados+=1
    else:
        suspensos+=1
    

print("APROBADOS"+str(aprobados))
print("SUSPENSOS"+str(suspensos))