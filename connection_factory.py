import MySQLdb

class Connection_factory(object):
    def get_connection(self):
        connection = MySQLdb.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='dp'
        )
        return connection
