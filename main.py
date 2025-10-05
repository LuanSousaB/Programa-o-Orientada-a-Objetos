from veiculo import Veiculo

print("=== LOCADORA DE VEÍCULOS ===")

v1 = Veiculo("OIU2100", "Chevette", 200.0)
v2 = Veiculo("LUC9283", "Opala", 150.0)

print("\n--- STATUS INICIAL ---")
v1.status()
v2.status()

print("\n--- ALUGANDO VEÍCULO 1 ---")
v1.alugar()
v1.status()

print("\n--- DEVOLVENDO VEÍCULO 1 ---")
v1.devolver()
v1.status()

print("\n--- TESTE DE PLACA (ENCAPSULAMENTO) ---")
print("Placa do veículo 1:", v1.placa)
v1.placa = "AAA0000"

print("\n--- TOTAL DE VEÍCULOS ---")
Veiculo.mostrar_total_veiculos()

print("\n--- CALCULAR PREÇO DO ALUGUEL ---")
dias = 5
preco = Veiculo.calcular_preco_aluguel(dias, v2.diaria)
print("Valor do aluguel por", dias, "dias do", v2.modelo, "é R$", preco)
