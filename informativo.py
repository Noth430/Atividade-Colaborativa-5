# banco de dados
# SQLite


# SQL
# Linguagem de Consulta Estruturada

# SELECT * FROM CLIENTES 
# nome, sobrenome, idade 

# ORM - Object Relational Mapper
# pip install sqlalchemy

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# ORM
# CREATE DATABASE meubanco;

# Criando conexão com banco de dados.
Session = sessionmaker(bind=db)
session = Session()

#  I/O
# I = input
# O = output(saída)

# Computação na nuvem

# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

# Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

# Salvar no banco de dados.
os.system("cls || clear")

# Create
print("Solicitando dados para o usuário")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu e-mail: ")
inserir_senha = input("Digite sua senha: ")


usuario = Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()

# Listando todos os usuários do banco de dados.
print("\nExibindo todods os usuarios do banco de dados.")
lista_usuarios = session.query(Usuario).all()


# Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")


# Delete
print("\nExcluindo um usuário.")
email_usuario = input("Informe o email do usuário para ser excluido: ")

usuario=session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print(f"{usuario.nome} excluido com sucesso.")

# Listando todos os usuários do banco de dados.
print("\nExibindo todods os usuarios do banco de dados.")
lista_usuarios = session.query(Usuario).all()


# Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

# Update
print("\nAtualizando dados do usuário. ")
novos_dados = Usuario(
    nome = input("Digite seu nome: "),
    email = input("Digite seu email: "),
    senha = input("Digite sua senha: ")
)

# Fechando conexão. 
session.close()