""" La función filter() filtra una lista de elementos para los que una función devuelve True.

 filter(una_funcion, una_lista)
 Imagina que quieres filtrar una lista de números para obtener solo los valores pares.

 De nuevo, una primera aproximación podría ser como la siguiente:"""

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda  x : x % 2 == 0, valores))
print(pares)
[2, 4, 6, 8]
