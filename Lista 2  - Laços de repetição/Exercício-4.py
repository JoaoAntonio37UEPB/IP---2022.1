

n = int(input())

nomeplanet = ""
menor = 0
melhor = 0

while n<2:
    print("Número inválido, tente novamente")
    n = int(input())

for c in range(0,n):

    planeta = input()
    raio = float(input())
    massa = float(input())
    temp = int(input())

    habt = (raio + massa + (temp/288))/3
    x = abs(habt - 1)

    if c == 0:

        menor = x
        melhor = habt
        nomeplanet = planeta

    else:
        if x < menor:

            menor = x
            melhor = habt
            nomeplanet = planeta



if melhor == 1:
    print(f"{nomeplanet} é perfeito!")

elif melhor < 1:
    print(f"{nomeplanet} vai dar pro gasto")

elif melhor > 1:
    print(f"{nomeplanet} vai ter que servir")
    
    
