def bubbleSort(dicinario):
    for j in range(len(dicinario) - 1, 0, -1):
        for i in range(j):
            if dicinario[i+1] > dicinario[i + 2]:
                aux = dicinario[i+1]
                dicinario[i+1] = dicinario[i + 2]
                dicinario[i + 2] = aux


gohan = dict()
picolo = dict()

tam = int(input())

ler_gohan = input().split()
ler_picolo = input().split()

for c in range(tam):
    gohan[c + 1] = int(ler_gohan[c])
    picolo[c + 1] = int(ler_picolo[c])

bubbleSort(gohan)
bubbleSort(picolo)


# checa as distancias

cont = 0
for c in range(tam):
    if gohan[c+1] == picolo[c+1]:
        cont += 1


if cont == tam:
    print('Dale Gohan!')
else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')
