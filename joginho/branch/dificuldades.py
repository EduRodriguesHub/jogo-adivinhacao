from tela_inicio import lista_de_dificuldade
userd = int(input('Escolha: '))
listad = []
escolhas = [1, 2, 3, 4]
base = 0
while userd not in escolhas:
    errado = print('Não tem esse número na lista, escolha outro:')
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