from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
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
    


class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cargo = Column(String(100), nullable=False)
    salario = Column(Float, nullable=False)



    funcionario_id = Column(Integer,ForeignKey("funcionarios_id"))


    
    
