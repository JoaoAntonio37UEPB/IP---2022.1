suspeitos = []
n_comando = 0

ler_suspeitos = input().split(',')

for c in range(len(ler_suspeitos)):
    suspeitos.append(ler_suspeitos[c])

while len(suspeitos) > 1:

    
    palpite = input()

    if palpite == 'Não encontrei nada no primeiro suspeito':
        suspeitos.remove(suspeitos[0])


    elif palpite == 'O último da lista está limpo':
        suspeitos.remove(suspeitos[len(suspeitos) - 1])



    elif palpite == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita':

        if len(suspeitos) % 2 == 0:
            suspeitos.remove(suspeitos[((len(suspeitos)-1)//2)+1])
        
        else:
            suspeitos.remove(suspeitos[int((len(suspeitos)-1)/2)])


    elif palpite == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:':

        remov = int(input())
        suspeitos.remove(suspeitos[remov])


    elif palpite == 'Acho que temos mais uma opção a ser analisada…':

        novo_suspeito = input()
        suspeitos.append(novo_suspeito)


    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')


print(f'Acho que encontramos o suspeito. O seu nome é {suspeitos[0]}, vamos salvar o Sam!')
