from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

"""No SQLITE ele pede /// """

# -> Conexão com o banco de dados
db = create_engine("sqlite:///database.db")  # Aqui vai passar o link do banco de dados

# -> Base do banco de dados
Base = declarative_base()

# -> Criar as classes/tabelas do banco de dados
"""Criar uma tabela -> 
Usuário
Pedido
ItensPedido

OBS: 
ChoiceType -> Garante a padronização e integridade do banco de dados
"""


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    email = Column(
        "email", String, nullable=False
    )  # parâmetro nullable impede de criar algo sem o email
    nome = Column("nome", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    # admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo: True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        # self.admin = admin


class Pedido(Base):
    __tablename__ = "pedidos"

    """Garante a integridade do banco de dados"""
    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO"),
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)  # status: pendente, cancelado, finalizado
    usuario = Column(
        "usuario", ForeignKey("usuarios.id")
    )  # Vai passar o nome da tabela e a coluna
    preco = Column("preco", Float)
    # itens =

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco


class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido


# -> Executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)
