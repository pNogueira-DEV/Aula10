from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()


class Departamento(Base):
    __tablename__ = "departamentos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)


    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Usuario = id={self.id} - nome={self.nome}"

