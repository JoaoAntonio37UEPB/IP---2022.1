nome = input()

if nome == 'Bonna':
    print("Os filmes sugeridos por Bonna são:")
elif nome == 'João':
    print("Os filmes sugeridos por João são:")

tam = int(input())

nome = []

for filmes in range(tam):
    ler = input().split(' - ')
    ler.reverse()
    nome.append(ler)


#ordenação....

for i in range(len(nome)):

    for j in range(0, len(nome)- i-1):
        if nome[j] < nome[j+1]:
            aux = nome[j]
            nome[j] = nome[j+1]
            nome[j+1] = aux



#printa a saida
for c in range(len(nome)):
    print(f'{nome[c][1]} - {nome[c][0]}')
