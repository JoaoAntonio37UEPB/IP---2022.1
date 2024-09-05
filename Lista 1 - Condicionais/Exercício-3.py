diaspar = [18,22,24,26]
diasimpar = [17,19,21,23,25]


x = int(input())

if x in diaspar:
  print("Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!")

elif x in diasimpar:
  print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")


elif x == 20:
  print("Você escolheu um dia que não irá acontecer nenhum show, tente novamente!")
  
else:
  print("Você escolheu um dia que não irá acontecer nenhum show, tente novamente!")
