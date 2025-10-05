class Veiculo:
    total_veiculos = 0

    def __init__(self, placa, modelo, diaria):
        self.__placa = placa
        self.modelo = modelo
        self.diaria = diaria
        self.__alugado = False
        Veiculo.total_veiculos += 1

    def alugar(self):
        if not self.__alugado:
            self.__alugado = True
            print("Veículo alugado com sucesso!")
        else:
            print("Esse veículo já está alugado!")

    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            print("Veículo devolvido com sucesso!")
        else:
            print("Esse veículo já está disponível!")

    def status(self):
        if self.__alugado:
            print("Status: Alugado")
        else:
            print("Status: Disponível")

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        print("A placa não pode ser alterada!")

    @classmethod
    def mostrar_total_veiculos(cls):
        print("Total de veículos cadastrados:", cls.total_veiculos)

    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
        return dias * diaria