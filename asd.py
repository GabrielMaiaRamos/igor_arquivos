import time
import random
import datetime
import numpy as np
# cores = {"padrao": "\033[m", "cinza": "\033[90m", "preto": "\033[7;30;m"}


nomes = ["Lucas", "Ana", "Pedro", "Julia", "Gabriel", "Maria", "Joao", "Larissa", "Felipe", "Camila", 
        "Rafael", "Beatriz", "Bruno", "Carolina", "Daniel",
        "Isabela", "Thiago", "Amanda", "Leonardo", "Fernanda"]
sobrenome = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima", "Carvalho", "Ferreira", "Rodrigues", "Almeida",
    "Costa", "Nascimento", "Araujo", "Barbosa", "Ribeiro", "Martins", "Gomes", "Rocha", "Teixeira", "Moura"]
numeros = np.random.choice(115000, size=115000, replace=False)

def gerar_dados():

    nome_completo = random.choice(nomes) + " " + random.choice(sobrenome)

    #gerar dependendentes aleatorios e formatar de ["A", "B"] para "A, B"
    lista_dependentes = [random.choice(nomes) for c in range(random.randint(0,3))]
    if not lista_dependentes:
        dependentes = "Nenhum"
    else:
        dependentes = ", ".join(lista_dependentes)

    #gerar data de aniversario e data de entrada aleatorios e, caso necessario, adicionar 0 no inicio
    dia_ani = random.randint(1,28)
    mes_ani = random.randint(1,12)
    ano_ani = random.randint(1935, 2007)
    ani = f"{dia_ani:02d}/{mes_ani:02d}/{ano_ani}"

    dia_entrada = random.randint(1,28)
    mes_entrada = random.randint(1,12)
    entrada = f"{dia_entrada:02d}/{mes_entrada:02d}/2025"

    #gerar idade a partir do ano aleatorio gerado
    idade = 2025-int(ano_ani)

    #se o mes do dia_atual for igual ao mes do aniversaio da pessoa, o acesso é gratuioto, se nao, 39.90 por pessoa
    gasto = "Gratuito" if int(mes_entrada) == int(mes_ani) else str(round((len(dependentes.split())+1)*39.90, 2))+"0"

    #escolhe um ID dentro dos numeros unicos
    cracha = random.choice(numeros)

    linha = [nome_completo, idade, entrada, ani, dependentes, gasto, cracha]
    return linha


def gerar_arquivo(nome_arquivo, linhas):
    #cabecalho da matriz (primeira linha)
    cabecalho = ["Nome", "Idade", "Data de Entrada", "Data de Aniversario", "Dependentes", "Gasto", "ID"]
    #comeca a contar o tempo
    inicio = time.time()
    #abre ou cria o arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:   
        #adiciona o cabecalho uma unica vez
        arquivo.write(";".join(cabecalho) + "\n")
        #escreve o resto das liinhas
        for c in range(linhas):
            linha_atual = gerar_dados()
            #formada no padrao legivel ao CSV
            linha_formatada_para_csv = ";".join(str(item) for item in linha_atual) + "\n"
            arquivo.write(linha_formatada_para_csv)
    #salva o tempo de geracao do arquivo
    tempo = time.time() - inicio
    print(f"Arquivo {nome_arquivo} gerado em {tempo:.2f} segundos.")

gerar_arquivo("pequeno.csv", 100)
gerar_arquivo("medio.csv", 1000)
gerar_arquivo("grande.csv", 10000)
gerar_arquivo("gigante.csv", 100000)

class Gerenciador_Matriz:
    #caracteristicas de cada matriz
    def __init__(self, nome_arquivo):
        self.arquivo = nome_arquivo
        self.matriz = []
        self.cabecalho = []
        self.tamanho = int
        self.carregar_matriz()
