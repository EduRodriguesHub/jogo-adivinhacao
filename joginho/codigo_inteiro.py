'''from random import choice
from time import sleep

vermelho = '\033[31m'
branco = '\033[0;30m'
amarelo = '\033[1;33m'
verde = '\033[1;32m'
roxo = '\033[1;35m'
azul_claro = '\033[1;36m'

titulo = print(f'{verde}Bem vindo ao jogo de adivinhações!\033[m')

subtitulo = print(f'{roxo}Bora testar a sorte?\033[m')

lista_de_dificuldade = print(('DIFICULDADE:\n'
    'FACIL: 1-50, DIGITE (1)\n'
    'MÉDIO: 1-100, DIGITE (2)\n'
    'DIFÍCIL: 1-150, DIGITE (3)\n'
    'MUITO DIFÍCIL: 1-200, DIGITE (4)\n'))


userd = int(input('Escolha: '))
listad = []
escolhas = [1, 2, 3, 4]
base = 0
while userd not in escolhas:
    errado = print(f'{vermelho}Não tem esse número na lista, escolha outro:\033[m')
    lista_de_dificuldade
    userd = int(input('Escolha: '))

if userd == 1:
    while len(listad) < 50:
        numero = base + 1
        listad.append(numero)
        base = base + 1
elif userd == 2:
    while len(listad) < 100:
        numero = base + 1
        listad.append(numero)
        base = base + 1
elif userd == 3:
    while len(listad) < 150:
        numero = base + 1
        listad.append(numero)
        base = base + 1
elif userd == 4:
    while len(listad) < 200:
        numero = base + 1
        listad.append(numero)
        base = base + 1

listad

contador = 0
numero_escolhido = choice(listad)
maquina_lista_escolha = []

while len(maquina_lista_escolha) < len(listad):  # Limita tentativas ao tamanho da lista
    maquina = choice(listad)
    if maquina not in maquina_lista_escolha:  # Adiciona apenas números únicos
        maquina_lista_escolha.append(maquina)

titulo
sleep(0.5)
subtitulo
sleep(0.5)
lista_de_dificuldade
contador = 1
numero_escolhido = choice(listad)

intervalo = len(listad)

while True:
    while True:
        try:
            user = int(input(f"Escolha um número de 1 a {intervalo}: "))
            if user not in listad:
                print(f"Número não encontrado na lista de 1 a {len(listad)}. Tente novamente.")
            else:
                break  # Sai do loop se o número estiver na lista
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
    # Checa se o jogador acertou
    if user == numero_escolhido:
        sleep(0.5)
        print(f"{azul_claro}Parabéns! Você acertou o número {amarelo}{numero_escolhido}\033[m {azul_claro}em {contador} tentativas!\033[m")
        break

    # Feedback para o jogador
    if user < numero_escolhido:
        sleep(0.5)
        print("Jogador chutou baixo!")
    else:
        sleep(0.5)
        print("Jogador chutou alto!")

    # Jogada do computador
    computador_tentativa = maquina_lista_escolha[contador - 1]
    sleep(0.5)
    print(f"{amarelo}COMPUTADOR\033[m: eu escolhi {computador_tentativa}")

    # Checa se o computador acertou
    if computador_tentativa == numero_escolhido:
        sleep(0.5)
        print(f"{azul_claro}O computador acertou o número {amarelo}{numero_escolhido}\033[m {azul_claro}em {contador} tentativas!\033[m")
        break

    # Feedback para o computador
    if computador_tentativa < numero_escolhido:
        sleep(0.5)
        print("Computador chutou baixo!")
    else:
        sleep(0.5)
        print("Computador chutou alto!")
    sleep(0.5)
    
    contador += 1
    ____________________________________________________________________
'''

from random import choice
from time import sleep

# Definições de cores
CORES = {
    'vermelho': '\033[31m',
    'branco': '\033[0;30m',
    'amarelo': '\033[1;33m',
    'verde': '\033[1;32m',
    'roxo': '\033[1;35m',
    'azul_claro': '\033[1;36m'
}

# Funções de exibição
def mostrar_titulo():
    print(f"{CORES['verde']}Bem-vindo ao jogo de adivinhações!\033[m")
    print(f"{CORES['roxo']}Bora testar a sorte?\033[m")

def mostrar_dificuldades():
    print((
        "DIFICULDADE:\n"
        "1 - FACIL: 1-50\n"
        "2 - MÉDIO: 1-100\n"
        "3 - DIFÍCIL: 1-150\n"
        "4 - MUITO DIFÍCIL: 1-200\n"
    ))

# Função para escolher a lista de números baseada na dificuldade
def definir_lista_dificuldade():
    escolhas = {1: 50, 2: 100, 3: 150, 4: 200}
    while True:
        try:
            dificuldade = int(input('Escolha a dificuldade (1 a 4): '))
            if dificuldade in escolhas:
                return list(range(1, escolhas[dificuldade] + 1))
            else:
                print(f"{CORES['vermelho']}Escolha inválida! Tente novamente.\033[m")
        except ValueError:
            print(f"{CORES['vermelho']}Entrada inválida! Por favor, digite um número.\033[m")

# Função principal do jogo
def jogo_adivinhacao():
    mostrar_titulo()
    mostrar_dificuldades()
    
    listad = definir_lista_dificuldade()
    numero_escolhido = choice(listad)
    maquina_lista_escolha = []
    intervalo = len(listad)
    contador = 1

    # Preenche as escolhas da máquina sem repetições
    while len(maquina_lista_escolha) < intervalo:
        tentativa_maquina = choice(listad)
        if tentativa_maquina not in maquina_lista_escolha:
            maquina_lista_escolha.append(tentativa_maquina)

    # Loop de adivinhação
    while True:
        # Entrada do jogador com validação
        while True:
            try:
                user = int(input(f"Escolha um número de 1 a {intervalo}: "))
                if user in listad:
                    break
                print(f"Número não encontrado na lista de 1 a {intervalo}. Tente novamente.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

        # Verifica o palpite do jogador
        if user == numero_escolhido:
            print(f"{CORES['azul_claro']}Parabéns! Você acertou o número {CORES['amarelo']}{numero_escolhido}\033[m "
                  f"{CORES['azul_claro']}em {contador} tentativas!\033[m")
            break
        elif user < numero_escolhido:
            print("Jogador chutou baixo!")
        else:
            print("Jogador chutou alto!")

        # Jogada da máquina
        tentativa_maquina = maquina_lista_escolha[contador - 1]
        print(f"{CORES['amarelo']}COMPUTADOR\033[m: eu escolhi {tentativa_maquina}")

        # Verifica o palpite da máquina
        if tentativa_maquina == numero_escolhido:
            print(f"{CORES['azul_claro']}O computador acertou o número {CORES['amarelo']}{numero_escolhido}\033[m "
                  f"{CORES['azul_claro']}em {contador} tentativas!\033[m")
            break
        elif tentativa_maquina < numero_escolhido:
            print("Computador chutou baixo!")
        else:
            print("Computador chutou alto!")

        contador += 1

# Executa o jogo
jogo_adivinhacao()
