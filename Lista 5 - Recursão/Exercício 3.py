def checa_char(ler):
    if len(ler) == 0:
        return ''
    else:

        if ler[-1].isupper():
            return "U" + checa_char(ler[:-1])
        elif ler[-1].islower():
            return "L" + checa_char(ler[:-1])


def fatorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fatorial(num - 1)



maiusculas = ''
minusculas = ''

# definindo o k

k = 0

min = mai = 0


ler_input = input()
aux = checa_char(ler_input)

for c in range(len(aux)):
    if aux[c] == 'U':
        mai += 1
        maiusculas += aux[c]
    elif aux[c] == 'L':
        min += 1
        minusculas += aux[c]

# determina o valor de k conforme a analise das minusculas e maiusculas
if min > mai:
    k = min
elif min < mai:
    k = mai
elif min == mai:
    k = min

#calculo da combinação
NUM = fatorial(len(ler_input))/(fatorial(k)*fatorial((len(ler_input)-k)))

#acha a -enezima letra
r = NUM % k

#printa as saidas
if ler_input[int(r)].isupper():
    print(f'Morty!!! Morty!!! Vamos para a dimensão {ler_input[int(r)]}-{int(NUM)}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {ler_input[int(r)]}-{int(NUM)} para sempre, Morty!!! Wubba lubba dub dub!!!')
else:
    print(f'Oh geez, Rick!!! Eu não sei se ir pra dimensão {ler_input[int(r)]}-{int(NUM)} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!')
