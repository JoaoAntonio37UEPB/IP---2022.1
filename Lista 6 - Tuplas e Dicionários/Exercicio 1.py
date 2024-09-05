pokemon = dict()
trying = True

while trying:
    try:
        ler_input = input().split()

        if ler_input[0] == 'ADD':
            if ler_input[1] in pokemon:
                print('Pokémon já adicionado na Pokédex')
            else:
                print('Pokémon adicionado com sucesso')
                pokemon[f'{ler_input[1]}'] = input()


        elif ler_input[0] == 'DESC':
            if ler_input[1] not in pokemon:
               print('Ainda não há registro desse Pokémon')
            else:
                print(pokemon[ler_input[1]])

    except EOFError:
        trying = False
