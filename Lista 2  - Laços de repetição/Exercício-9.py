palpites = 0

aux1 = 0
aux2 = 0
aux3 = 0
conversao = 0

num = int(input())

for c in range(0, num):

    op = input()
    if op == 'DEC':

        n1 = input()
        aux3 = int(n1)
        n1 = aux3
        x = n1

        # conversao para decimal
        n = len(str(n1))
        valor_digitado = n1
        decimal1 = 0
        i = 0

        while n >= 0:
            resto = n1 % 10
            decimal1 += (resto * (2 ** i))
            n -= 1
            i += 1
            n1 //= 10

        n2 = int(input())

        if decimal1 == n2:
            palpites += 1

        elif decimal1 != n2:
            print(f"Palpite Incorreto, o valor {x} = {decimal1}")




    elif op == 'BIN':

        n1 = input()
        aux1 = int(n1)
        n1 = aux1
        x = n1

        if n1 == 0:

            conversao = 0

        else:
            # conversao para binario

            binario = ''

            while n1 > 0:
                binario += str(n1 % 2)
                n1 //= 2

            conversao = int(binario[::-1])


        n2 = input()
        aux2 = int(n2)
        n2 = aux2



        if n2 == conversao:

            palpites += 1

        else:
            print(f"Palpite Incorreto, o valor {x} = {conversao}")

if palpites > (num / 2):
    print("Bazinga! Quem realizou esses cálculos foi o computador??")

elif palpites <= (num / 2):
    print("Parece que realizar conversões em binário não é o seu forte")

