#- cria uma lista com 100 números
#- maquina escolher um número de 1 a 100
#- guardar o número em uma variável
#- pedir que o usuário digite um número
#- se o número estiver muito alto, diga para chutar mais baixo
#- se o número estiver muito baixo, diga para chutar mais alto
#- se estiver correto, parabenize


from random import choice
from maquina import lista
from tela_inicio import titulo, subtitulo
from cores import azul_claro

print(titulo)
print(subtitulo)

escolha = choice(lista)


user = int(input("Escolha um número de 1 a 100: "))

while user != escolha:
    if user < escolha:
        print('Muito baixo, tente chutar mais alto!')
        user = int(input("Escolha um número de 1 a 100: "))
    else:
        print('Muito alto, tente chutar mais baixo!')
        user = int(input("Escolha um número de 1 a 100: "))

print(f'{azul_claro}Muito bem, Você acertou, Eu tinha escolhido o número {escolha}\033[m')
