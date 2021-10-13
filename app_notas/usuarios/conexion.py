import mysql.connector

def conectar():

    database=mysql.connector.connect(
    
        host="localhost",
        user="root",
        passwd="",
        database="appnotas",
        #  port="127.0.0.1"


    )

    cursor=database.cursor(buffered=True)
#ESTO ME PERMITE HACER MUCHAS CONSULTAS CON EL MISMO CURSOR
    return [database,cursor]
# print(database)