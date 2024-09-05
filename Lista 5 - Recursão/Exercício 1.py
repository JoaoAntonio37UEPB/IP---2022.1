def somanum(num):
    if len(num) == 1:
        return num[0]
    else:
        return num[0] + somanum(num[1:])


def MDC(a, b):
    resto = a % b
    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b


def mdc_3num(num):
    for c in range(1, len(num)):
        num[c] = MDC(num[c - 1], num[c])
    return num[c]


# numero 1
vetor1 = []
num1 = input()
for c in range(len(num1)):
    vetor1.append(int(num1[c]))

aux1 = somanum(vetor1)

# numero 2
vetor2 = []
num2 = input()
for c in range(len(num2)):
    vetor2.append(int(num2[c]))

aux2 = somanum(vetor2)

# numero 3
vetor3 = []
num3 = input()
for c in range(len(num3)):
    vetor3.append(int(num3[c]))

aux3 = somanum(vetor3)

vetor_num = [aux1, aux2, aux3]

print(f'O MDC obtido é: {mdc_3num(vetor_num)}')
