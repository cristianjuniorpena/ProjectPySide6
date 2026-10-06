import mysql.connector

class Database():
    def __init__(self, host, port, user, password):
        self.acesso = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
        }
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.acesso['host'],
            port=self.acesso['port'],
            user=self.acesso['user'],
            password=self.acesso['password']
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("use empresas")
        self.connection.commit()

    def _fechar(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None

    def select_empresa(self):
        try:
            self.connect()
            self.cursor.execute('''select * from empresa''')
            return (True, self.cursor.fetchall())
        except mysql.connector.Error as error:
            print(f'erro na busca de dados {error}')
            return (False, f'erro na busca de dados: {error}')
        finally:
            self._fechar()

    def insert_empresa(self, cnpj, nome_empresa, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email):
        try:
            self.connect()
            self.cursor.execute('''insert into empresa values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (cnpj, nome_empresa, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email))
            self.connection.commit()
            return (True, '')
        except mysql.connector.Error as error:
            print(f'erro na inserção de dados {error}')
            return (False, f'erro na inserção de dados: {error}')
        finally:
            self._fechar()

    def delete_empresa(self, cnpj):
        try:
            self.connect()
            self.cursor.execute('''delete from empresa where cnpj = %s''', (cnpj,))
            self.connection.commit()
            return (True, '')
        except mysql.connector.Error as error:
            print(f'erro na exclusão de dados {error}')
            return (False, f'erro na exclusão de dados: {error}')
        finally:
            self._fechar()

    def update_empresa(self, dados_alterados, cnpj):
        try:
            self.connect()
            campos = ', '.join(f'`{campo}` = %s' for campo in dados_alterados)
            valores = list(dados_alterados.values()) + [cnpj]
            self.cursor.execute(f'UPDATE empresa SET {campos} WHERE cnpj = %s', valores)
            self.connection.commit()
            return (True, '')
        except mysql.connector.Error as error:
            print(f'erro na alteração de dados {error}')
            return (False, f'erro na alteração de dados: {error}')
        finally:
            self._fechar()
