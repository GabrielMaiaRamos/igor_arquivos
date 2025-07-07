import time
import random
import datetime
import numpy as np
from cores import cores
from cores import linha_menu
from cores import solicitar
from cores import erro
from cores import resultado

nomes = ["Lucas", "Ana", "Pedro", "Julia", "Gabriel", "Maria", "João", "Larissa", "Felipe", "Camila", 
         "Rafael", "Beatriz", "Bruno", "Carolina", "Daniel", "Isabela", "Thiago", "Amanda", "Leonardo", "Fernanda",
         "Mateus", "Letícia", "Gustavo", "Mariana", "André", "Sophia", "Rodrigo", "Vitória", "Diego", "Alice",
         "Eduardo", "Helena", "Vinicius", "Manuela", "Victor", "Júlia", "Henrique", "Giovanna", "Caio", "Luana",
         "Marcelo", "Yasmin", "Arthur", "Gabriela", "Fábio", "Nicole", "Otávio", "Melissa", "Renato", "Bianca"]
sobrenome = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima", "Carvalho", "Ferreira", "Rodrigues", "Almeida",
             "Costa", "Nascimento", "Araújo", "Barbosa", "Ribeiro", "Martins", "Gomes", "Rocha", "Teixeira", "Moura",
             "Dias", "Ramos", "Cardoso", "Machado", "Freitas", "Lopes", "Rezende", "Monteiro", "Mendes", "Cavalcanti",
             "Castro", "Correia", "Pinto", "Farias", "Campos", "Moreira", "Cunha", "Pires", "Andrade", "Melo",
             "Franco", "Nunes", "Barros", "Duarte", "Vieira", "Coelho", "Miranda", "Azevedo", "Siqueira", "Fonseca"]
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


def gerar_arquivo(nome_arquivo, linhas, nome_historico):
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
    #gerar o txt para guardar o histórico
    with open(nome_historico, "w", encoding="utf-8") as historico:
        historico.write(f"Tempo de criação do arquivo {nome_arquivo} = {tempo:.2f} segundos\n")

gerar_arquivo("pequeno.csv", 100, "hist_pequeno.txt")
gerar_arquivo("medio.csv", 1000, "hist_medio.txt")
gerar_arquivo("grande.csv", 10000, "hist_grande.txt")
gerar_arquivo("gigante.csv", 100000, "hist_gigante.txt")

class Gerenciador_Matriz:
    #caracteristicas de cada matriz
    def __init__(self, nome_arquivo, nome_historico):
        self.historico = nome_historico
        self.arquivo = nome_arquivo
        self.matriz = []
        self.cabecalho = []
        self.tamanho = int
        self.carregar_matriz()
#=========================================================================================================#
    #carregar as linhas da matriz e contar o tempo que leva
    def carregar_matriz(self):
        try:
            inicio = time.time()
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
            tempo = time.time() - inicio
            #escrever o tempo no historico do arquivo
            with open(self.historico, "a", encoding="utf-8") as historico:
                historico.write(f"Tempo de formatação do '{self.arquivo}' em matriz no Python = {tempo:.2f} segundos\n")
        #caso nao existe o nome do arquivo, da erro
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo} não encontrado!\nCertifique-se de colocar o nome correto!")
#=========================================================================================================#
    def mostrar_matriz(self):
        for linha in self.matriz: #pra cada linha da matriz, da um print
            print(linha)
#=========================================================================================================#
    def encontrar_linha(self, n, metodo):
    #uma funcao pra, a partir de um tipo de busca (por nome ou id) encontre a linha da matriz que esse parametro esta contido
        try:
            parametro = metodo
            #incializo a linha_correpondente como False (caso nao existe o paramtro na matriz)
            linha_correpondente = False
            if n == 1:
                for linha in range((self.tamanho)+1):
                    #se eu chegar ao fim da matriz, redireciono ao except com o problema (nome nao esta na lista)
                    if linha == self.tamanho:
                        raise ValueError(f"o nome '{metodo}' não está na lista!")
                    #se o meu parametro for igual à algum elemento que esteja na coluna 0 (nomes), entao eu salvo essa linha
                    elif self.matriz[linha][0] == parametro:
                        linha_correpondente = linha
                        break
            #mesma coisa que a anterior, mas agora o parametro é a ID, entao vou comparar com elementos da coluna 6 (IDs)
            elif n == 2:
                for linha in range((self.tamanho)+1):
                    if linha == self.tamanho:
                        #como no if anterior, mas agora o problema enviado é (ID nao estao na lista)
                        raise ValueError(f"o ID: '{metodo}' não está na lista!")
                    elif self.matriz[linha][6] == str(parametro):
                        linha_correpondente = linha
                        break
            return linha_correpondente
        #se vier pro except, printa o problema
        except ValueError as problema:
            print(f"{cores["erro"]}Erro, {problema}{cores["reset"]}")
