import sqlite3 as sql

class TransactionObject:
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        return False
