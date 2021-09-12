"""
n Python, el parámetro especial *args en una función se usa para pasar, de forma opcional, un número variable de argumentos posicionales.

Jajaja, vaya paranoia de definición. Vamos a verla detalladamente:

Lo que realmente indica que el parámetro es de este tipo es el símbolo ‘*’, el nombre args se usa por convención.
El parámetro recibe los argumentos como una tupla.
Es un parámetro opcional. Se puede invocar a la función haciendo uso del mismo, o no.
El número de argumentos al invocar a la función es variable.
Son parámetros posicionales, por lo que, a diferencia de los parámetros con nombre, su valor depende de la posición en la que se pasen a la función.
Pero como yo siempre digo, las cosas se ven mejor con un ejemplo:

La siguiente función toma dos parámetros y devuelve como resultado la suma de los mismos:

def sum(x, y):
    return x + y
Si llamamos a la función con los valores x=2 e y=3, el resultado devuelto será 5.

>>>sum(2, 3)
5
Pero, ¿qué ocurre si posteriormente decidimos o nos damos cuenta de que necesitamos sumar un valor más?

>>>sum(2, 3, 4)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: sum() takes 2 positional arguments but 3 were given
Obviamente, estaba claro de que la llamada a la función iba a fallar.

¿Cómo podemos solucionar este problema? Pues una opción sería añadir más parámetros a la función, pero ¿cuántos?

La mejor solución, la más elegante y la más al estilo Python es hacer uso de *args en la definición de esta función. De este modo, podemos pasar tantos argumentos como queramos. Pero antes de esto, tenemos que reimplementar nuestra función sum:

def sum(*args):
    value = 0
    for n in args:
        value += n
    return value
Con esta nueva implementación, podemos llamar a la función con cualquier número variable de valores:

>>>sum()
0
>>>sum(2, 3)
5
>>>sum(2, 3, 4)
9
>>>sum(2, 3, 4, 6, 9, 21)
45

"""


