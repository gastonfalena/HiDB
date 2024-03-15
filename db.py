import mysql.connector
from decouple import config 
MYSQL_HOST , MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB = config('MYSQL_HOST'),config('MYSQL_USER'), \
config('MYSQL_PASSWORD'),config('MYSQL_DB')

midb = mysql.connector.connect(
   host = MYSQL_HOST,
   user = MYSQL_USER,
   password = MYSQL_PASSWORD,
   database = MYSQL_DB
)
#objeto que nos permtie interactuar con la base de datos mediante el lenguaje sql
cursor = midb.cursor()

cursor.execute('select * from Usuario')

resultado = cursor.fetchall()

print(resultado)