#=========================================================================================================#
    def buscar_cliente(self):
        try:
            #pergunto o metodo (por nome ou ID) e o conteudo que deseja ver sobre o cliente (tudo ou apenas nome, id e gasto)
            print(f"\n===  Método da Busca  ===\n{linha_menu(1, "Por Nome")}\n{linha_menu(2, "Por ID")}\n")
            metodo = int(input(solicitar("Selecione o método de busca que deseja: ")))
            print(f"\n=== Conteúdo da Busca ===\n{linha_menu(3, "Dados Completos")}\n{linha_menu(4, "Apenas Nome, ID e Gasto")}")
            conteudo = int(input(solicitar("Selecione o conteúdo de busca que deseja: ")))
            #se escolher por nome, peço o nome e jogo pra funcao de encontrar_linhas
            if metodo == 1:
                nome = input(solicitar("Por favor, digite o nome do Cliente: "))
                linha = self.encontrar_linha(1, nome)
                #se escolheu conteudo todo, printo toda a linha da matriz (obs: em todos os casos, a linha tem ter um valor, por isso "and linha")
                if conteudo == 3 and linha:
                    print(resultado("\nDados Cadastrados:\n", self.matriz[linha]))
                #se escolheu apenas nome, id, gasto, entao so printo as colunas 0 (nome), 6(id), 5(gasto)
                elif conteudo == 4 and linha:
                    print(resultado("\nCliente: ", self.matriz[linha][0]))
                    print(resultado("ID do Cliente: ", self.matriz[linha][6]))
                    print(resultado("Gasto do Cliente: ", self.matriz[linha][5]))
            #se escolher por id, faço examente as mesmas coisas de antes, so que peço o ID ao inves do nome e jogo pra funcao encontrar_linha
            elif metodo == 2:
                cracha = int(input(solicitar("Por favor, digite o ID do cliente: ")))
                linha = self.encontrar_linha(2,cracha)
                if conteudo == 3 and linha:
                    print(resultado("\nDados Cadastrados:\n", self.matriz[linha]))
                elif conteudo == 4 and linha:
                    print(resultado("\nCliente: ", self.matriz[linha][0]))
                    print(resultado("ID do Cliente: ", self.matriz[linha][6]))
                    print(resultado("Gasto do Cliente: ", self.matriz[linha][5]))
        #erro que abrange os valores inesperados (onde deveria ser int, ser str e etc)
        except ValueError:
            print(erro("Erro, digite valores válidos!"))
#=========================================================================================================#
    def coletardados(self):
        #indicar nome
        nome = str(input(solicitar("Digite seu nome: "))).strip()
        #indicar idade
        while True:
            try:
                idade = int(input(solicitar("Digite sua idade: ")))
                break
            except ValueError:
                print(erro("Digite apenas sua idade com números!"))
        #indicar data de aniversario
        while True:
            aniversario = input(solicitar("Digite sua data de nascimento (dd/mm/aaaa): "))
            try:
                dataniver = datetime.datetime.strptime(aniversario, "%d/%m/%Y").date()
                dataniver = dataniver.strftime("%d/%m/%Y")
                break
            except ValueError:
                print(erro("Formato inválido. O correto é dd/mm/aaaa."))
        #gerar data de entrada (dia atual)
        dia_entrada = datetime.datetime.now().strftime("%d/%m/%Y")
        #indicar quais sao os dependentes
        while True:
            try:
                pergunta = str(input(solicitar("Você está acompanhado(a) de algum não pagante?\nResponda com Sim ou Não: ")).strip().lower())
                resposta = pergunta.split()[0]
                lista_acompanhantes = []
                if resposta in ["s", "sim"]:
                    numero = int(input(solicitar("Quantos dependentes estão com você? ")))
                    for a in range(numero):
                        nomedep = str(input(solicitar("Digite o nome do(a) dependente: ")))
                        lista_acompanhantes.append(nomedep)
                elif resposta in ["n", "nao", "não"]:
                    pass
                else:
                    raise ValueError
                break
            except (ValueError, IndexError):
                print(erro("Resposta Inválida!"))

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
        #busco todos os dados pela funcao de coleta
        cliente = self.coletardados()
        #se tiver 7 dados certinho (nome, idade, entrada, aniversario, dependenetes, gastos, cracha) entao eu adicino na matriz
        if len(cliente) == 7:
            self.matriz.append(cliente)
            self.tamanho += 1 #aumento o tamanho da matriz em 1
#=========================================================================================================#
    def remover_cliente(self):
        print(f"\n===  Método de Remoção  ===\n{linha_menu(1, "Por Nome")}\n{linha_menu(2, "Por ID")}\n")
        #pergunto o metodo de remocao (por nome ou id)
        metodo = int(input(solicitar("Selecione o método que deseja: ")))
        #caso escolha por nome, pergunto o nome e jogo pra funcao de encontrar_linha desse nome
        if metodo == 1:
            nome = input(solicitar("Por favor, digite o nome: "))
            linha = self.encontrar_linha(1, nome)
            #se o nome existir, entao eu deleto (del) a linha da matriz
            if linha:
                print(resultado("\nCliente Removido:\n", self.matriz[linha]))
                del(self.matriz[linha])
                self.tamanho -= 1 #reduzo o tamanho da matriz em 1
        #caso escolha por id, faço o mesmo que anteriomente, mas jogo o id na funcao de encontrar_linhas
        elif metodo == 2:
            cracha = input(solicitar("Por favor, digite o ID do cliente: "))
            linha = self.encontrar_linha(2, cracha)
            if linha:
                print(resultado("\nCliente Removido:\n", self.matriz[linha]))
                del(self.matriz[linha])
                self.tamanho -= 1
#=========================================================================================================#
    def menu_interativo(self):
        while True:
            print("\n=====   MENU   =====")
            print(linha_menu(1, "Ver Clientes"))
            print(linha_menu(2, "Buscar Clientes"))
            print(linha_menu(3, "Adicionar Clientes"))
            print(linha_menu(4, "Retirar Clientes"))
            print(linha_menu(5, "Sair"))
            print("")

            try:
                #pergnto o que ele quer (nao pode ser maior que 6, nem diferente de inteiro)
                pergunta = int(input(solicitar("O que deseja fazer? ")))
                #forço os inputs maiores que 6 para o except
                if pergunta >= 6:
                    raise ValueError
            #uso o except pra ficar voltando pro inicio (com o continue) toda vez que o input vier em formato indesejado
            except ValueError:
                print(erro("Erro, favor escolha um número entre 1 e 5"))
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

matriz1 = Gerenciador_Matriz("pequeno.csv", "hist_pequeno.txt")
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