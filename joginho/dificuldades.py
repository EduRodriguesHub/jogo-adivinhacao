from tela_inicio import lista_de_dificuldade
from cores import vermelho
from random import choice

# verifica se o número está no nível de dificuldade ou não se encaixa, ex: (str)
def verify(escolhas):
        while True:
            try:
                user = int(input('Escolha: '))
                while user not in escolhas:
                        print(f'{vermelho}Não tem esse número na lista, escolha outro:\033[m')
                        user = int(input('Escolha: '))
                return user
            except:
                print(f'{vermelho}Um número entre 1 e 4 por gentileza!\033[m')
        
        
def dificuldade(usuario, lista):
    while True:
        try:
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
        except:
            print('Um número por gentileza!')

def escolher_Numero(numero):
    choic = choice(numero)
    return choic

def escolha(opc):
    opc = int(input(f"Escolha um número de 1 a {intervalo}: "))
    return opc

opcoes = [1, 2, 3, 4]
listad = []
user = verify(opcoes)
dificuldade(user, listad)
numero_escolhido = escolher_Numero(listad)
intervalo = len(listad)

