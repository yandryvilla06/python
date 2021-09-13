""" 
Las listas en Python son uno de los tipos o estructuras de datos más versátiles del lenguaje, ya que permiten almacenar un conjunto arbitrario de datos. Es decir, podemos guardar en ellas prácticamente lo que sea. Si vienes de otros lenguajes de programación, se podría decir que son similares a los arrays.

lista = [1, 2, 3, 4]
También se puede crear usando list y pasando un objeto iterable.

lista = list("1234")
Una lista sea crea con [] separando sus elementos con comas ,. Una gran ventaja es que pueden almacenar tipos de datos distintos.

lista = [1, "Hola", 3.67, [1, 2, 3]]
Algunas propiedades de las listas:

Son ordenadas, mantienen el orden en el que han sido definidas
Pueden ser formadas por tipos arbitrarios
Pueden ser indexadas con [i].
Se pueden anidar, es decir, meter una dentro de la otra.
Son mutables, ya que sus elementos pueden ser modificados.
Son dinámicas, ya que se pueden añadir o eliminar elementos.
"""

""" 1) Meter valores a una lista"""
# lista=[]
# lista.append("yandry")
# print(lista)
""" 2) Acceder y modificar listas"""
# lista=[]
# lista.append("pepe")
# lista[0]="rafael"
# print(lista)
"""3) Recorrer listas """

# lista=["yandry","pepe","juan","maria"]

# for l in lista :
#     print(l)

""" 4) Enumerar una lista . Esto lo que hace es basicamente mediante un index el cual empezara en 0 , ira enumerandolo segun los parametros de nuestra lista"""

# lista=["yandry","pepe","juan","maria"]

# for num , l in enumerate(lista):
#     print(num,l)

""" 5) Recorrernos 2 listas .Usamos zip que nos la rrecorre"""

# lista1 = [5, 9, 10]
# lista2 = ["Jazz", "Rock", "Djent"]
# for l1, l2 in zip(lista1, lista2):
#     print(l1, l2)

""" 6) El método extend() permite añadir una lista a la lista inicial."""

# l = [1, 2]
# l.extend([3, 4])
# print(l) #[1, 2, 3, 4]

""" insert(<index>, <obj>)
El método insert() añade un elemento en una posición o índice determinado."""

# l=[1,2,3,4]

# l.insert(2,"juan") 
# print(l)

""" Metodo remove"""

# l=[1,2,3,4]
# l.remove(2)
# print(l)

""" pop(index=-1)
El método pop() elimina por defecto el último elemento de la lista, pero si se pasa como parámetro un índice permite borrar elementos diferentes al último."""


# l = [1, 2, 3]
# l.pop()
# print(l) #[1, 2]

""" reverse()
El método reverse() inverte el órden de la lista."""

# l = [1, 2, 3]
# l.reverse()
# print(l) #[3, 2, 1]

""" sort()
El método sort() ordena los elementos de menos a mayor por defecto.

l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3] """


"""  También permite ordenar de mayor a menor si se pasa como parámetro reverse=True.
l = [3, 1, 2]
l.sort(reverse=True)
print(l) #[3, 2, 1]
"""
