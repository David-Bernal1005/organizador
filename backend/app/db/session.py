
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.core.config import settings
from backend.app.db.base import Base


engine = create_engine(
    settings.DATABASE_URL, 
    echo=False,
    pool_pre_ping=True,  # Verifica la conexión antes de usar
    pool_recycle=3600    # Recicla conexiones cada hora
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()