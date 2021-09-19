"""Al comienzo del tutorial adelantaba que el tipo set en Python es utilizado para trabajar con conjuntos de elementos. La principal característica de este tipo de datos es que es una colección cuyos elementos no guardan ningún orden y que además son únicos. No tienen ni indice ni orden , son mutables.

Estas características hacen que los principales usos de esta clase sean conocer si un elemento pertenece o no a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).

Además, esta clase también implementa las típicas operaciones matemáticas sobre conjuntos: unión, intersección, diferencia, …

Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {}, o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable (como una lista, una tupla, una cadena …).
 NOTA: Los elementos que se pueden añadir a un conjunto deben ser de tipo hashable. Un objeto es hashable si tiene un valor de hash que no cambia durante todo su ciclo de vida. En principio, los objetos que son instancias de clases definidas por el usuario son hashables. También lo son la mayoría de tipos inmutables definidos por Python.

"""
mi_conjunto = {1, 3, 2, 9, 3, 1}
for e in mi_conjunto:
     print(e)

""" Eliminar un elemento de un conjunto en Python
La clase set ofrece cuatro métodos para eliminar elementos de un conjunto. Son: discard(), remove(), pop() y clear(). A continuación te explico qué hace cada uno de ellos.

discard(elemento) y remove(elemento) eliminan elemento del conjunto. La única diferencia es que si elemento no existe, discard() no hace nada mientras que remove() lanza la excepción KeyError.

pop() es un tanto peculiar. Este método devuelve un elemento aleatorio del conjunto y lo elimina del mismo. Si el conjunto está vacío, lanza la excepción KeyError.

clear() elimina todos los elementos contenidos en el conjunto.

"""
