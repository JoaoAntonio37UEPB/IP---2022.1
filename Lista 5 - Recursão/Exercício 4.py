def fatorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


def fibonacci(num):
    if num > 1:
        return fibonacci(num - 1) + fibonacci(num - 2)

    return num


letras = []
senhas = []

for i in range(ord('a'), ord('z') + 1):
    letras.append(chr(i))

senha_original = input()

n = int(input())

for c in range(n):

    nova_senha = ''

    ler_senha = input()
    for i in range(len(ler_senha)):

        mod = letras.index(ler_senha[i]) % 11
        if mod == 0:
            nova_senha += '1'

        elif mod % 2 == 0:
             for j in range(mod):
                op = (fibonacci(j) + fatorial(j)) % 26
                nova_senha += letras[op]
        else:
            for j in range(mod):
                op = (fibonacci(j) * fatorial(j)) % 26
                nova_senha += letras[op]

    senhas.append(nova_senha)

if senha_original in senhas:
  print('Achamos! Achamos a senha.')
  
else:
  print('É... Temos que procurar mais.')
