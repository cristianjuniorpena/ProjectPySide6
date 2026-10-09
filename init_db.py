import re
import sys
from pathlib import Path

import mysql.connector

from config import Settings

SCHEMA = Path(__file__).with_name('schema.sql')
NOME_BANCO_VALIDO = re.compile(r'^[A-Za-z0-9_]+$')


def main():
    try:
        settings = Settings.from_env(require_token=False)
    except RuntimeError as error:
        print(f'Erro de configuração: {error}')
        return 1

    if not NOME_BANCO_VALIDO.fullmatch(settings.db_name):
        print(f'Nome de banco inválido no .env: {settings.db_name}')
        return 1

    try:
        sql = SCHEMA.read_text(encoding='utf-8')
    except OSError as error:
        print(f'Não foi possível ler {SCHEMA.name}: {error}')
        return 1

    connection = None
    cursor = None
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
        return 0
    except mysql.connector.Error as error:
        print(f'Erro ao inicializar o banco: {error}')
        return 1
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == '__main__':
    sys.exit(main())
