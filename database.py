from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///biblioteca.db", echo=False)

SessionLocal = sessionmaker(bind=engine)
session = Session()
