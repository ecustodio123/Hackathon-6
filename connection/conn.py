from psycopg2 import connect, Error

class Connection (): 
    def __init__(self, server='127.0.0.1', user='postgres', password='admin', database='hackathon', port=5432):
        self.db = connect(host=server, user=user, password=password, database=database, port=port)
        self.cursor = self.db.cursor()

    def execute_query(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def close_connection(self):
        self.db.close()

    def commit(self):
        self.db.commit()
        return True
