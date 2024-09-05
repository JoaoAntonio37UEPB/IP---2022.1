sintomas = [' dor de cabeca', ' insonia', ' pesadelos', ' suor frio', ' visoes']
pessoas = []
na_mira = []

cont_max = 0
cont_outros = 0

while True:

    ler_nomes = input()

    if ler_nomes == 'descobrir':
        break

    pessoas.append(ler_nomes.split(','))



#checa os sintomas
for i in range(len(pessoas)):
    cont_outros = 0
    for j in range(len(pessoas[i])- 1):

        if pessoas[i][0] == 'Max':
            if pessoas[i][j+1] in sintomas:
                #caso sejam sintomas repetidos
                if pessoas[i].count(pessoas[i][j+1]) > 1:
                    cont_max += 0
                else:
                    cont_max += 1

        elif pessoas[i][j+1] in sintomas:
            #caso sejam sintomas repetidos
            if pessoas[i].count(pessoas[i][j+1]) > 1:
                cont_outros += 0
            else:
                cont_outros += 1


        # checa se outras pessoas estao na mira
        if cont_outros == 5:
            na_mira.append(pessoas[i][0])
            break


#caso ninguem tenha os sintomas
if len(na_mira) == 0 and cont_max < 5:
    print('Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.')
    exit()

# caso max esteja com os 5 sintomas
if cont_max == 5:
    print("Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga.")
    # caso max n seja a unica com os 5 sintomas
    if len(na_mira)>= 1:
        print(f'Além dela, tem mais {len(na_mira)} pessoa(s) na mira do Vecna!')

# caso max n esteja na lista ou n tenha todos os sintomas
if cont_max < 5:
    print(f'Tem {len(na_mira)} pessoa(s) na mira do Vecna!')

# caso mais pessoas estejam em perigo
if len(na_mira) > 1:
    print('Precisamos avisar', end='')
    for c in range(len(na_mira)):
        print(f' {na_mira[c]}', end='')
        if c < len(na_mira) - 2:
            print(',', end='')

        if c == len(na_mira) - 2:
            print(f' e', end='')
    print(' para prepararem suas músicas favoritas.')

# caso so tenha um pessoa em perigo alem de max:
if len(na_mira) == 1:
    print(f'Precisamos avisar {na_mira[0]} para preparar sua música favorita.')
