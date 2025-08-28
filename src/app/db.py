from settings import env
from sqlalchemy import create_engine

db_url = env.str('DATABASE_URL', 'sqlite+pysqlite:///:memory:')
engine = create_engine(url=db_url, echo=False)