#=========================================================================================================#
    #carregar as linhas da matriz
    def carregar_matriz(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                #le as linhas removendo quebra de linha
                linhas = [linha.strip() for linha in arquivo.readlines()]
                #cabecalho = primeira linha
                self.cabecalho = linhas[0].split(";")
                #resto das linhas
                for linha_atual in linhas[1:]:
                    dados = linha_atual.split(";")
                    self.matriz.append(dados)
                self.tamanho = len(self.matriz)
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo} não encontrado!\nCertifique-se de colocar o nome correto!")



#=========================================================================================================#
    def mostrar_matriz(self):
        for linha in self.matriz:
            print(linha)
#=========================================================================================================#
    def buscar_cliente(self):
        try:
            conteudo = int(input("\n==Conteúdo da Busca==\n[1] Dados Completos\n[2] Apenas Nome, ID e Gasto" \
            "\nSelecione o conteúdo de busca que deseja: "))
            metodo = int(input("\n==Método da Busca==\n[3] Por Nome\n[4] Por ID" \
            "\nSelecione o método de busca que deseja: "))
            if metodo == 3:
                nome = input("Por favor, digite a o nome: ")
                for c in range(self.tamanho):
                    if self.matriz[c][0] == nome:
                        linha = c
                        break
                if conteudo == 1:
                    print(f"Dados Cadastrados:\n{self.matriz[linha]}")
                elif conteudo == 2:
                    print(f"Cliente: {self.matriz[linha][0]}\nID do Cliente: {self.matriz[linha][6]}\nGasto do Cliente: {self.matriz[linha][5]}")
            elif metodo == 4:
                cracha = int(input("Por favor, digite o ID do cliente: "))
                for c in range(self.tamanho):
                    if self.matriz[c][6] == str(cracha):
                        linha = c
                        break
                if conteudo == 1:
                    print(f"Dados Cadastrados:\n{self.matriz[linha]}")
                elif conteudo == 2:
                    print(f"Cliente: {self.matriz[linha][0]}\nID do Cliente: {self.matriz[linha][6]}\nGasto do Cliente: {self.matriz[linha][5]}")
        except ValueError:
            print("Erro, repita a operação com dados disponíveis")
#=========================================================================================================#
    def coletardados(self):
        #indicar nome
        nome = str(input("Digite seu nome: ").strip())
        #indicar idade
        while True:
            try:
                idade = int(input("Digite sua idade: "))
                break
            except ValueError:
                print("Digite apenas sua idade com números!")
        #indicar data de aniversario
        while True:
            aniversario = input("Digite sua data de nascimento (dd/mm/aaaa): ")
            try:
                dataniver = datetime.datetime.strptime(aniversario, "%d/%m/%Y").date()
                dataniver = dataniver.strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Formato inválido. O correto é dd/mm/aaaa.")
        #gerar data de entrada (dia atual)
        dia_entrada = datetime.datetime.now().strftime("%d/%m/%Y")
        #indicar quais sao os dependentes
        while True:
            try:
                pergunta = str(input("Você está acompanhado(a) de algum não pagante?\nResponda com Sim ou Não: ").strip().lower())
                resposta = pergunta.split()[0]
                lista_acompanhantes = []
                if resposta in ["s", "sim"]:
                    numero = int(input("Quantos dependentes estão com você? "))
                    for a in range(numero):
                        nomedep = str(input("Digite o nome do(a) dependente: "))
                        lista_acompanhantes.append(nomedep)
                elif resposta in ["n", "nao", "não"]:
                    pass
                else:
                    raise ValueError
                break
            except (ValueError, IndexError):
                print("Resposta Inválida!")

        #a partir da lista de acompanhantes, formata ["A", "B"] para "A, B" Caso a lista seja vazia, recebe "Nenhum"
        if not lista_acompanhantes:
            dependentes = "Nenhum"
        else:
            dependentes = ", ".join(lista_acompanhantes)
        #gera os gastos a partir da quantidade de pessoas
        gastos = "Gratuito" if int(dia_entrada[3:5]) == int(dataniver[3:5]) else str(round((len(dependentes.split())+1)*39.90, 2))+"0"
        #gera um ID aleatorio
        cracha = random.choice(numeros)

        return [nome, str(idade), dia_entrada, dataniver, dependentes, gastos, str(int(cracha))]
