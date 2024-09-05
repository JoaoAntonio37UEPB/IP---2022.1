pedemoleque = input()
cpedemoleque = int(input())
f1 = cpedemoleque*2

cocada = input()
ccocada = int(input())
f2 = ccocada*5

maca = input()
cmaca = int(input())
f3 = cmaca*3

if f1>f2 and f1>f3:
    print(f"Oxe! Você ganhou {f1} reais vendendo {pedemoleque}. O povo gostou, visse?!")

elif f2>f1 and f2>f3:
    print(f"Oxe! Você ganhou {f2} reais vendendo {cocada}. O povo gostou, visse?!")

elif f3>f2 and f3>f1:
    print(f"Oxe! Você ganhou {f3} reais vendendo {maca}. O povo gostou, visse?!")

elif f1 == 0 and f2 == 0  and f3 == 0:
    print("A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...")

elif f1 == f2 and f1>f3:
    if cpedemoleque>ccocada:
        print(f"Oxe! Você ganhou {f1} reais vendendo {pedemoleque}. O povo gostou, visse?!")
    else:
        print(f"Oxe! Você ganhou {f2} reais vendendo {cocada}. O povo gostou, visse?!")

elif f1 == f3 and f1>f2:
     if cpedemoleque>ccocada:
        print(f"Oxe! Você ganhou {f1} reais vendendo {pedemoleque}. O povo gostou, visse?!")
     else:
        print(f"Oxe! Você ganhou {f3} reais vendendo {maca}. O povo gostou, visse?!")

