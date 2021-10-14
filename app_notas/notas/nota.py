import usuarios.conexion as conexion
import datetime
connecta=conexion.conectar()
database=connecta[0]
cursor=connecta[1]


class Nota:

   def __init__(self,usu_id,titulo,descripcion):

       self.usu_id=usu_id
       self.titulo=titulo
       self.descripcion=descripcion
       


   def creacion(self):
       
       fecha=datetime.datetime.now()
       
       sql="INSERT INTO notas VALUES (null,%s,%s,%s,%s)"
       nota=(self.usu_id,self.titulo,self.descripcion,fecha)
       try:
         
         cursor.execute(sql,nota)

         database.commit()
        
         result=[cursor.rowcount,self]


       except:

          result=[0,self]

       return result

    
   def listar(self):

       sql=f"SELECT * from notas WHERE usuario_id={self.usu_id};"
       cursor.execute(sql)

       database.commit()
       result=cursor.fetchall()

        
       return result
        
   def borrar(self,idbus):

       sql=f"DELETE * from notas WHERE id={idbus};"

       try:
        cursor.execute(sql)

        database.commit()
        result=cursor.rowcount()
       except:
        result=0
        
       return result


       

       