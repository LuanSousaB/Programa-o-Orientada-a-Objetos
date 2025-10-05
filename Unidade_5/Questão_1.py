from abc import ABC, abstractmethod

class CartaoWeb(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    @abstractmethod
    def showMessage(self):
        pass


class DiaDosNamorados(CartaoWeb):
    def __init__(self, destinatario):
        super().__init__(destinatario)

    def showMessage(self):
        print("Feliz Dia dos Namorados,", self.destinatario + "!")
        print("Te desejo muito amor e carinho nesse dia especial 💖")


class Natal(CartaoWeb):
    def __init__(self, destinatario):
        super().__init__(destinatario)

    def showMessage(self):
        print("Feliz Natal,", self.destinatario + "!")
        print("Que seu Natal seja cheio de alegria e presentes 🎄")


class Aniversario(CartaoWeb):
    def __init__(self, destinatario):
        super().__init__(destinatario)

    def showMessage(self):
        print("Feliz Aniversário,", self.destinatario + "!")
        print("Parabéns por mais um ano de vida 🎂")

print("=== CARTÕES WEB ===")

cartao = DiaDosNamorados("Luan")
cartao.showMessage()

print()
cartao = Natal("Luan")
cartao.showMessage()

print()
cartao = Aniversario("Luan")
cartao.showMessage()

#O polimorfismo acontece porque a mesma variável pode chamar o mesmo método (showMessage) em objetos diferentes,
#e cada classe filha executa o seu próprio comportamento.

class MetodoPagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        pass


class CartaoCredito(MetodoPagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def pagar(self):
        total = self.valor * 1.05
        print("Pagamento com Cartão de Crédito")
        print("Valor original:", self.valor)
        print("Valor final com taxa de 5%:", total)


class BoletoBancario(MetodoPagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def pagar(self):
        total = self.valor * 0.98
        print("Pagamento com Boleto Bancário")
        print("Valor original:", self.valor)
        print("Valor final com 2% de desconto:", total)


class Pix(MetodoPagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def pagar(self):
        print("Pagamento via PIX")
        print("Valor total:", self.valor)


print("\n=== SISTEMA DE PAGAMENTO ===")

valor = float(input("Digite o valor da compra: "))
print("Escolha o método de pagamento:")
print("1 - Cartão de Crédito")
print("2 - Boleto Bancário")
print("3 - Pix")

opcao = int(input("Opção: "))

pagamento = None

if opcao == 1:
    pagamento = CartaoCredito(valor)
elif opcao == 2:
    pagamento = BoletoBancario(valor)
elif opcao == 3:
    pagamento = Pix(valor)
else:
    print("Opção inválida!")

if pagamento:
    pagamento.pagar()

#O polimorfismo permite usar uma única variável para diferentes formas de pagamento, 
#chamando o método pagar() de cada classe sem precisar saber qual tipo de pagamento foi escolhido.
