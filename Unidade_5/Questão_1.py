from datetime import datetime
import random

class Usuario:
    def __init__(self, rg=0, cpf=0, nome="Sem nome", dataNascimento=datetime.now()):
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento

    def set_rg(self, rg):
        self.rg = rg

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_nome(self, nome):
        self.nome = nome

    def set_dataNascimento(self, data):
        self.dataNascimento = data

    def get_rg(self):
        return self.rg

    def get_cpf(self):
        return self.cpf

    def get_nome(self):
        return self.nome

    def get_dataNascimento(self):
        return self.dataNascimento

class Conta:
    def __init__(self, agencia, usuario, dataAbertura, saldo):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    def get_agencia(self):
        return self.agencia

    def get_usuario(self):
        return self.usuario

    def get_dataAbertura(self):
        return self.dataAbertura

    def get_saldo(self):
        return self.saldo


print("CADASTRO DE USUÁRIO")


usuario = Usuario()


rg = int(input("Digite o RG: "))
cpf = int(input("Digite o CPF: "))
nome = input("Digite o nome: ")
dataNascTexto = input("Digite a data de nascimento (dd/mm/aaaa): ")


dataNasc = datetime.strptime(dataNascTexto, "%d/%m/%Y")

usuario.set_rg(rg)
usuario.set_cpf(cpf)
usuario.set_nome(nome)
usuario.set_dataNascimento(dataNasc)


agencia = random.randint(0, 999)
dataAbertura = datetime.now()
saldo = float(input("Digite o saldo inicial: "))

conta = Conta(agencia, usuario, dataAbertura, saldo)


print("\n==== DADOS DA CONTA ====")
print("Agência:", conta.get_agencia())
print("Saldo:", conta.get_saldo())
print("Data de Abertura:", conta.get_dataAbertura())
print("\n--- DADOS DO USUÁRIO ---")
print("Nome:", conta.get_usuario().get_nome())
print("RG:", conta.get_usuario().get_rg())
print("CPF:", conta.get_usuario().get_cpf())
print("Data de Nascimento:", conta.get_usuario().get_dataNascimento())

class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def descreverRestaurante(self):
        print("Restaurante:", self.nomeRestaurante, "- Tipo de cozinha:", self.tipoCozinha)

    def abrirRestaurante(self):
        print(self.nomeRestaurante, "está aberto!!")

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} | Tipo: {self.tipoCozinha}"


local1 = Restaurante("Comidas Brasileira", "Caseira")
local2 = Restaurante("Massas quentes", "Italiana")
local3 = Restaurante("Sushi", "Japonesa")


print("\n--- DESCRIÇÕES ---")
local1.descreverRestaurante()
local2.descreverRestaurante()
local3.descreverRestaurante()


print("\n--- USANDO __str__ ---")
print(local1)
print(local2)
print(local3)


print()
local1.abrirRestaurante()
