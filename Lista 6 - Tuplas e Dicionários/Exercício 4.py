import operator

tupla_atk = ('Carta com maior poder de ataque:')
tupla_def = ('Carta com maior poder de defesa:')

cartas_atk = dict()
cartas_deff = dict()

nome_cartas = []
atk = []
deff = []

n = int(input())

for i in range(n):
    nome = ''
    ler = input().split()
    atk.append(int(ler[-2]))
    deff.append(int(ler[-1]))
    for c in range(len(ler) - 2):
        nome += ler[c] + ' '
    nome_cartas.append(nome[:-1])

# add os itens

for c in range(n):
    cartas_atk[f'{nome_cartas[c]}'] = atk[c]
    cartas_deff[f'{nome_cartas[c]}'] = deff[c]

maior_atk = max(cartas_atk.items(), key=operator.itemgetter(1))[0]
maior_deff = max(cartas_deff.items(), key=operator.itemgetter(1))[0]

print(tupla_atk, f'{maior_atk}')

print(f'Ataque: {cartas_atk[maior_atk]}\n')

print(tupla_def, f'{maior_deff}')

print(f'Defesa: {cartas_deff[maior_deff]}')
