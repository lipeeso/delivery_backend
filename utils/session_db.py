from sqlalchemy.orm import sessionmaker

from models.model_db import db


def get_session():
    """Abrindo uma sessão e fazendo uma consulta no banco de dados"""
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()
