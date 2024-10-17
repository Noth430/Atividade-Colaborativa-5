import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=db)
session = Session()


# Criando tabela.
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionario"
    
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer, primary_key=True)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Float)
    telefone = Column("telefone", Float)
    
    
    def __init__(self, nome, idade, cpf, setor, funcao, salario, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        
        
# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

os.system("cls || clear")

def limpar_tela():
    os.system("cls || clear")
    

def menu():
    print("="*40)
    print(f"{"RH System":^40}")
    print("="*40)
    print("""
    1 - Adicionar um funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário 
    5 - Listar todos os funcionários
    0 - Sair do sistema.     
          """)



while True:
    menu()
    opcao = input("digite seu numero: ")
    match opcao:
        case "1": 
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            cpf_usuario = int(input("Digite seu : "))
            setor = input("Digite seu setor: ")
            funcao = input("Digite sua função: ")
            salario = float(input("Digite seu salario: "))
            telefone = int(input("Digite seu telefone: "))
            
            funcionario = Funcionario(nome=nome, idade=idade, cpf=cpf_usuario, setor=setor, funcao=funcao, salario=salario, telefone=telefone)
            session.add(funcionario)
            session.commit()
            limpar_tela()

        case "2":
            cpf_usuario = int(input("coloque seu CPF: "))
            lista_funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
            for usuario in lista_funcionario:
                print(f"{usuario.cpf} - {usuario.nome} - {usuario.idade} - {usuario.setor} - {usuario.funcao}- {usuario.salario}- {usuario.tefone}")
            limpar_tela()
            
        case "3":
            cpf_usuario = int(input("Digite o CPF: "))
            funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
            
            novos_dados = Funcionario(
            nome = input("Digite seu nome: "),
            idade = int(input("Digite sua idade: ")),
            cpf_usuario = int(input("Digite seu cpf: ")),
            setor = input("Digite seu setor: "),
            funcao = input("Digite sua função: "),
            salario = float(input("Digite seu salario: ")),
            telefone = int(input("Digite seu telefone: "))
            )

            funcionario = novos_dados
            session.add(funcionario)
            session.commit
            print("Usuário atualizado.")
            limpar_tela()
            
        case "4":
            cpf_usuario = int(input("Digite o CPF: "))
            funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
            session.delete(funcionario)
            session.commit()
            print("Usuário deletado.")
            limpar_tela()
            
        case "5":
            limpar_tela()
            
        case "0":
            break
            
            
            
                        
            
            
        
    


        
    