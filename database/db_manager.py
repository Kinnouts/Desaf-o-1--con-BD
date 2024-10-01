import sqlite3

class DBManager:
    def __init__(self, db_name='productos.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            idp INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            fecha_caducidad TEXT,
            potencia_consumida INTEGER
        )
        ''')
        conn.commit()
        conn.close()