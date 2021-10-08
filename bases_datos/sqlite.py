#Importar modulo

import sqlite3

#conexion

conexion=sqlite3.connect('pruebas.db')

#crear cursor

cursor=conexion.cursor()

#crear tabla

# cursor.execute("CREATE TABLE IF NOT EXISTS productos("+"id INTEGER PRIMARY KEY AUTOINCREMENT,"+"titulo varchar(255),"+"descripcion text,"+"precio int(255)"+")")

# #INSERTAR DATOS

# cursor.execute("INSERT INTO productos VALUES (NULL,'BOTAS','NIKE',500)")

# #GUARDAR CAMBIOS

# conexion.commit()

# #LISTAR DATOS O HACER SELECT 

# cursor.execute("SELECT * FROM productos;")
# productos=cursor.fetchall() 
# """ fecthall() devuelve un array que contiene tadas las filas restantes del conjunto de resultados. El array representa cada fila como un array con valores de las columnas, o como un objeto con propiedades correspondientes a cada nombre de columna."""
# # print(productos[0])

# #Recorrer mi select 

# for producto in productos:
#     print("Titulo",producto[2])

#borrar registro

cursor.execute("DELETE FROM productos WHERE titulo='NIKE'")
conexion.commit()


cursor.execute("SELECT * FROM productos;")
productos=cursor.fetchall() 
print(productos)
#Cerrar conexion

conexion.close()