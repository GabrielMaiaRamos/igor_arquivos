import time
import random
import datetime
import numpy as np
#importando minha biblioteca com cores e padroes
from cores import cores
from cores import linha_menu
from cores import solicitar
from cores import erro
from cores import resultado
#==========================================================================================================================#
#dicionarios de nome, sobrenome e numeros unicos para o cracha
nomes = ["Lucas", "Ana", "Pedro", "Julia", "Gabriel", "Maria", "Joao", "Larissa", "Felipe", "Camila", 
         "Rafael", "Beatriz", "Bruno", "Carolina", "Daniel", "Isabela", "Thiago", "Amanda", "Leonardo", "Fernanda",
         "Mateus", "Leticia", "Gustavo", "Mariana", "Andre", "Sophia", "Rodrigo", "Vitoria", "Diego", "Alice",
         "Eduardo", "Helena", "Vinicius", "Manuela", "Victor", "Julia", "Henrique", "Giovanna", "Caio", "Luana",
         "Marcelo", "Yasmin", "Arthur", "Gabriela", "Fabio", "Nicole", "Otavio", "Melissa", "Renato", "Bianca"]
sobrenome = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima", "Carvalho", "Ferreira", "Rodrigues", "Almeida",
             "Costa", "Nascimento", "Araujo", "Barbosa", "Ribeiro", "Martins", "Gomes", "Rocha", "Teixeira", "Moura",
             "Dias", "Ramos", "Cardoso", "Machado", "Freitas", "Lopes", "Rezende", "Monteiro", "Mendes", "Cavalcanti",
             "Castro", "Correia", "Pinto", "Farias", "Campos", "Moreira", "Cunha", "Pires", "Andrade", "Melo",
             "Franco", "Nunes", "Barros", "Duarte", "Vieira", "Coelho", "Miranda", "Azevedo", "Siqueira", "Fonseca"]
numeros = np.random.choice(115000, size=115000, replace=False)
#==========================================================================================================================#
#funcao para gerar dados de clientes aleatorios
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
#==========================================================================================================================#
#funcao para gerar os 4 arquivos e os 4 historicos a partir dos dados aleatorios
def gerar_arquivo(nome_arquivo, linhas, nome_historico):
    #cabecalho da matriz (primeira linha)
    cabecalho = ["Nome", "Idade", "Data de Entrada", "Data de Aniversario", "Dependentes", "Gasto", "ID"]
    #comeca a contar o tempo
    inicio = time.time()
    #abre ou cria o arquivo com encoding especifico para Excel
    with open(nome_arquivo, "w", encoding="utf-8-sig", newline='') as arquivo:
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
    with open(nome_historico, "w", encoding="utf-8-sig", newline='') as historico:
        historico.write(f"Tempo de criacao do arquivo {nome_arquivo} = {tempo:.6f} segundos\n")
#==========================================================================================================================#
#class para criar matrizes e manipular elas
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
    #funcao para carregar as linhas da matriz na caracteristica "self.matriz"
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
            with open(self.historico, "a", encoding="utf-8-sig") as historico:
                historico.write(f"Tempo de formatacao do '{self.arquivo}' em matriz no Python = {tempo:.6f} segundos\n")
        #caso nao existe o nome do arquivo, da erro
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo} nao encontrado!\nCertifique-se de colocar o nome correto!")
#=========================================================================================================#
    def mostrar_matriz(self):
        inicio = time.time()
        for linha in self.matriz: #pra cada linha da matriz, da um print
            print(linha)
        tempo = time.time() - inicio
        #escrever o tempo no historico do arquivo
        with open(self.historico, "a", encoding="utf-8-sig") as historico:
            historico.write(f"\n Tempo de mostrar a matriz do arquivo: '{self.arquivo}' em Python = {tempo:.6f} segundos\n")
