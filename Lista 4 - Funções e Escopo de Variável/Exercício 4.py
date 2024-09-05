letras = []


# LETRAS MINUSCULAS
# lista de a-z minusculas
for i in range(ord('a'), ord('z') + 1):
    letras.append(chr(i))
# nova adição das letras minusculas
for i in range(ord('a'), ord('x') + 1):
    letras.append(chr(i))

# LETRAS MAIUSCULAS
# lista de A-Z maiusculas
for i in range(ord('A'), ord('Z') + 1):
    letras.append(chr(i))

# nova adiççao de letras maiusculas
for i in range(ord('A'), ord('X') + 1):
    letras.append(chr(i))

# adição dos dois espaços na ultima posião do vetor
letras.append(' ')


def tradutor(msg, cont):
    print(letras[int(msg[cont])],end='')


ler = input().split()

#checa se existe algum numero fora do range
for c in range(len(ler)):
    if int(ler[c]) > len(letras):
        print('Infelizmente os números nao dizem nada')
        exit()

#printa as saidas

for c in range(len(ler)):
    tradutor(ler, c)
