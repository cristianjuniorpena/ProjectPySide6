import mysql.connector

class Database():
    def __init__(self, host, port, user, password, database):
        self.acess = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'database': database,
        }
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.acess['host'],
            port=self.acess['port'],
            user=self.acess['user'],
            password=self.acess['password'],
            database=self.acess['database'],
            connection_timeout=5
        )
        self.cursor = self.connection.cursor()

    def _close(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None

    def catch_workbench_error(SQLcommand):
        def wrapper(self, *args):
            try:
                self.connect()
                response = SQLcommand(self, *args)
                return response
            except mysql.connector.Error as error:
                print(f'Erro na requisição sql: {error}')
                return (False, f'Erro na requisição sql: {error}')
            finally:
                self._close()
        return wrapper

    @catch_workbench_error        
    def select_empresa(self):
        self.cursor.execute('''select * from empresa''')
        return (True, self.cursor.fetchall())

    @catch_workbench_error
    def insert_empresa(self, cnpj, nome_empresa, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email):
        self.cursor.execute('''insert into empresa values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (cnpj, nome_empresa, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email))
        self.connection.commit()
        return (True, '')

    @catch_workbench_error
    def delete_empresa(self, cnpj):
        self.cursor.execute('''delete from empresa where cnpj = %s''', (cnpj,))
        self.connection.commit()
        return (True, '')

    @catch_workbench_error
    def update_empresa(self, dados_alterados, cnpj):
            campos = ', '.join(f'`{campo}` = %s' for campo in dados_alterados)
            valores = list(dados_alterados.values()) + [cnpj]
            self.cursor.execute(f'UPDATE empresa SET {campos} WHERE cnpj = %s', valores)
            self.connection.commit()
            return (True, '')