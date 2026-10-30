import re
import sys
from pathlib import Path
import mysql.connector
from config import Settings

SCHEMA = Path(__file__).with_name('schema.sql')

def validate_database_name(databaseName):
    VALID_DATABASE_NAME = re.compile(r'^[A-Za-z0-9_]+$')
    return VALID_DATABASE_NAME.fullmatch(databaseName)

def try_read_schemaSQL(schema):
    try:
        sql = SCHEMA.read_text(encoding='utf-8')
        return (True, sql)
    except OSError as error:
        return (False, f'Não foi possível ler {SCHEMA.name}: {error}')
        
def create_database_and_table(settings, sql):
    try:
        connection = mysql.connector.connect(
            host=settings.db_host,
            port=settings.db_port,
            user=settings.db_user,
            password=settings.db_password,
            connection_timeout=5,
        )
        cursor = connection.cursor()
        cursor.execute(
            f'CREATE DATABASE IF NOT EXISTS `{settings.db_name}` '
            'DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci'
        )
        cursor.execute(f'USE `{settings.db_name}`')
        for statement in sql.split(';'):
            if statement.strip():
                cursor.execute(statement)
        connection.commit()
        print(f'Banco "{settings.db_name}" e tabela "{settings.db_table}" prontos.')
        return 
    except mysql.connector.Error as error:
        print(f'Erro ao inicializar o banco: {error}')
        return 
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def main():
    settings = Settings.get_environment_variables_from_env(require_token=False)

    if not validate_database_name(settings.db_name):
        print('Erro na criação do banco de dados: o DB_NAME .env só pode conter letras e números')
        return

    ok, sql = try_read_schemaSQL(SCHEMA)
    if not sql:
        print(sql)
        return
    
    create_database_and_table(settings, sql)

    


if __name__ == '__main__':
    sys.exit(main())