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
    telefone = Column("telefone", String)  # Corrigi aqui, porque o telefone geralmente tem mais dígitos e deve ser String.
    
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

# Função para limpar a tela
def limpar_tela():
    os.system("cls || clear")

# Função para exibir o menu
def menu():
    print("="*40)
    print(f"{'RH System':^40}")
    print("="*40)
    print("""
    1 - Adicionar um funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário 
    5 - Listar todos os funcionários
    0 - Sair do sistema.     
          """)

# Loop principal do sistema
while True:
    menu()
    opcao = input("Digite o número da opção: ")

    match opcao:
        case "1":  # Adicionar funcionário
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            cpf_usuario = int(input("Digite o CPF: "))
            setor = input("Digite o setor: ")
            funcao = input("Digite a função: ")
            salario = float(input("Digite o salário: "))
            telefone = input("Digite o telefone: ")
            
            funcionario = Funcionario(nome=nome, idade=idade, cpf=cpf_usuario, setor=setor, funcao=funcao, salario=salario, telefone=telefone)
            session.add(funcionario)
            session.commit()
            print("Funcionário adicionado com sucesso!")
            limpar_tela()

        case "2":  # Consultar funcionário
            cpf_usuario = int(input("Digite o CPF: "))
            funcionario = session.query(Funcionario).filter_by(cpf=cpf_usuario).first()
            
            if funcionario:
                print(f"CPF: {funcionario.cpf}, Nome: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}, Função: {funcionario.funcao}, Salário: {funcionario.salario}, Telefone: {funcionario.telefone}")
            else:
                print(f"Funcionário com CPF {cpf_usuario} não encontrado.")
            
            input("Pressione Enter para continuar...")
            limpar_tela()

        case "3":  # Atualizar funcionário
            cpf_usuario = int(input("Digite o CPF do funcionário que deseja atualizar: "))
            funcionario = session.query(Funcionario).filter_by(cpf=cpf_usuario).first()
            
            if funcionario:
                funcionario.nome = input(f"Digite o novo nome (atual: {funcionario.nome}): ") or funcionario.nome
                funcionario.idade = int(input(f"Digite a nova idade (atual: {funcionario.idade}): ") or funcionario.idade)
                funcionario.setor = input(f"Digite o novo setor (atual: {funcionario.setor}): ") or funcionario.setor
                funcionario.funcao = input(f"Digite a nova função (atual: {funcionario.funcao}): ") or funcionario.funcao
                funcionario.salario = float(input(f"Digite o novo salário (atual: {funcionario.salario}): ") or funcionario.salario)
                funcionario.telefone = input(f"Digite o novo telefone (atual: {funcionario.telefone}): ") or funcionario.telefone
                
                session.commit()
                print("Funcionário atualizado com sucesso!")
            else:
                print(f"Funcionário com CPF {cpf_usuario} não encontrado.")
            
            input("Pressione Enter para continuar...")
            limpar_tela()

        case "4":  # Excluir funcionário
            cpf_usuario = int(input("Digite o CPF do funcionário que deseja excluir: "))
            funcionario = session.query(Funcionario).filter_by(cpf=cpf_usuario).first()
            
            if funcionario:
                session.delete(funcionario)
                session.commit()
                print("Funcionário excluído com sucesso!")
            else:
                print(f"Funcionário com CPF {cpf_usuario} não encontrado.")
            
            input("Pressione Enter para continuar...")
            limpar_tela()

        case "5":  # Listar todos os funcionários
            funcionarios = session.query(Funcionario).all()
            if funcionarios:
                print("Lista de funcionários:")
                for func in funcionarios:
                    print(f"CPF: {func.cpf}, Nome: {func.nome}, Idade: {func.idade}, Setor: {func.setor}, Função: {func.funcao}, Salário: {func.salario}, Telefone: {func.telefone}")
            else:
                print("Nenhum funcionário cadastrado.")
            
            input("Pressione Enter para continuar...")
            limpar_tela()

        case "0":  # Sair
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida!")
            limpar_tela()

