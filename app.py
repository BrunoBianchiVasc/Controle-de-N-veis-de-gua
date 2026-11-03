import random
from colorama import Fore, Style

situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
]


def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE


def exibir_situacao(nivel):
    cor = definir_cor(nivel)
    mensagem = situacoes[nivel - 1]  # nível 1 = índice 0
    print(cor + f"Nível {nivel}: {mensagem}")


print("=== Monitoramento do Reservatório ===\n")

# Exibe todos os níveis, do mais baixo ao máximo
for nivel in range(1, 6):
    exibir_situacao(nivel)

# Simula a leitura de um sensor
nivel_atual = random.randint(1, 5)
print(Style.RESET_ALL + "\nLeitura atual do sensor:")
exibir_situacao(nivel_atual)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)