grupo = dict()

grupo['Bobby'] = ['grande espada', 'armadura media']
grupo['Diana'] = ['dardo', 'armadura leve']
grupo['Eric'] = ['grande espada', 'armadura pesada']
grupo['Hank'] = ['espada', 'armadura media']
grupo['Presto'] = ['cajado', 'armadura leve']
grupo['Sheila'] = ['espada', 'armadura leve']
grupo['Uni'] = ['chifre', 'armadura leve']

pontos_vilao = 0

ler_vilao = input()
if ler_vilao == 'Vingador':
    pontos_vilao = 30
elif ler_vilao == 'Tiamat':
    pontos_vilao = 20
elif ler_vilao == 'Vingador das Sombras':
    pontos_vilao = 14
else:
    pontos_vilao = 9


num_turnos = int(input())


while num_turnos > 0:
    
  
    try:
      ler_heroi = input()
    except EOFError:
      break
    
    
    if ler_heroi == 'Mestre dos Magos':
        print(f'Muito obrigado amigo, que nos vejamos novamente um dia')
        exit()

    # armas
    if grupo[ler_heroi][0] == 'espada':
        pontos_vilao -= 6
    elif grupo[ler_heroi][0] == 'grande espada':
        pontos_vilao -= 8
    elif grupo[ler_heroi][0] == 'dardo':
        pontos_vilao -= 12
    elif grupo[ler_heroi][0] == 'chifre':
        pontos_vilao -= 2
    elif grupo[ler_heroi][0] == 'cajado':
        pontos_vilao -= 4

    #armadura

    if grupo[ler_heroi][1] == 'armadura leve':
        num_turnos -= 3

    elif grupo[ler_heroi][1] == 'armadura media':
        num_turnos -= 2
    
    else:
      num_turnos -= 1
    
    #printa as saidas

    if pontos_vilao <= 0:
        print(f'{ler_heroi} executou o ultimo golpe em {ler_vilao}, estamos livres!')
        exit()

    if num_turnos < 0:
      break
print(f'Oh nao, {ler_vilao} e muito forte, este e o fim!')        



   
