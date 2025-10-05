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

    def consultarSaldo(self):
        print("Saldo atual:", self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de", valor, "realizado. Novo saldo:", self.saldo)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque de", valor, "realizado. Novo saldo:", self.saldo)
        else:
            print("Saldo insuficiente!")

    def transferir(self, outraConta, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            outraConta.saldo += valor
            print("Transferência de", valor, "realizada.")
        else:
            print("Saldo insuficiente para transferência.")

class ContaPoupanca(Conta):
    def __init__(self, agencia, usuario, dataAbertura, saldo, rendimento=0.02):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.rendimento = rendimento

    def aplicarRendimento(self):
        ganho = self.saldo * self.rendimento
        self.saldo += ganho
        print("Rendimento aplicado! Ganhou:", ganho, "Novo saldo:", self.saldo)

class ContaCorrente(Conta):
    def __init__(self, agencia, usuario, dataAbertura, saldo, tarifa=10):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.tarifa = tarifa

    def descontarTarifa(self):
        self.saldo -= self.tarifa
        print("Tarifa de", self.tarifa, "reais descontada. Saldo agora é:", self.saldo)

class ContaEspecial(ContaCorrente):
    def __init__(self, agencia, usuario, dataAbertura, saldo, limite=500):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.limite = limite

    def consultarSaldo(self):
        print("Saldo disponível (com limite):", self.saldo + self.limite)

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print("Saque realizado com sucesso. Saldo atual:", self.saldo)
        else:
            print("Limite ultrapassado! Saque não realizado.")

    def transferir(self, outraConta, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            outraConta.saldo += valor
            print("Transferência de", valor, "feita com sucesso.")
        else:
            print("Não foi possível transferir, limite estourado.")

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

contaNormal = Conta(agencia, usuario, dataAbertura, saldo)
contaP = ContaPoupanca(agencia, usuario, dataAbertura, saldo)
contaC = ContaCorrente(agencia, usuario, dataAbertura, saldo)
contaE = ContaEspecial(agencia, usuario, dataAbertura, saldo)

print("\n=== TESTANDO AS CONTAS ===")
contaNormal.consultarSaldo()
contaNormal.depositar(200)
contaNormal.sacar(50)

contaP.aplicarRendimento()

contaC.descontarTarifa()

contaE.consultarSaldo()
contaE.sacar(900)
contaE.transferir(contaNormal, 100)
contaE.consultarSaldo()

class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha, numeroServidos=0):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha
        self.numeroServidos = numeroServidos

    def descreverRestaurante(self):
        print("Restaurante:", self.nomeRestaurante, "- Tipo de cozinha:", self.tipoCozinha)

    def abrirRestaurante(self):
        print(self.nomeRestaurante, "está aberto!!")

    def getNumeroServidos(self):
        return self.numeroServidos

    def setNumeroServidos(self, n):
        self.numeroServidos = n

    def incrementeNumeroServidos(self, n):
        atual = self.getNumeroServidos()
        novo = atual + n
        self.setNumeroServidos(novo)

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} | Tipo: {self.tipoCozinha} | Clientes Servidos: {self.numeroServidos}"

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

print("\n--- TESTANDO NUMERO SERVIDOS ---")
restaurante = Restaurante("Ponto da Esquina", "Nordestina")
print("Clientes atendidos:", restaurante.getNumeroServidos())

restaurante.setNumeroServidos(20)
print("Clientes atendidos agora:", restaurante.getNumeroServidos())

restaurante.incrementeNumeroServidos(5)
print("Depois de servir mais 5:", restaurante.getNumeroServidos())
