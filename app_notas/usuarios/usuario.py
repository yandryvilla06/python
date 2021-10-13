
import usuarios.conexion as conexion
import datetime
import hashlib

connecta=conexion.conectar()
database=connecta[0]
cursor=connecta[1]


class Usuario:


    def __init__(self,nombre,apellidos,email,passwd):
       
       self.nombre=nombre
       self.apellido=apellidos
       self.email=email
       self.passwd=passwd
   
    def registrar(self):

        fecha=datetime.datetime.now()

        """ Cifrar contraseña usamos el algoritmo sha256 , el metodo update le pasamos lo q queremos cifrar , este metodo solo acepta bytes y self.pass es un string
        por lo tanto usamos encode('utf8') para que asi me lo pase a hezadecimal """

        cifrado=hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))


        sql="INSERT into usuarios VALUES(null,%s,%s,%s,%s,%s)"

        """ Usamos hexdigest() que lo que hace es ponerlo en hexadecimal asi podemos meterlo como string qe es lo q acepta nuestra BBDD """
        usuario=(self.nombre,self.apellido,self.email,cifrado.hexdigest(),fecha)
        try:
            cursor.execute(sql,usuario)
            database.commit()
            """ devolvemos una lista con el numero de filas devueltas del insert y el objeto insertado en forma de lista"""
            # return [cursor.rowcount,self]
            result=[cursor.rowcount,self]
        except:
            """ Si no se puede insertar el usuario le damos que devuelva 0 """
            result=[0,self]

        return result
     
    
    def identificar(self):
        sql="SELECT * FROM usuarios WHERE email=%s AND pass=%s"
        
        cifrado=hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))
        #dtos consulta
        usuario=(self.email,cifrado.hexdigest())
        cursor.execute(sql,usuario)
        """OJITO A LA SINTAXIS DE SQL"""
        result=cursor.fetchone()

        return result

       