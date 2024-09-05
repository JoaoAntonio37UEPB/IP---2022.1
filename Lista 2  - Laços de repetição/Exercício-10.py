num = int(input())
if num <= 0:
    print("Isso está quebrado, acho que Howard pode me ajudar.")
    exit()
elif num>0 and num <3:
    print("Acho que bebi demais, eu juro que tinha mais estrelas!")
    exit()

somaDist = 0
tprimo = 0
primo = 0
nprimo = 0
cont = 0
ultimox = 0
ultimoy = 0
f ='0 1 1'
certos = 0
errado = 0
#Fibonnaci

ulitmo = 1
penuluitmo = 1
contf = 3
while contf <= num:
    proximo = ulitmo + penuluitmo
    f += f' {str(proximo)}'
    ulitmo = penuluitmo
    penuluitmo = proximo
    contf += 1



for c in range(0, num):


    estrela1x = int(input())
    estrela1y = int(input())

    if c > 0:
        dist = ((ultimox - estrela1x) ** 2 + (ultimoy - estrela1y) ** 2) ** 0.5
        print(f"Distância [star{cont} <-> star{cont + 1}]: {int(dist)}")
        somaDist += int(dist)

        if str(int(dist)) in f:
            certos += 1
        else:
            errado += 1

    ultimox = estrela1x
    ultimoy = estrela1y
    cont += 1

for i in range(1,somaDist+1):
    if somaDist % i == 0:
        tprimo += 1
    
if tprimo > 2:
    
    nprimo += 1
else:
    primo += 1



if certos == (num-1) and nprimo == 1:
    print("Yes! Eu consegui!")

elif certos == (num-1) and primo == 1:
    print("Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!")

elif errado == 1:
    print("Oh, não! Eu quase consegui!")

elif errado >= 2 and nprimo == 1:
    print("Eu vou acabar como o Stuart :/")

elif errado >= 2 and primo == 1:
    print("Pelo menos o programa está funcionando...")
