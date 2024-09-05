
n = int(input())

svence = 0
rvence = 0
empate = 0

for c in range(0,n):

    sheldon = input()
    raj = input()

    if sheldon == raj:

        empate += 1


    elif sheldon == 'lagarto' and raj == 'spock':
            svence += 1

    elif sheldon == 'spock' and raj == 'tesoura':
            svence += 1

    elif sheldon == 'tesoura' and raj == 'lagarto':
            svence += 1

    else:
        rvence += 1






if svence == rvence or empate == n:
    print("Oh não, precisamos de outra rodada.")

elif svence > rvence:
    print("BAZINGA! EU SOU O SENHOR DA SALA!")

else:
    print("ENGOLE ESSA, SHELDON!")
