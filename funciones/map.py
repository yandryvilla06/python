"""
map()
La función map() en Python aplica una función a cada uno de los elementos de una lista.

map(una_funcion, una_lista)
Imagina que tienes una lista de enteros y quieres obtener una nueva lista con el cuadrado de cada uno de ellos.

"""

numeros=[]
pares=[]

numeros=range(1,100)

pares = list(map(lambda x : x %2==0, numeros))

print(pares)