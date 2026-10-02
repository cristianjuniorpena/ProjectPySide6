import mysql.connector

class Database():
    def __init__(self, host, port, user, password):
        self.acess = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
        }
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.acess['host'],
            port=self.acess['port'],
            user=self.acess['user'],
            password=self.acess['password']
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("use empresas")
        self.connection.commit()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        print('conexão encerrada')

    def select_empresa(self):
        try:
            self.connect()
            self.cursor.execute('''select * from empresa''');
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            print(f'erro na busca de dados {error}')
        finally:
            self.cursor.close()
            self.connection.close()

    def insert_empresa(self, cnpj, nome_empresa, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email):
        try:
            self.connect()
            self.cursor.execute('''insert into empresa values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (cnpj, nome_empresa, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email))
            self.connection.commit()
            print('dados inseridos com sucesso')
        except mysql.connector.Error as error:
            print(f'erro na inserção de dados {error}')
        finally:
            self.cursor.close()
            self.connection.close()
    
    def delete_empresa(self, cnpj):
        try:
            self.connect()
            self.cursor.execute('''delete from empresa where cnpj = %s''', (cnpj,));
            self.connection.commit()
            print('dados excluídos com sucesso')
        except mysql.connector.Error as error:
            print(f'erro na exclusão de dados {error}')
        finally:
            self.cursor.close()
            self.connection.close()
    
    def update_empresa(self, dados_alterados, cnpj):
        try:
            self.connect()
            campos = ', '.join(f'`{campo}` = %s' for campo in dados_alterados)
            valores = list(dados_alterados.values()) + [cnpj]
            self.cursor.execute(f'UPDATE empresa SET {campos} WHERE cnpj = %s', valores)
            self.connection.commit()
            print('dados alterados com sucesso')
            return True
        except mysql.connector.Error as error:
            print(f'erro na alteração de dados {error}')
            return False
        finally:
            self.cursor.close()
            self.connection.close()