#=========================================================================================================#
    def encontrar_linha(self, n, metodo):
    #uma funcao pra, a partir de um tipo de busca (por nome ou id) encontre a linha da matriz que esse parametro esta contido
        try:
            parametro = metodo
            #incializo a linha_correpondente como False (caso nao existe o paramtro na matriz)
            linha_correpondente = False
            if n == 1:
                #uso o "for else" pra ver se o nome existe na matriz, se nao, forca o erro
                for linha in range(self.tamanho):
                    #se o meu parametro for igual à algum elemento que esteja na coluna 0 (nomes), entao eu salvo essa linha
                    if self.matriz[linha][0] == parametro:
                        linha_correpondente = linha
                        break
                else:
                    raise ValueError(f"o nome '{metodo}' não está na lista!")
            #mesma coisa que a anterior, mas agora o parametro é a ID, entao vou comparar com elementos da coluna 6 (IDs)
            elif n == 2:
                for linha in range(self.tamanho):
                    if self.matriz[linha][6] == str(parametro):
                        linha_correpondente = linha
                        break
                else:
                    raise ValueError(f"o ID: '{metodo}' não está na lista!")
        
            return linha_correpondente
        #se vier pro except, printa o problema
        except ValueError as problema:
            print(f"{cores["erro"]}Erro, {problema}{cores["reset"]}")
            return False  # Retorna False em caso de erro
#=========================================================================================================#
    def buscar_cliente(self):
        while True:
            try:
                #pergunto o metodo (por nome ou ID) e o conteudo que deseja ver sobre o cliente (tudo ou apenas nome, id e gasto)
                print(f"\n===  Método da Busca  ===\n{linha_menu(1, "Por Nome")}\n{linha_menu(2, "Por ID")}\n")
                metodo = int(input(solicitar("Selecione o método de busca que deseja: ")))
                if metodo not in [1,2]:
                    raise IndexError("Escolha entre [1] e [2]")
                print(f"\n=== Conteúdo da Busca ===\n{linha_menu(3, "Dados Completos")}\n{linha_menu(4, "Apenas Nome, ID e Gasto")}")
                conteudo = int(input(solicitar("Selecione o conteúdo de busca que deseja: ")))
                if conteudo not in [3,4]:
                    raise IndexError("Escolha entre [3] e [4]")
                #se escolher por nome, peco o nome e jogo pra funcao de encontrar_linhas
                if metodo == 1:
                    nome = input(solicitar("Por favor, digite o nome do Cliente: "))
                    #se o nome nao for com letras, forca o erro
                    if not ("".join(nome.split())).isalpha():
                        raise IndexError("Digite o nome apenas com letras!")
                    inicio = time.time()
                    linha = self.encontrar_linha(1, nome)
                    tempo = time.time() - inicio
                    #se escolheu conteudo todo, printo toda a linha da matriz (obs: em todos os casos, coloco "is not False" pois se a funcao encontrar_linha retornar False,
                    # entao nem entra, e se ela retornar 0 (primeira linha) o "is not False" nao reconhece o 0 como False, mas se fosse "and linha", ele reconheceria, entao estrito
                    #para que seja EXATAMENTE False, e nao os outros tipos de valores que sao "Falsos" no python
                    if conteudo == 3 and linha is not False:
                        print(resultado("\nDados Cadastrados:\n", self.matriz[linha]))
                        #atualizo o arquivo de historico
                        with open(self.historico, "a", encoding="utf-8-sig") as historico:
                            historico.write(f"\nLinha buscada: {self.matriz[linha]}\nTempo de busca: = {tempo:.6f} segundos\n")
                    #se escolheu apenas nome, id, gasto, entao so printo as colunas 0 (nome), 6(id), 5(gasto)
                    elif conteudo == 4 and linha is not False:
                        print(resultado("\nCliente: ", self.matriz[linha][0]))
                        print(resultado("ID do Cliente: ", self.matriz[linha][6]))
                        print(resultado("Gasto do Cliente: ", self.matriz[linha][5]))
                        #atualzio o arquivo de historico
                        with open(self.historico, "a", encoding="utf-8-sig") as historico:
                            historico.write(f"\n Conteúdo buscado: {self.matriz[linha][0]}, {self.matriz[linha][6]}, {self.matriz[linha][5]}\n"
                                            f" Tempo de busca: = {tempo:.6f} segundos\n")
                #se escolher por id, faco examente as mesmas coisas de antes, so que peco o ID ao inves do nome e jogo pra funcao encontrar_linha
                elif metodo == 2:
                    cracha = int(input(solicitar("Por favor, digite o ID do cliente: ")))
                    inicio = time.time()
                    linha = self.encontrar_linha(2,cracha)
                    tempo = time.time() - inicio
                    if conteudo == 3 and linha is not False:
                        print(resultado("\nDados Cadastrados:\n", self.matriz[linha]))
                        with open(self.historico, "a", encoding="utf-8-sig") as historico:
                            historico.write(f"\nLinha buscada: {self.matriz[linha]}\nTempo de busca: = {tempo:.6f} segundos\n")
                    elif conteudo == 4 and linha is not False:
                        print(resultado("\nCliente: ", self.matriz[linha][0]))
                        print(resultado("ID do Cliente: ", self.matriz[linha][6]))
                        print(resultado("Gasto do Cliente: ", self.matriz[linha][5]))
                        with open(self.historico, "a", encoding="utf-8-sig") as historico:
                            historico.write(f"\n Conteúdo buscado: {self.matriz[linha][0]}, {self.matriz[linha][6]}, {self.matriz[linha][5]}\n"
                                            f" Tempo de busca: = {tempo:.6f} segundos\n")
                break
            #erro que abrange os problemas acima
            except IndexError as problema:
                print(f"{cores["erro"]}Erro, {problema}{cores["reset"]}")
            except ValueError:
                print(erro("Reposta inválida!"))
