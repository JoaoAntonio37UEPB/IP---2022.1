quant_mochilas = int(input())
nomes = input().split()
list_nomes = []
for c in range(len(nomes)):
    list_nomes.append(nomes[c])

mochila = []
tamnaho_mochila = []

for i in range(quant_mochilas):
    mochila.append(['Lanterna', 'Omega 3 da top therm'])

for c in range(quant_mochilas):
    tam = int(input())
    mochila[c].append(tam)
    tamnaho_mochila.append(tam)


itens_add = int(input())



for c in range(itens_add):

    ler_iten = input()
    idx_mochila = int(input())
    if mochila[idx_mochila][2] + 1 == len(mochila[idx_mochila]):
        print('Mochila cheia. Não vai dar para levar.')
    else:
        mochila[idx_mochila].append(ler_iten)

#remove os "tamnahos"

for i in range(len(mochila)):
    for j in range(1):
        mochila[i].remove(mochila[i][2])



while True:

    ler = input()
    #funcoes

    #tirar da mochila
    if ler == 'Tirar da mochila':
        item = input()
        escolha_mochila = int(input())
        if item in mochila[escolha_mochila]:
            print(f'{item} usado com sucesso da mochila {escolha_mochila}.')
            mochila[escolha_mochila].remove(item)
        else:
            print(f'Você não tem {item} na mochila {escolha_mochila}.')
    #coloca na mochila

    elif ler == 'Guardar na mochila':
        item = input()
        escolha_mochila = int(input())
        if tamnaho_mochila[escolha_mochila] == len(mochila[escolha_mochila]):
            print(f'Mochila {escolha_mochila} cheia!')
        else:
            print(f'{item} adicionado na mochila {escolha_mochila}.')
            mochila[escolha_mochila].append(item)


    elif ler == 'CHEGAMOS NO CIN!':
        break
    else:
      print('Ação inválida.')



#printa as saidas conforme os donas das mochilas
for i in range(0, quant_mochilas):
    print(f'Mochila de {list_nomes[i]} chegou assim:')
    for j in range(len(mochila[i])):
        print(mochila[i][j])

