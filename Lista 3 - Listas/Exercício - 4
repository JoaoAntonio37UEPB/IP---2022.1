palavras = []
palavras_repetidas = []
soma = 0


for c in range(10):
    ler = input()
    if ler in palavras:
        palavras_repetidas.append(ler)
    palavras.append(ler)



#checagem dos repetidos

for i in range(10):
    for j in range(len(palavras_repetidas)):
        if palavras_repetidas[j] in palavras:
            palavras.remove(palavras_repetidas[j])

print('As palavras sao:')
for c in range(len(palavras)):
    print(palavras[c])
    soma += len(palavras[c])

print(f'A soma do tamanho das palavras é: {soma}')
print('Estou impressionado, você me venceu, pode ir embora...')
