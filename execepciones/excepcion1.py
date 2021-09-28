try:

 num=int(input("dime num 1 "))
 num2=int(input("dime num 2 "))
 
 sol=num/num2

except Exception as e:
     print("excepcion:" + type(e).__name__)