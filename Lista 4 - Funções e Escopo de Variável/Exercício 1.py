def calculadora(m, x):
    valor = 0
    ultimo = 0
    operação = m

    if operação == 'S':

        for c in range(x):
            num = int(input())
            valor = ultimo + num
            ultimo = valor
        print(valor)

    if operação == 'sub':
        for c in range(x):
            num = int(input())
            if c == 0:
                ultimo = num
            else:
                valor = ultimo - num
                ultimo = valor

        print(valor)
    if operação == 'D':
        for c in range(x):
            num = int(input())
            if c == 0:
                ultimo = num
            else:
                valor = ultimo / num
                ultimo = valor
        print(valor)

    if operação == 'M':
        for c in range(x):
            num = int(input())
            if c == 0:
                ultimo = num
            else:
                valor = ultimo * num
                ultimo = valor
        print(valor)




    return valor


v = False

while not v:

    m = input()
    x = int(input())

    calculadora(m, x)

    continuador = int(input())
    if continuador != 1:
        v = True
