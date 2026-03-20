from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Departamento(Base):
    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    funcionarios = relationship("Funcionario", back_populates="departamento")

    def __init__(self, nome):
        self.nome = nome

    #Função para imprimir
    def __repr__(self):
        return f"Departamento =  id={self.id} - nome={self.nome}"

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cargo = Column(String(100), nullable=False)
    salario = Column(Float, nullable=False)

    departamento_id = Column(Integer, ForeignKey("departamentos.id"))

    #Relacionamento
    departamento = relationship("Departamento", back_populates="funcionarios")

    def __init__(self, nome):
        self.nome = nome

    #Função para imprimir
    def __repr__(self):
        return f"Departamento =  id={self.id} - nome={self.nome}"


engine = create_engine("sqlite:///empresa.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)