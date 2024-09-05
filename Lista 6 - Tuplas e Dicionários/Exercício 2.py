jogadores = {}
lista_jog = []


ler_pos = input()
aux = ler_pos[1:-1].split(',')


for c in range(len(aux)):
    jogadores[c] = int(aux[c])



targ = int(input())


#Acha os dois jogadores
v = False
jogador1= 0
jogador2 = 0


for i in range(len(jogadores)):

    if v == True:
        break
    jogador1 = i

    for j in range(len(jogadores)):

        if jogadores[i] == jogadores[j]:
            continue

        elif jogadores[i] + jogadores[j] == targ:
            jogador2 = j
            v = True
            break


print(f'[{jogador1}, {jogador2}]')
