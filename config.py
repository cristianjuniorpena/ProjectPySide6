import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    receitaws_token: str
    db_table: str = 'empresa'

    mandatory_database_fields = ('DB_HOST', 'DB_PORT', 'DB_USER', 'DB_NAME')
    missing_field = []


    @classmethod
    def verify_missing_fields_from_env(cls):
        cls.missing_fields = [field for field in cls.mandatory_database_fields if not os.getenv(field)]
        if cls.missing_fields:
            return True
        else:
            return False

    @classmethod
    def verify_if_DB_PORT_is_number(cls):
        try:
            db_port = int(os.getenv('DB_PORT'))
        except ValueError:
            raise ValueError
            

    @classmethod
    def get_environment_variables_from_env(cls, require_token=True):
        if require_token:
            cls.mandatory_database_fields += ('RECEITAWS_TOKEN',)

        if cls.verify_missing_fields_from_env():
            raise RuntimeError(
            'Variaveis de ambiente ausentes no .env: '
            + ', '.join(cls.missing_fields)
            + '. Copie o .env.example e preencha os valores.'
        )
        
        try:
            cls.verify_if_DB_PORT_is_number()
        except ValueError:
            raise RuntimeError('DB_PORT invalido no .env: deve ser um numero inteiro.')            

        return cls(
            db_host=os.getenv('DB_HOST'),
            db_port=os.getenv('DB_PORT'),
            db_user=os.getenv('DB_USER'),
            db_password=os.getenv('DB_PASSWORD', ''),
            db_name=os.getenv('DB_NAME'),
            receitaws_token=os.getenv('RECEITAWS_TOKEN', ''),
        )