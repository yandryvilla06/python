"""
Funciones:
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocando a la funcion tantas veces como sea necesario.

def mifuncion(parametros):
    instrucciones


parametros opcionales
def mifuncion(parametro, parametro2=None)
  if parametro2!=None
     print("muestro")


funciones lambda

En Python, una función Lambda se refiere a una pequeña función anónima. Las llamamos “funciones anónimas” porque técnicamente carecen de nombre.
Al contrario que una función normal, no la definimos con la palabra clave estándar def que utilizamos en Python. En su lugar, las funciones Lambda 
se definen como una línea que ejecuta una sola expresión. Este tipo de funciones pueden tomar cualquier número de argumentos, pero solo pueden tener una expresión.

Como mejor te lo puedo explicar es enseñándote un ejemplo básico, vamos a ver una función normal y un ejemplo de Lambda:
#Aquí tenemos una función creada para sumar.

def suma(x,y):
    return(x + y)
#Aquí tenemos una función Lambda que también suma.
lambda x,y : x + y
#Para poder utilizarla necesitamos guardarla en una variable.
suma_dos = lambda x,y : x + y


Variables locales:
Se definen denro de la funcion y no se pueden usar fuera de ella , solo estan disponibles dentro
a no ser que hagamos un return

Variables globales : Se declaran fuera de una funcion y estan disponibles dento y fuera de ellas

funciones 
isinstance(variable,float)=me dice lo q es una variable
varibale.strip =limpia los espacios

del(variable)=me elimina la varible

len(variable)=me dice longitud de variable
find=me busca la palabra
variable.find("vida")

nuevafrase=frase,replace("vida","moto")
me sustituye vida por moto

lower()=minusculas
upper()=mayusculas

"""

