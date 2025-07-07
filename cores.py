#criei essa "biblioteca" pra poder pintar o terminal de uma forma mais facil e "clean"

#dicionario com cores e formatos separados
cores = {
    "preto": "\033[1;30m",
    "vermelho": "\033[31m",
    "verde": "\033[1;32m",
    "amarelo": "\033[1;33m",
    "azul": "\033[34m",
    "magenta": "\033[35m",
    "ciano": "\033[36m",
    "branco": "\033[37m",
    
    "cinza": "\033[90m",
    "vermelho_claro": "\033[91m",
    "verde_claro": "\033[92m",
    "amarelo_claro": "\033[93m",
    "azul_claro": "\033[94m",
    "magenta_claro": "\033[95m",
    "ciano_claro": "\033[96m",
    
    "reset": "\033[0m",         # Volta ao padrão
    "negrito": "\033[1m",
    "sublinhado": "\033[4m",    # Padrão sublinhado
    "inverso": "\033[7m",       # Inverte cor do texto e fundo
    "normal": "\033[22m",       # Remove negrito/sublinhado
    
    "aviso": "\033[93;41m",     # Amarelo claro com fundo vermelho
    "destaque": "\033[96;44m",  # Ciano claro com fundo azul
    "erro": "\033[97;101m",      # Branco co
}

#funcoes pra cada tipo de interacao com o terminal que seja recorrente (menus de escolhas, perguntas de input, resultados e erros)

#coloca o numero da opcao com cor amarela e entre colchetes, o texto da opcao em preto e no final reseta
def linha_menu(opcao, texto):
    return f"{cores["amarelo"]}[{opcao}]{cores["reset"]} = {cores["preto"]}{texto}{cores["reset"]}"
#na hora do input, pinta o texto de amarelo_claro e reseta no final
def solicitar(texto):
    return f"{cores["amarelo_claro"]}{texto}{cores["reset"]}"
#na hora de printar um resultado qualquer, pinta o texto anterior ao resultado de verde_claro e reseta pra printar o resultado na cor padrao
def resultado(texto, resultado):
    return f"{cores["verde_claro"]}{texto}{cores["reset"]}{resultado}"
#na hora de mostrar um erro, pinta o fundo de vermelho e o texto de preto
def erro(texto):
    return f"{cores["erro"]}{texto} {cores["reset"]}"
