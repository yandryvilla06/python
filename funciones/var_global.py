"""
Un ámbito define los límites de un programa en los que un espacio de nombres puede ser accedido sin utilizar un prefijo.

Como te he mostrado en el apartado anterior, en principio existen, como mínimo, tres ámbitos. Uno por cada espacio de nombres:

Ámbito de la función actual, que tiene los nombres locales a la función.
Ámbito a nivel de módulo, que tiene los nombres globales, los que se definen en el propio módulo.
Ámbito incorporado, el más externo, que tiene los nombres que define Python.
Cuando desde dentro de una función se hace referencia a un nombre, este se busca en primer lugar en el espacio de nombres local, luego en el espacio de nombres global y finalmente en el espacio de nombres incorporado.

Si hay una función dentro de otra función, se anida un nuevo ámbito dentro del ámbito local.

"""

#nombre="MArio" aqui esta definida globalmente 

# def funcion():

#     nombre="Pepe"  # esto seria una variable local


#print(nombre) no podemos hacer un print de esto debido a que nombre es local a la funcion

"Si la queremos modificar fuera de la funcion lo que debemos de hacer es hacerla global"

def funcion():
    global nombre
    nombre="Pepe"

# funcion() Ojo: si no invocamos la funcion es normal que no la tengamos definida 
funcion()

nombre="Yandry wp"

print(nombre) #aqui modificamos la funcion , bueno arriba 