#=========================================================================================================#
    def adicionar_cliente(self):
        cliente = self.coletardados()
        if len(cliente) == 7:
            self.matriz.append(cliente)
#=========================================================================================================#
    def remover_cliente(self):
        metodo = int(input("\n==Método de Remoção==\n[1] Por Nome\n[2] Por ID" \
"\nSelecione o método que deseja: "))
        if metodo == 1:
            nome = input("Por favor, digite a o nome: ")
            for c in range(self.tamanho):
                if self.matriz[c][0] == nome:
                    linha = c
                    break
            print(f"Cliente Removido:\n{self.matriz[linha]}")
            del(self.matriz[linha])
        elif metodo == 2:
            cracha = int(input("Por favor, digite o ID do cliente: "))
            for c in range(self.tamanho):
                if self.matriz[c][6] == str(cracha):
                    linha = c
                    break
            print(f"Cliente Removido:\n{self.matriz[linha]}")
            del(self.matriz[linha])
            
#=========================================================================================================#
    def menu_interativo(self):
        while True:
            print("\n===   MENU   ===")
            print("1 - Ver clientes")
            print("2 - Buscar Cliente")
            print("3 - Novo cliente")
            print("4 - Retirar cliente")
            print("5 - Sair")
            print("")

            try:
                pergunta = int(input("O que deseja fazer? "))
            except ValueError:
                print("Erro, favor entre com um número entre 1 e 5")
                continue

            if pergunta == 1:
                self.mostrar_matriz()
            elif pergunta == 2:
                self.buscar_cliente()
            elif pergunta == 3:
                self.adicionar_cliente()
            elif pergunta == 4:
                self.remover_cliente()
            elif pergunta == 5:
                # atualizar_matriz()
                break
# #=========================================================================================================#

matriz1 = Gerenciador_Matriz("pequeno.csv")
matriz1.menu_interativo()
#     @staticmethod

#     def coletardados():
#         nome = str(input("Digite seu nome: ").strip().lower())

#         while True:
#             try:
#                 idade = int(input("Digite sua idade: "))
#                 break
#             except ValueError:
#                 print("Digite apenas sua idade com números!")

#         while True:
#             aniversario = input("Digite sua data de nascimento (dd/mm/aaaa): ")
#             try:
#                 dataniver = datetime.strptime(aniversario, "%d/%m/%Y").date()
#                 dataniver = dataniver.strftime("%d/%m/%Y")
#                 break
#             except ValueError:
#                 print("Formato inválido. O correto é dd/mm/aaaa.")

#         dia_entrada = datetime.now().strftime("%d/%m/%Y")

#         while True:
#             try:
#                 dependentes = str(input("Você está acompanhado(a) de algum não pagante?\nResponda com Sim ou Não: ").strip().lower())
#                 resposta = dependentes.split()[0]
#                 acompanhantes = []
#                 if resposta in ["s", "sim"]:
#                     numero = int(input("Quantos dependentes estão com você? "))
#                     for a in range(numero):
#                         nomedep = str(input("Digite o nome do(a) dependente: "))
#                         acompanhantes.append(nomedep)
#                 if resposta in ["n", "nao", "não"]:
#                     pass
#                 break
#             except:
#                 print("Resposta inválida. Entre com Sim ou Não.")
        
#         gastos = round((len(acompanhantes)+1)*39.90, 2)

#         return {
#         "Nome": nome,
#         "Idade": idade,
#         "Dia da Entrada": dia_entrada,
#         "Data Aniversário": dataniver,
#         "Dependentes": acompanhantes,
#         "Gasto": "Gratuito" if int(dataniver[3:5]) == int(dia_entrada[3:5]) else round((len(acompanhantes)+1)*39.90, 2)
#         }


# novo_cliente = Cliente()
# with open("pequeno.txt", "a", encoding="utf-8") as arquivo:
#     arquivo.write(str(novo_cliente.coletardados())  + "\n")



