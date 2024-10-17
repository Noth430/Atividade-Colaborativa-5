import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=db)
session = Session()

# Criando tabela.
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", String)
    cpf = Column("cpf", String)
    setor = Column("setor", String)
    funcao = Column("funcao1", String)
    salario = Column("salario", String)
    telefone = Column("telefone", String)

# Definindo atributos da classe.
    def __init__(self, nome: str, idade: str, cpf: str, setor: str, funcao: str, salario: str, telefone: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.salario = salario
        self.telefone = telefone

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

# Salvar no banco de dados.
os.system("cls || clear")

# Create
def menu():
    print("""
  --- RH System ---
    1 - Adicionar funcionário
    2 - Consultar um Funcionário 
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário 
    5 - Lista todos os funcionário
    0 - Sair do sistema

""")

#def salvar_funcionario(funcionario):

while True:
    menu()
    opcao = input("Resposta: ")
    match opcao:
        case "1":
            funcionario = Funcionario(
                nome = input("Digite seu nome: "),
                idade = int(input("Digite sua idade: ")),
                
            )