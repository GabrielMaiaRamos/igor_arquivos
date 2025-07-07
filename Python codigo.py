# import random
# colunas = {
#     "Nome": str,
#     "Idade": int,
#     "Preço Quarto": float,
#     "Contatos": list,
#     "Check-in": str
# }

# def gerar_dados_aleatorios():
#     nomes = ["João", "Maria", "Carlos", "Ana", "Pedro"]
#     return {
#         "Nome": random.choice(nomes),
#         "Idade": random.randint(18, 80),
#         "Preço Quarto": round(random.uniform(100, 500), 2),
#         "Contatos": [f"9{random.randint(10000000, 99999999)}" for _ in range(2)],
#         "Check-in": f"{random.randint(1, 31):02d}/{random.randint(1, 12):02d}/2024"
#     }

# # Exemplo 1: Printar apenas os nomes das colunas
# print("Colunas disponíveis:")
# for coluna in colunas.keys():
#     print(f"- {coluna}")

# print("\n" + "="*50 + "\n")

# # Exemplo 2: Printar colunas com seus tipos
# print("Colunas e seus tipos:")
# for coluna, tipo in colunas.items():
#     print(f"{coluna}: {tipo.__name__}")

# print("\n" + "="*50 + "\n")

# # Exemplo 3: Gerar e printar dados aleatórios
# dados = gerar_dados_aleatorios()
# print("Dados gerados:")
# for coluna, valor in dados.items():
#     print(f"{coluna}: {valor}")

# print("\n" + "="*50 + "\n")

# # Exemplo 4: Printar de forma mais organizada (tabela simples)
# print("Formato de tabela:")
# print(f"{'Coluna':<15} {'Valor':<20}")
# print("-" * 35)
# for coluna, valor in dados.items():
#     print(f"{coluna:<15} {str(valor):<20}")