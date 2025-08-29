import sqlite3 as sql

class TransactionObject:
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True  # ← corrigido: era connect=True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql_cmd, parms=None):
        if TransactionObject.connected:
            if parms is None:
                TransactionObject.cur.execute(sql_cmd)
            else:
                TransactionObject.cur.execute(sql_cmd, parms)
            return True
        return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        return False

    @staticmethod
    def initDB():
        trans = TransactionObject()
        trans.connect()
        trans.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                sobrenome TEXT,
                email TEXT,
                CPF TEXT
            )
        """)
        trans.persist()
        trans.disconnect()

    @staticmethod
    def insert(nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("INSERT INTO clientes VALUES(NULL,?,?,?,?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()

    @staticmethod
    def view():
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    @staticmethod
    def delete(id):
        trans = TransactionObject()
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id=?", (id,))
        trans.persist()
        trans.disconnect()

    @staticmethod
    def update(id, nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, CPF=? WHERE id=?",
                      (nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()

TransactionObject.initDB()
