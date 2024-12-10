from tela_inicio import titulo, subtitulo, lista_de_dificuldade
from cores import azul_claro, amarelo
from dificuldades import listad, numero_escolhido, escolha
from versus_maquina import maquina_lista_escolha
from time import sleep
titulo
sleep(0.5)
subtitulo
sleep(0.5)
lista_de_dificuldade
contador = 1

intervalo = len(listad)
tentativa = escolha('')

while True:
    # Checa se o jogador acertou
    if tentativa == numero_escolhido:
        sleep(0.5)
        print(f"{azul_claro}Parabéns! Você acertou o número {amarelo}{numero_escolhido}\033[m {azul_claro}em {contador} tentativas!\033[m")
        break

    # Feedback para o jogador
    if tentativa < numero_escolhido:
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

    tentativa = escolha(tentativa)
    contador += 1