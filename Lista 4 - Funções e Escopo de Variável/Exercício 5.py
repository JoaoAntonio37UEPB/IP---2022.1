def pag_pedras(a, b):
    media = (a + b) / 2

    return media


def pag_massagem(a):
    nova_gorjeta = 0
    if a % 2 == 0:
        nova_gorjeta += (a % 7) * 6
    else:
        nova_gorjeta += (a % 7) ** 2
    return nova_gorjeta

def servir(a):

    nova_gorjeta = 0

    if a % 10 == 0:
        nova_gorjeta += 5
    else:
        while a % 10 != 0:
            a += 1
            nova_gorjeta += 1

    return nova_gorjeta



serviços = ['pedras', 'pes', 'refeicao', 'completa']
gorjeta = 10
tempo = 0

while True:

    ler_serviço = input().split()

    if ler_serviço[0] not in serviços:
        print(f'O cliente fez voce perder tempo, voce ainda possui {int(gorjeta)} gorjetas.')
        tempo += 5
    # pedras

    elif ler_serviço[0] == serviços[0]:

        gorjeta += pag_pedras(tempo, gorjeta)
        tempo += 20

        print(f'Voce concluiu o servico de Pedras Quentes e agora possui {int(gorjeta)} gorjetas.')


    # massagem
    elif ler_serviço[0] == serviços[1]:

        gorjeta += pag_massagem(gorjeta)
        tempo += 30

        print(f'Voce concluiu o servico de Massagem nos Pes e agora possui {int(gorjeta)} gorjetas.')

    # servir
    elif ler_serviço[0] == serviços[2]:

        gorjeta += servir(gorjeta)

        tempo += 15

        print(f'Voce concluiu o servico de Servir Refeicao e agora possui {int(gorjeta)} gorjetas.')

    # messagem
    elif ler_serviço[0] == serviços[3]:

        soma_gorjeta = str(gorjeta)
        gorjeta += int(soma_gorjeta[0]) + int(soma_gorjeta[1])

        tempo += 50

        print(f'Voce concluiu o servico de Massagem Completa e agora possui {int(gorjeta)} gorjetas.')

    if tempo >= 120 or gorjeta == 50:
        break

# printa as saidas
if gorjeta >= 50:
    print(f'Você acumulou {int(gorjeta)} gorjetas, com essa quantidade voce conseguira comprar sua passagem de saida e '
          f'salvar seus pais.')
else:
    print('Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar seus pais.')
