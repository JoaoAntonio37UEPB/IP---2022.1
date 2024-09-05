jogos = []

jogos_alterados = []

fantasma = []
#contadores da lsita sem alteração

cont_jogos = 0

#contadores da lista alterada
cont1 = cont2 = cont3 = 0
cont_total = 0


#recebe os dados para as listas
ler_jogos = input().split(' ')
for c in range(len(ler_jogos)):
    jogos.append(ler_jogos[c])
    jogos_alterados.append(ler_jogos[c])


ler_fantasma = input().split(' ')
for c in range(len(ler_fantasma)):
    fantasma.append(ler_fantasma[c])



#muda a lista confrome o fantasma

for i in range(12):
    if jogos[i] == 'V' and fantasma[i] == '1':

        print('O maldito sapo interferiu no resultado! O que parecia uma vitória garantida terminou em um empate.')

        jogos_alterados[i] = 'E'

    elif jogos[i] == 'E' and fantasma[i] == '1':

        print('O anfíbio da maldição interferiu no resultado! Um empate tranquilo virou uma frustrante derrota.')
        jogos_alterados[i] = 'D'

    elif jogos[i] == 'D' and fantasma[i] == '1':
        print('O que já era ruim, se tornou uma humilhante derrota. Desgraçado desse sapo!')



#checa o desempenho das equipes a cada terço

#primeiro terço
for c in range(4):

    if jogos_alterados[c] == 'V':
        cont1 += 3

    elif jogos_alterados[c] == 'E':
        cont1 += 1

    elif jogos_alterados[c] == 'D':
        cont1 += 0
if cont1 == 7:
    print(f'A pontuação na 1ª fatia de 4 jogos está dentro do planejado.')
elif cont1 > 7:
    print(f'A pontuação na 1ª fatia de 4 jogos está com uma gordurinha de {cont1-7} pontos.')
elif cont1 < 7:
    print(f'A pontuação na 1ª fatia de 4 jogos está abaixo da planejada em {7-cont1} pontos.')

#segundo terço

for c in range(4):

    if jogos_alterados[c+4] == 'V':
        cont2 += 3

    elif jogos_alterados[c+4] == 'E':
        cont2 += 1

    elif jogos_alterados[c+4] == 'D':
        cont2 += 0

if cont2 == 7:
    print(f'A pontuação na 2ª fatia de 4 jogos está dentro do planejado.')
elif cont2 > 7:
    print(f'A pontuação na 2ª fatia de 4 jogos está com uma gordurinha de {cont2-7} pontos.')
elif cont2 < 7:
    print(f'A pontuação na 2ª fatia de 4 jogos está abaixo da planejada em {7-cont2} pontos.')
#terceiro terço

for c in range(4):

    if jogos_alterados[c+8] == 'V':
        cont3 += 3

    elif jogos_alterados[c+8] == 'E':
        cont3 += 1

    elif jogos_alterados[c+8] == 'D':
        cont3 += 0
if cont3 == 7:
    print(f'A pontuação na 3ª fatia de 4 jogos está dentro do planejado.')
elif cont3 > 7:
    print(f'A pontuação na 3ª fatia de 4 jogos está com uma gordurinha de {cont3-7} pontos.')
elif cont3 < 7:
    print(f'A pontuação na 3ª fatia de 4 jogos está abaixo da planejada em {7-cont3} pontos.')

cont_total = cont1 + cont2 + cont3
#contagem dos pontos da lista sem alteração

for c in range(len(jogos)):
    if jogos[c] == 'V':
        cont_jogos += 3
    elif jogos[c] == 'E':
        cont_jogos += 1
    elif jogos[c] == 'D':
        cont_jogos += 0

#teste para saber se ouve perca de pontos, ou n
if abs(cont_total - cont_jogos) > 0:
    print(f'A maldição do sapo fez o Vascão perder {abs(cont_total - cont_jogos)} pontos. Um número preocupante, que pode fazer diferença.')
else:
    print('A maldição parece que não teve impacto relevante! Não houve nenhuma perda de pontos.')

#print final com total de pontos

if cont_total >= 21:
    print(f'Na reta final do campeonato, o Vasco garantiu um total de {cont_total} pontos, com {jogos_alterados.count("V")} vitórias, {jogos_alterados.count("E")} empates e {jogos_alterados.count("D")} derrotas, e alcançou o tão esperado acesso. O Clube do Fomento Corporal vibra num SJ lotado!')

else:
    print(f'Na reta final do campeonato, o Vasco fez somente {cont_total} pontos, com {jogos_alterados.count("V")} vitórias, {jogos_alterados.count("E")} empates e {jogos_alterados.count("D")} derrotas, e não conseguiu o acesso. Mais um ano de série B e sofrimento. Mob, o clube e a torcida estão completamente desolados.')
