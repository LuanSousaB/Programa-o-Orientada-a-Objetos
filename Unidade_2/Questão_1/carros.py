class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro1 = Carro("Chevrolet", "Chevette", 1985, "Vermelho")
carro2 = Carro("Chevrolet", "Opala", 1990, "Azul")

print("Carro 1:")
print("Marca:", carro1.marca)
print("Modelo:", carro1.modelo)
print("Ano:", carro1.ano)
print("Cor:", carro1.cor)

print("\nCarro 2:")
print("Marca:", carro2.marca)
print("Modelo:", carro2.modelo)
print("Ano:", carro2.ano)
print("Cor:", carro2.cor)