quimicos = []
unico_frasco = ''
controle = 0
soma = 0
i = 0
v = True
somatorio = int(input())
n = int(input())

for c in range(n):
    ler = input().split(' ')
    quimicos.append(ler)

while v:

    if i <= len(quimicos) - 1:
        soma += int(quimicos[i][1])
        if somatorio == int(quimicos[i][1]):
            unico_frasco = quimicos[i]
            v = False

    else:
        v = False

    if soma == somatorio:

        if i < len(quimicos) - 1:
            quimicos.pop()

        v = False

    i += 1

    if soma > somatorio:
        quimicos.pop(0)
        i = 0
        soma = 0
        controle += 1

        if controle == (len(quimicos) - 1):
            v = False

if soma == somatorio:
    print('Vencemos a batalha e a humanidade foi restaurada!', end='')
    for c in range(len(quimicos)):
        print(f' {quimicos[c][0]}', end='')
    print(' foram usados para deszumbificar')
elif len(unico_frasco) > 0:
    print(f'Vencemos a batalha e a humanidade foi restaurada! {unico_frasco[0]} foram usados para deszumbificar')

else:
    print('Estou sentido algo estranho... será que também vou virar zumbi?')
