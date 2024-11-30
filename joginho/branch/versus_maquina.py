#criar uma maquina que jogue com o jogador revezando entre eles, quem acertar primeiro ganha.

#importar a listad
#robô escolher um número de acordo com a dificuldade do jogo
#fazer jogador e maquina revezarem 
#verificar se o jogador e a máquina acertaram

from dificuldades import listad
from random import choice

contador = 0

maquina_lista_escolha = []

while len(maquina_lista_escolha) < len(listad):  # Limita tentativas ao tamanho da lista
    maquina = choice(listad)
    if maquina not in maquina_lista_escolha:  # Adiciona apenas números únicos
        maquina_lista_escolha.append(maquina)


