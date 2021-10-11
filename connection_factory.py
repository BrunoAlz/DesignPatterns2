import MySQLdb


def get_connection():
    connection = MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='dp'
    )
    return connection
