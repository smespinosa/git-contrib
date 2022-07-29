import psycopg

class DataContext:
    connection: str

    def __init__(self, connection: str):
        self.connection = connection
    
    def get_connection(self):
        with psycopg.connect(self.connection) as conn:
            pass


        return conn
