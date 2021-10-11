import MySQLdb
from connection_factory import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute('SELECT * FROM lol')

for linha in cursor:
    print(linha)
    
