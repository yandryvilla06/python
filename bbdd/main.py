import mysql.connector

#conexion

database=mysql.connector.connect(

     host="localhost", #el servidor es local
     user="root",
     passwd="",
     database="curso_python"

     
)

#como saber que la xonexion ha sido correcta?

# print(database) si ejecutamos el programa nos daremos cuenta
#que database es un objeto de mysql-connector

""" Creacion de la Base de datos
  1) Creamos el cursor que nos permitira conectarnos a mysql y crear las consultas
  2) Mediante Create creamos la base de datos
  3) si queremos comprobar que se ha creado correctamente , basta con encender nuestro servidor
  en este caso XAMP y luego meternos a phpMyadmin y veremos como esta creada 

"""

cursor=database.cursor(buffered=True)

#Buffered lo ponemos para que cuando hagamos muchas consultas no de fallos

#Este comando es mejor ya que me crea la base de datos si no existe 
cursor.execute("CREATE DATABASE IF NOT EXISTS curso_python")

# cursor.execute("CREATE DATABASE curso_python")

""" Para mostrar el resto de base de datos usamos SHOW DATABASE """

# cursor.execute("SHOW DATABASES")

# for bd in cursor :
   
#     print(bd)

#CREAR TABLAS OJO A LA SINTAXIS

cursor.execute(""" CREATE TABLE IF NOT EXISTS vehiculos (
  
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)

)""")


#MOSTRAR LAS TABLAS

# cursor.execute("SHOW TABLES")

# for tablas in cursor:
#   print(tablas)

#INSERTAR DATOS

# cursor.execute("INSERT INTO  vehiculos VALUES (null,'Opel','Astra','6500')")

#INSERTAR MAS DE UN DATO 

coches=[

  ('Citroen','Picasso',1200),
  ('Mercedes','Clase1',25000),
  ('Ford','Kouga',35000),
  ('BMW','M5',45000)
  
  ]

""" 1) Usamos la funcion executemany()
      Pasa varios registros a la tabla de una base de datos con una sola instrucción.
      Como las filas o registros se almacenan en una tupla, para pasarlos es necesaria una lista con los registros, 
      teniendo en cuenta que cada elemento de la lista es una tupla con los valores de los campos a pasar
    
    2)  VALUES(null,%s,%s,%s) => Vamos a explicar esto el null es debido a que ID es autoincrementable me lo hace automaticamente SQL
        la palabra reservada %s viene a sustituir el valor que le pasamos de nuestra lista de tuplas, en este caso nuestar lista se llama coches


  """
# cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)",coches)



#SELECT 

# cursor.execute("SELECT * from vehiculos")
#con fetchall() recojo todos los datps y los almacena en un array , por eso es que los meto en una variable .Tambien por comodidad
# result=cursor.fetchall()

#Si solo quiero que me saque el primer vehiculo uso fetchone() me devuelve solo una fila en forma de array

# coche=cursor.fetchone()


#Borrar filas usamos delete , ojito el commit() es fundamental para que se guarde el cambio, no tener select en medio si no dara error

# cursor.execute("DELETE FROM vehiculos WHERE marca='Ford' ")

# database.commit()

#Para saber cuantos datos se gan borrado usamos cursor.rowcount


#Actualiza Update

# cursor.execute("UPDATE vehiculos SET modelo='Picasso' WHERE marca='BMW' ")
# database.commit()



#necesito el commit para guardar los cambios  
#database.commit() =>ojo que al gacer un fetchone esto me da error hay que borrarlo
