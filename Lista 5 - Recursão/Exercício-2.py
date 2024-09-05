def checa_parenteses(ler):

    if len(ler) == 0:
        return 'm'
    else:

        if ler[-1] == '(':
            return "E" + checa_parenteses(ler[:-1])
        elif ler[-1] == ')':
            return "D" + checa_parenteses(ler[:-1])
        else:
            return "N" + checa_parenteses(ler[:-1])

num = int(input())

for c in range(num):
    #contadores
    cont_esq = 0
    cont_dir = 0

    ler_input = input()
    aux = checa_parenteses(ler_input)
    #checa os parenteses
    for i in range(len(aux)):
        if aux[i] == 'E':
            cont_esq += 1
        elif aux[i] == 'D':
            cont_dir += 1

    if cont_esq == cont_dir:
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif cont_esq > cont_dir:
        print('A quantidade de parênteses \'(\' ''está maior que a de'' \')\','' vamos descartá-la')
    elif cont_esq < cont_dir:
        print('A quantidade de parênteses \')\''' está maior que a de ''\'(\','' vamos descartá-la')
