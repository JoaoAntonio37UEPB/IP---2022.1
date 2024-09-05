talisma = {}
requesitos = {}

talisma['Carneiro'] = 'Adormecer'
talisma['Cao'] = 'Imortalidade'
talisma['Cobra'] = 'Invisibilidade'
talisma['Coelho'] = 'Alta velocidade'
talisma['Tigre'] = 'Equilibrio espiritual'
talisma['Dragao'] = 'Fogo'
talisma['Cavalo'] = 'Cura'
talisma['Macaco'] = 'Metamorfose animal'
talisma['Galo'] = 'Levitacao'
talisma['Porco'] = 'Raio laser'
talisma['Rato'] = 'Animar objetos'
talisma['Touro'] = 'Forca descomunal'

requesitos['Carneiro'] = 'Imortalidade'
requesitos['Cao'] = 'Forca descomunal'
requesitos['Cobra'] = 'Equilibrio espiritual'
requesitos['Coelho'] = 'Metamorfose animal'
requesitos['Tigre'] = 'Adormecer'
requesitos['Dragao'] = 'Cura'
requesitos['Cavalo'] = 'Levitacao'
requesitos['Macaco'] = 'Raio laser'
requesitos['Galo'] = 'Animar objetos'
requesitos['Porco'] = 'Fogo'
requesitos['Rato'] = 'Alta velocidade'
requesitos['Touro'] = 'Invisibilidade'

meus_talisma = []
chefe_talisma = []

n = int(input())

for c in range(n):
    ler_talisma = input()
    meus_talisma.append(talisma[ler_talisma])

n_inimigo = int(input())

for c in range(n_inimigo):
    ler_talisma = input()
    chefe_talisma.append(requesitos[ler_talisma])

# batalha

novos_talisma = []
cont = 0

for c in range(len(chefe_talisma)):
    if chefe_talisma[c] in meus_talisma:
        cont += 1
        for chave, valor in requesitos.items():
            if valor == chefe_talisma[c]:
                meus_talisma.append(talisma[chave])
                print(f'Boa! O talisma do {chave} vai ser nosso!')
    else:
        for chave, valor in talisma.items():
            if valor == chefe_talisma[c]:

                print(f'Nao vai dar, melhor ir atras do talisma do {chave} antes.')


if cont >= n_inimigo:
    print('Esse plano funciona, vamos agora!')
else:
    print('Que mau dia!! Melhor pensarmos num plano de fuga.')