#=========================================================================================================#
    def coletardados(self):
        while True:
            try:
                #indicar nome (retiro os espacos pra verirficar se so tem letra)
                nome = input(solicitar("Digite seu nome: "))
                if not ("".join(nome.split())).isalpha():
                    raise ValueError
                break
            except ValueError:
                print(erro("Digite seu nome apenas com letras!"))
        while True:
            try:
                #indicar idade
                idade = int(input(solicitar("Digite sua idade: ")))
                break
            except ValueError:
                print(erro("Digite sua idade apenas com números!"))
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
                pergunta = str(input(solicitar("\nVocê está acompanhado(a) de algum não pagante?\nResponda com Sim ou Não: ")).strip().lower())
                resposta = pergunta.split()[0]
                lista_acompanhantes = []
                if resposta in ["s", "sim"]:
                    numero = int(input(solicitar("Quantos dependentes estão com você? ")))
                    while True:
                        try:
                            for a in range(numero):
                                nomedep = input(solicitar("Digite o nome do(a) dependente: "))
                                if not ("".join(nomedep.split())).isalpha():
                                    raise ValueError
                                lista_acompanhantes.append(nomedep)
                            break
                        except ValueError:
                            print(erro("Digite o nome dos dependentes apenas com letras!"))
                elif resposta in ["n", "nao", "não"]:
                    pass
                else:
                    raise ValueError
                break
            except (ValueError, IndexError):
                print(erro("Responda inválida!"))
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
        inicio = time.time()
        if len(cliente) == 7:
            self.matriz.append(cliente)
            self.tamanho += 1 #aumento o tamanho da matriz em 1
            tempo = time.time() - inicio
            #escrever o tempo no historico do arquivo
            with open(self.historico, "a", encoding="utf-8-sig") as historico:
                historico.write(f"\n Cliente adicionado: {cliente}\n Tempo para adicao: {tempo:.6f} segundos\n")
