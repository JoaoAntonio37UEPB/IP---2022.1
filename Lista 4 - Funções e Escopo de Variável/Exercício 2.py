insetos = ['crcrcrcrcr', 'uuuuuuuoooooo', 'ooooooeeeeeeee']
nave = ['ppprrrrrooon', 'tutututututututu', 'eeeeeeeeoooooo']


def identificador(a, b):

    if a >= 1 and b == 0:
        print('É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…')

    elif b >= 1 and a == 0:
        print('São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??')

    elif a >= 1 and b >= 1:
        print('A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!')


while True:

    cont_insetos = 0
    cont_naves = 0

    ler_msg = input().split()


    for c in range(len(ler_msg)):

        if ler_msg[c] in insetos:
            cont_insetos += 1

        elif ler_msg[c] in nave:
            cont_naves += 1

        elif ler_msg[c] in nave and ler_msg[c] in insetos:
            cont_insetos += 1
            cont_naves += 1

    #checa se a frase n é de nenhum lado

    if cont_insetos == 0 and cont_naves == 0:
        print('Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.')
        break

    identificador(cont_insetos, cont_naves)

