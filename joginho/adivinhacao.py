#- cria uma lista com 100 números
#- maquina escolher um número de 1 a 100
#- guardar o número em uma variável
#- pedir que o usuário digite um número
#- se o número estiver muito alto, diga para chutar mais baixo
#- se o número estiver muito baixo, diga para chutar mais alto
#- se estiver correto, parabenize

from random import choice
from tela_inicio import titulo, subtitulo, lista_de_dificuldade
from cores import azul_claro
from branch.dificuldades import listad
titulo
subtitulo
lista_de_dificuldade
contador = 1
escolha = choice(listad)
if len(listad) == 50:
    user = int(input("Escolha um número de 1 a 50: "))
elif len(listad) == 100:
    user = int(input('Escolha um número de 1 a 100: '))
elif len(listad) == 150:
    user = int(input('Escolha um número de 1 a 150: '))
elif len(listad) == 200:
    user = int(input('Escolha um número de 1 a 200: '))

while user != escolha:
    if user < escolha:
        print('Muito baixo, tente chutar mais alto!')
        user = int(input("Escolha um número de 1 a 100: "))
    else:
        print('Muito alto, tente chutar mais baixo!')
        user = int(input("Escolha um número de 1 a 100: "))
    contador = contador + 1

print(f'{azul_claro}Muito bem, Você acertou em {contador} tentativas, Eu tinha escolhido o número {escolha}\033[m')