#=========================================================================================================#
    def remover_cliente(self):
        while True:
            try:
                print(f"\n===  Método de Remocao  ===\n{linha_menu(1, "Por Nome")}\n{linha_menu(2, "Por ID")}\n")
                #pergunto o metodo de remocao (por nome ou id)
                metodo = int(input(solicitar("Selecione o método que deseja: ")))
                if metodo not in [1,2]:
                    raise IndexError("Escolha entre [1] e [2]")
                #caso escolha por nome, pergunto o nome e jogo pra funcao de encontrar_linha desse nome
                if metodo == 1:
                    nome = input(solicitar("Por favor, digite o nome: "))
                    #se nao for um NOME, forca o erro
                    if not ("".join(nome.split())).isalpha():
                        raise IndexError("Digite o nome apenas com letras!")
                    inicio = time.time()
                    linha = self.encontrar_linha(1, nome)
                    tempo = time.time() - inicio
                    #se o nome existir, entao eu deleto (del) a linha da matriz
                    if linha is not False:
                        print(resultado("\nCliente Removido:\n", self.matriz[linha]))
                        #escrever o tempo no historico do arquivo
                        with open(self.historico, "a", encoding="utf-8-sig") as historico:
                            historico.write(f"\n Cadastro removido: {self.matriz[linha]}\n Tempo para remocao: {tempo:.6f} segundos\n")
                        del(self.matriz[linha])
                        self.tamanho -= 1 #reduzo o tamanho da matriz em 1
                #caso escolha por id, faco o mesmo que anteriomente, mas jogo o id na funcao de encontrar_linhas
                elif metodo == 2:
                    cracha = int(input(solicitar("Por favor, digite o ID do cliente: ")))
                    inicio = time.time()
                    linha = self.encontrar_linha(2, cracha)
                    tempo = time.time() - inicio
                    if linha is not False:
                        print(resultado("\nCliente Removido:\n", self.matriz[linha]))
                        with open(self.historico, "a", encoding="utf-8-sig") as historico:
                            historico.write(f"\n Cadastro removido: {self.matriz[linha]}\n Tempo para remocao: {tempo:.6f} segundos\n")
                        del(self.matriz[linha])
                        self.tamanho -= 1
                break
            except IndexError as problema:
                print(f"{cores["erro"]}Erro, {problema}{cores["reset"]}")
            except ValueError:
                print(erro("Resposta inválda!"))
#=========================================================================================================#
    def atualizar_arquivo(self):
        inicio = time.time()
        with open(self.arquivo, "w", encoding="utf-8-sig", newline='') as arquivo:
        #escreve o cabecalho
            arquivo.write(";".join(self.cabecalho)+"\n")
            #escreve as linhas atuais
            for linha in range(self.tamanho):
                linha_atual = self.matriz[linha]
                linha_formatada_para_csv = ";".join(str(item) for item in linha_atual) + "\n"
                arquivo.write(linha_formatada_para_csv)
        tempo = time.time() - inicio
        with open(self.historico, "a", encoding="utf-8-sig") as historico:
            historico.write(f"\n === Arquivo '{self.arquivo}' atualizado! === \n Tempo de atualização: {tempo:.6f} segundos\n")

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
                #forco os inputs maiores que 6 para o except
                if pergunta >= 6:
                    raise ValueError
            #uso o except pra ficar voltando pro inicio (com o continue) toda vez que o input vier em formato indesejado
            except ValueError:
                print(erro("Erro, escolha entre [1] e [5]"))
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
                self.atualizar_arquivo()
                break
#=========================================================================================================#

gerar_arquivo("pequeno.csv", 100, "hist_pequeno.txt")
gerar_arquivo("medio.csv", 1000, "hist_medio.txt")
gerar_arquivo("grande.csv", 10000, "hist_grande.txt")
gerar_arquivo("gigante.csv", 100000, "hist_gigante.txt")

#menu para escolher qual matriz quer interagir
def menu_inicial():
    matrizpequena = Gerenciador_Matriz("pequeno.csv", "hist_pequeno.txt")
    matrizmedia = Gerenciador_Matriz("medio.csv", "hist_medio.txt")
    matrizgrande = Gerenciador_Matriz("grande.csv", "hist_grande.txt")
    matrizgigante = Gerenciador_Matriz("gigante.csv", "hist_gigante.txt")
    while True:
        try:
            print("\n===== Arquivos Gerados =====")
            print(linha_menu(1, "Matriz Pequena"))
            print(linha_menu(2, "Matriz Média"))
            print(linha_menu(3, "Matriz Grande"))
            print(linha_menu(4, "Matriz Gigante"))
            print(linha_menu(5, "Finalizar Programa"))
            pergunta = int(input(solicitar("Qual arquivo deseja alterar? ")))
            if pergunta == 1:
                matrizpequena.menu_interativo()
            elif pergunta == 2:
                matrizmedia.menu_interativo()
            elif pergunta == 3:
                matrizgrande.menu_interativo()
            elif pergunta == 4:
                matrizgigante.menu_interativo()
            elif pergunta == 5:
                break
                #salvar arquivo
            else:
                raise ValueError
        except ValueError:
            print(erro("Erro, escreva um valor entre 1 e 4"))
menu_inicial()