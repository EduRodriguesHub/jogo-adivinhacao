#- cria uma lista com 100 números
#- maquina escolher um número de 1 a 100
#- guardar o número em uma variável
#- pedir que o usuário digite um número
#- se o número estiver muito alto, diga para chutar mais baixo
#- se o número estiver muito baixo, diga para chutar mais alto
#- se estiver correto, parabenize


from random import choice

lista = []
base = 0
while len(lista) < 100:
    numero = base + 1
    lista.append(numero)
    base = base + 1

escolha = choice(lista)

user = int(input("Escolha um número de 1 a 100: "))

while user < escolha:
    print('Muito baixo, tente chutar mais alto!')
    user = int(input("Escolha um número de 1 a 100: "))
    if user == escolha:
        print(f'Muito bem, Você acertou, Eu tinha escolhido o número {escolha}')
while user > escolha:
    print('Muito alto, tente chutar mais baixo!')
    user = int(input("Escolha um número de 1 a 100: "))
    if user == escolha:
        print(f'Muito bem, Você acertou, Eu tinha escolhido o número {escolha}')

