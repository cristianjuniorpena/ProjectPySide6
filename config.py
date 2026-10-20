import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

TABELA_EMPRESA = 'empresa'


@dataclass(frozen=True)
class Settings:
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    receitaws_token: str
    db_table: str = TABELA_EMPRESA

    @classmethod
    def from_env(cls, require_token=True):
        mandatory_database_fields = ('DB_HOST', 'DB_PORT', 'DB_USER', 'DB_NAME')
        if require_token:
            mandatory_database_fields += ('RECEITAWS_TOKEN',)

        missing_fields = [var for var in mandatory_database_fields if not os.getenv(var)]
        if missing_fields:
            raise RuntimeError(
                'Variaveis de ambiente ausentes no .env: '
                + ', '.join(missing_fields)
                + '. Copie o .env.example e preencha os valores.'
            )

        try:
            db_port = int(os.getenv('DB_PORT'))
        except ValueError:
            raise RuntimeError('DB_PORT invalido no .env: deve ser um numero inteiro.')

        return cls(
            db_host=os.getenv('DB_HOST'),
            db_port=db_port,
            db_user=os.getenv('DB_USER'),
            db_password=os.getenv('DB_PASSWORD', ''),
            db_name=os.getenv('DB_NAME'),
            receitaws_token=os.getenv('RECEITAWS_TOKEN', ''),
        )
