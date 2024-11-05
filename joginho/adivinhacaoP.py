#- cria uma lista com 100 números
#- maquina escolher um número de 1 a 100
#- guardar o número em uma variável
#- pedir que o usuário digite um número
#- se o número estiver muito alto, diga para chutar mais baixo
#- se o número estiver muito baixo, diga para chutar mais alto
#- se estiver correto, parabenize

from random import choice
from tela_inicio import titulo, subtitulo, lista_de_dificuldade
from cores import azul_claro, amarelo
from dificuldades import listad
from branch.versus_maquina import maquina_lista_escolha
from time import sleep
titulo
sleep(0.5)
subtitulo
sleep(0.5)
lista_de_dificuldade
contador = 1
numero_escolhido = choice(listad)

intervalo = len(listad)
user = int(input(f"Escolha um número de 1 a {intervalo}: "))

while True:
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
    user = int(input(f"Escolha um número de 1 a {intervalo}: "))
    contador += 1