#     def menu_interativo():
#         while True:
#             print("\n===   MENU   ===")
#             print("1 - Novo cliente")
#             print("2 - Ver clientes")
#             print("3 - Retirar cliente")
#             print("4 - Sair")
#             print("")

#             try:
#                 pergunta = int(input("O que deseja fazer? "))
#             except ValueError:
#                 print("Erro, favor entre com um número entre 1 e 4")
#                 continue

#             if pergunta == 1:
#                 dados = coletardados()
#                 if dados:
#                     novo_cliente = Cliente(*dados)
#                     matriz_resposta.append(novo_cliente)
#                     print("\nCliente cadastrado com sucesso!")
            
#             elif pergunta == 2:
#                 if not matriz_resposta:
#                     print("\nNenhum cliente cadastrado ainda.")
#                 else:
#                     print("\n=== CLIENTES CADASTRADOS ===")
#                     i = 1
#                     for cliente in matriz_resposta:
#                         print("\nCliente :", i)
#                         print("Nome:", cliente.nome.title())  
#                         print("Idade:", cliente.idade)
#                         print("Data de entrada:", cliente.dia_entrada)
#                         print("Aniversário:", cliente.aniversario)
                        
                        
#                         if datetime.now().strftime("%d/%m") == datetime.strptime(cliente.aniversario, "%d/%m/%Y").strftime("%d/%m"):
#                             print("Parabéns! Hoje você não paga(;")
                            
#                         if cliente.dependentes: 
#                             print("Dependentes:", ", ".join(cliente.dependentes))
#                         else:
#                             print("Dependentes: Nenhum")
#                         i += 1

#             elif pergunta == 3:
#                 if not matriz_resposta:
#                     print("\nNenhum cliente cadastrado para remover.")
#                 else:
#                     try:
#                         num = int(input("\nDigite o número do cliente a remover: "))
#                         if 1 <= num <= len(matriz_resposta):
#                             removido = matriz_resposta.pop(num-1)
#                             print(f"\nCliente {removido.nome} removido com sucesso!")
#                         else:
#                             print("\nNúmero inválido!")
#                     except ValueError:
#                         print("\nDigite um número válido!")

#             elif pergunta == 4:
#                 print("\nSaindo do sistema...")
#                 break
            
#             else:
#                 print("\nInválido, tente novamente com número de 1 a 4")


# def coletardados():
#     try:
#         nome = str(input("Digite seu nome: ").strip().lower())
#         if not nome.replace(" ", "").isalpha():
#             print("Nome deve conter apenas letras e espaços")
#             return None
#     except:
#         print("Formato inválido para nome")
#         return None

#     try:
#         idade = int(input("Digite sua idade: "))
#         if idade <= 0:
#             print("Idade deve ser positiva")
#             return None
#     except ValueError:
#         print("Digite apenas números para idade!")
#         return None

#     while True:
#         aniversario = input("Digite sua data de nascimento (dd/mm/aaaa): ")
#         try:
#             datetime.strptime(aniversario, "%d/%m/%Y")
#             break
#         except ValueError:
#             print("Formato inválido. O correto é dd/mm/aaaa.")

#     dia_entrada = datetime.now().strftime("%d/%m/%Y")

#     while True:
#         resposta = input("Você está acompanhado(a) de algum não pagante? (Sim/Não): ").lower().strip()
#         if resposta in ["sim", "s", "não", "nao", "n"]:
#             break
#         else:
#             print("Resposta inválida. Responda com Sim ou Não.")

#     dependentes = []
#     if resposta.startswith("s"):
#         try:
#             numero = int(input("Quantos dependentes estão com você? "))
#             for i in range(numero):
#                 nome_dep = input(f"{i + 1}º dependente: ")
#                 dependentes.append(nome_dep)
#         except ValueError:
#             print("Digite um número válido para quantidade de dependentes!")
#             return None

#     return nome, idade, dia_entrada, aniversario, dependentes

# Cliente.menu_interativo()