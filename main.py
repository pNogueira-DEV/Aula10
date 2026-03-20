from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    #relacionamento
    pedidos = relationship("Pedido", back_populates="usuario")

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Usuario = id={self.id} - nome={self.nome}"
    
class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(100), nullable=False)

    #Chave estrangeira
    # Onde tem o foreing key, tem o relacionamento muitos para um (muitos pedidos para um usuario)
    # Relacionamento aberto

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    # Relacionamento
    usuario = relationship("Usuario", back_populates="pedidos")

    def __init__(self, produto):
        self.produto = produto

    def __repr__(self):
        return f"Pedido = id={self.id} - Produto={self.produto}"
    
engine = create_engine("sqlite:///loja.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

with Session() as session:
    #Criando um objeto
    usuario1 = Usuario("Pablo")

    #Criando os pedidos
    pedido1 = Pedido("Helicoptero")
    pedido2 = Pedido("Mobilia de rodinha")
    pedido3 = Pedido("Nota Fiscal")

    #Associando pedidos aos usuarios
    usuario1.pedidos.append(pedido1)
    usuario1.pedidos.append(pedido2)
    usuario1.pedidos.append(pedido3)

    #Salvar no banco
    session.add(usuario1)
    session.commit()

    #Buscar todos os usuarios no banco:
    usuarios = session.query(Usuario).all()

    for user in usuarios:
        print(user)

    #Pegando os pedidos
    print(f"Pedidos do usuario 1: {usuarios[0].pedidos}")

    for user in usuarios:
        print(f"\nUsuarios: {user.nome}")
        for pedido in user:
            print(f"Pedido: {user.produto}")