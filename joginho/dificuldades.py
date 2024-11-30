from tela_inicio import lista_de_dificuldade
from cores import vermelho
from random import choice

# verifica se o número está no nível de dificuldade ou não se encaixa, ex: (str)
def verify(escolhas):
        user = int(input('Escolha: '))
        if user not in escolhas:
            while True:
                print(f'{vermelho}Não tem esse número na lista, escolha outro:\033[m')
                user = int(input('Escolha: '))
                if user in escolhas:
                    return user
        elif user in escolhas:
            return user
        
        
def dificuldade(usuario, lista):
    base = 0
    if usuario == 1:
        while len(lista) < 50:
            base = base + 1
            lista.append(base)
        return lista
    elif usuario == 2:
        while len(lista) < 100:
            base += 1
            lista.append(base)
        return lista
    elif usuario == 3:
        while len(lista) < 150:
            base += 1
            lista.append(base)
        return lista
    elif usuario == 4:
        while len(lista) < 200:
            base += 1
            lista.append(base)
        return lista

def escolher_Numero(numero):
    choic = choice(numero)
    return choic

opcoes = [1, 2, 3, 4]
listad = []
user = verify(opcoes)
dificuldade(user, listad)
numero_escolhido = escolher_Numero(listad)
