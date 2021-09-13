"""
La sintaxis para definir una función lambda es la siguiente:

lambda parámetros: expresión
A continuación, te detallo las características principales de una función anónima:

Son funciones que pueden definir cualquier número de parámetros pero una única expresión. Esta expresión es evaluada y devuelta.
Se pueden usar en cualquier lugar en el que una función sea requerida.
Estas funciones están restringidas al uso de una sola expresión.
Se suelen usar en combinación con otras funciones, generalmente como argumentos de otra función. 

"""

num=int(input("Dime numero a sumar"))
suma=lambda x:x+num;
print(str(suma(2)))

