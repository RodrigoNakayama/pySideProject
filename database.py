import sqlite3

class Database:
    def __init__(self, name = 'system.db'):
        self.name: str = name
        self.connection: sqlite3.Connection

    def connection(self):
        self.connection = sqlite3.Connection(self.name)

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()

        except sqlite3.Error as e:
            print("Erro ao fechar conexão: {e}")

    def create_table_empresa(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresa
            (
                CNPJ TEXT,
                NOME TEXT,
                LOGRADOURO TEXT,
                NUMERO TEXT,
                COMPLEMENTO TEXT,
                BAIRRO TEXT,
                MUNICIPIO TEXT,
                UF TEXT,
                CEP TEXT,
                TELEFONE TEXT,
                EMAIL TEXT,
                PRIMARY KEY(CNPJ)
            );"""
        )

    def register_empresa(self, fullDataSet):
        campos_tabela = ('CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL')
        qtd = "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""INSERT INTO Empresa {campos_tabela} VALUES({qtd})""", fullDataSet)
            return("ok")
        except:
            return "ERRO"

    def select_all_empresa(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Empresa ORDER BY NONE")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass

    def delete_empresas(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresa WHERE CNPJ = '{id}' ")
            self.connection.commit()
            return "Empresa excluida com sucesso!"
        except:
            return "Erro ao excluir registro!"

    def update_empresa(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Empresa set
            CNPJ = '{fullDataSet[0]}',
            NOME = '{fullDataSet[1]}',
            LOGRADOURO = '{fullDataSet[2]}',
            NUMERO = '{fullDataSet[3]}',
            COMPLEMENTO = '{fullDataSet[4]}',
            BAIRRO = '{fullDataSet[5]}',
            MUNICIPIO = '{fullDataSet[6]}',
            UF = '{fullDataSet[7]}',
            CEP = '{fullDataSet[8]}',
            TELEFONE = '{fullDataSet[9]}',
            EMAIL = '{fullDataSet[10]}',
            WHERE CNPJ = = '{fullDataSet[0]}'""")
        self.connection.commit()