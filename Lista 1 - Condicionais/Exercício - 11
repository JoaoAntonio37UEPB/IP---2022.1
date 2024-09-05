vida_1 = int(input())
ataque_1 = int(input())
defesa_1 = int(input())
fraqueza_1 = input()
resistencia_1 = input()

nome = input()
vida_2 = int(input())
ataque_2 = int(input())
defesa_2 = int(input())
fraqueza_2 = input()
resistencia_2 = input()

acertou1 = 0
acertou2 = 0

turno1 = input()

# turno 1

if turno1 == 'Ataque Físico':
    vida_2 -= (ataque_1 - defesa_2)
    print(
        f'Turno: 1\nSão João usou Ataque Físico e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_2)} de vida.')

# fogo

elif turno1 == 'Agi':
    if resistencia_2 == 'fogo':
        vida_2 -= int((ataque_1 - defesa_2) / 2)
        if vida_2 < 0:
            vida_2 = 0
        print(
            f"Turno: 1\nSão João usou {turno1}, mas acertou uma resistência, portanto causou apenas {int((ataque_1 - defesa_2) / 2)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

    elif fraqueza_2 == 'fogo':
        vida_2 -= int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)
        acertou1 += 1
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f"Turno: 1\nIsso! São João usou {turno1} e acertou a fraqueza do adversário! A magia causou {int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

    else:
        vida_2 -= int((ataque_1 - defesa_2))
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f'Turno: 1\nSão João usou {turno1} e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_2)} de vida.')


# gelo
elif turno1 == 'Bufu':
    if resistencia_2 == 'gelo':
        vida_2 -= int((ataque_1 - defesa_2) / 2)
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f"Turno: 1\nSão João usou {turno1}, mas acertou uma resistência, portanto causou apenas {int((ataque_1 - defesa_2) / 2)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

    elif fraqueza_2 == 'gelo':
        vida_2 -= int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)
        acertou1 += 1
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f"Turno: 1\nIsso! São João usou {turno1} e acertou a fraqueza do adversário! A magia causou {int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

    else:
        vida_2 -= int((ataque_1 - defesa_2))
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f'Turno: 1\nSão João usou {turno1} e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_2)} de vida.')


# eletricidade
elif turno1 == 'Zio':
    if resistencia_2 == 'eletricidade':
        vida_2 -= int((ataque_1 - defesa_2) / 2)
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f"Turno: 1\nSão João usou {turno1}, mas acertou uma resistência, portanto causou apenas {int((ataque_1 - defesa_2) / 2)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

    elif fraqueza_2 == 'eletricidade':
        vida_2 -= int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)
        acertou1 += 1
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f"Turno: 1\nIsso! São João usou {turno1} e acertou a fraqueza do adversário! A magia causou {int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)} de dano em {nome} que agora tem {int(vida_2)} de vida.")
    else:
        vida_2 -= int((ataque_1 - defesa_2))
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f'Turno: 1\nSão João usou {turno1} e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_2)} de vida.')

# turno 2
if vida_2 == 0:
    print("Vitória! Parece que o Nahobino São João reinará nesse solstício!")
    exit()

if acertou1 == 1:
    print(f"Turno: 2\n{nome} teve sua fraqueza em {fraqueza_2} acertada, portanto não poderá agir.")

else:
    turno2 = input()

    if turno2 == 'Ataque Físico':
        vida_1 -= int((ataque_2 - defesa_1))
        if vida_1 < 0:
            vida_1 = 0


        print(
            f'Turno: 2\n{nome}usou Ataque Físico e causou {ataque_2 - defesa_1} de dano em São João que agora tem {int(vida_1)} de vida.')

    # fogo

    elif turno2 == 'Agi':
        if resistencia_1 == 'fogo':
            vida_1 -= int((ataque_2 - defesa_1) / 2)

            if vida_1 < 0:
                vida_1 = 0

            print(
                f'Turno: 2\n{nome} usou {turno2}, mas acertou uma resistência, portanto causou apenas {int((ataque_2 - defesa_1) / 2)} de dano em São João que agora tem {int(vida_1)} de vida.')

        elif fraqueza_1 == 'fogo':
            vida_1 -= int((ataque_2 - defesa_1) + (ataque_2 - defesa_1) * 0.7)
            acertou2 += 1

            if vida_1 < 0:
                vida_1 = 0

            print(
                f"Turno: 2\nVixe! {nome} usou {turno2} e acertou sua fraqueza! A magia causou {int((ataque_2 - defesa_1) + (ataque_2 - defesa_1) * 0.7)} de dano em São João que agora tem {int(vida_1)} de vida.")


        else:
            vida_1 -= int((ataque_2 - defesa_1))
            if vida_1 < 0:
                vida_1 = 0

            print(
                f'Turno: 2\n{nome} usou {turno2} e causou {ataque_2 - defesa_1} de dano em São João que agora tem {int(vida_1)} de vida.')


    # gelo
    elif turno2 == 'Bufu':
        if resistencia_1 == 'gelo':
            vida_1 -= int((ataque_2 - defesa_1) / 2)
            if vida_1 < 0:
                vida_1 = 0

            print(
                f'Turno: 2\n{nome} usou {turno2}, mas acertou uma resistência, portanto causou apenas {int((ataque_2 - defesa_1) / 2)} de dano em São João que agora tem {int(vida_1)} de vida.')

        elif fraqueza_1 == 'gelo':
            vida_1 -= int((ataque_2 - defesa_1) + (ataque_2 - defesa_1) * 0.7)
            acertou2 += 1
            if vida_1 < 0:
                vida_1 = 0

            print(
                f"Turno: 2\nVixe! {nome} usou {turno2} e acertou sua fraqueza! A magia causou {int((ataque_2 - defesa_1) + (ataque_2 - defesa_1) * 0.7)} de dano em São João que agora tem {int(vida_1)} de vida.")


        else:
            vida_1 -= int((ataque_2 - defesa_1))
            if vida_1 < 0:
                vida_1 = 0

            print(
                f'Turno: 2\nSão João usou {turno2} e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_1)} de vida.')


    # eletricidade
    elif turno2 == 'Zio':
        if resistencia_1 == 'eletricidade':
            vida_1 -= int((ataque_2 - defesa_1) / 2)
            if vida_1 < 0:
                vida_1 = 0

            print(
                f'Turno: 2\n{nome} usou {turno2}, mas acertou uma resistência, portanto causou apenas {int((ataque_2 - defesa_1) / 2)} de dano em São João que agora tem {int(vida_1)} de vida.')


        elif fraqueza_1 == 'eletricidade':
            vida_1 -= int((ataque_2 - defesa_1) + (ataque_2 - defesa_1) * 0.7)
            acertou2 += 1
            if vida_1 < 0:
                vida_1 = 0

            print(
                f"Turno: 2\nVixe! {nome} usou {turno2} e acertou sua fraqueza! A magia causou {int((ataque_2 - defesa_1) + (ataque_2 - defesa_1) * 0.7)} de dano em São João que agora tem {int(vida_1)} de vida.")

        else:
            vida_1 -= int((ataque_2 - defesa_1))
            if vida_1 < 0:
                vida_1 = 0

            print(
                f'Turno: 2\nSão João usou {turno2} e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_1)} de vida.')

    if vida_1 == 0:
        print(f"Morremos… Parece que {nome} tem mais chances de ascender ao trono da Midsommar…")
        exit()

# turno 3
if acertou2 == 1:
    print(f"Turno: 3\nSão João teve sua fraqueza em {fraqueza_1} acertada, portanto não poderá agir.")
else:

    turno3 = input()
    if turno3 == 'Ataque Físico':
        vida_2 -= int((ataque_1 - defesa_2))
        if vida_2 < 0:
            vida_2 = 0
        int(vida_2)
        print(
            f'Turno: 3\nSão João usou Ataque Físico e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_2)} de vida.')

    # fogo

    elif turno3 == 'Agi':
        if resistencia_2 == 'fogo':
            vida_2 -= int((ataque_1 - defesa_2) / 2)
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f"Turno: 3\nSão João usou {turno3}, mas acertou uma resistência, portanto causou apenas {int((ataque_1 - defesa_2) / 2)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

        elif fraqueza_2 == 'fogo':
            vida_2 -= int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f"Turno: 3\nIsso! São João usou {turno3} e acertou a fraqueza do adversário! A magia causou {int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

        else:
            vida_2 -= int((ataque_1 - defesa_2))
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f'Turno: 3\nSão João usou {turno3} e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_2)} de vida.')


    # gelo
    elif turno3 == 'Bufu':
        if resistencia_2 == 'gelo':
            vida_2 -= int((ataque_1 - defesa_2)/ 2)
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f"Turno: 3\nSão João usou {turno3}, mas acertou uma resistência, portanto causou apenas {int((ataque_1 - defesa_2) / 2)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

        elif fraqueza_2 == 'gelo':
            vida_2 -= int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f"Turno: 3\nIsso! São João usou {turno3} e acertou a fraqueza do adversário! A magia causou {int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

        else:
            vida_2 -= int((ataque_1 - defesa_2))
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f'Turno: 3\nSão João usou {turno3} e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_2)} de vida.')


    # eletricidade
    elif turno3 == 'Zio':
        if resistencia_2 == 'eletricidade':
            vida_2 -= int((ataque_1 - defesa_2) / 2)
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f"Turno: 3\nSão João usou {turno3}, mas acertou uma resistência, portanto causou apenas {int((ataque_1 - defesa_2) / 2)} de dano em {nome} que agora tem {int(vida_2)} de vida.")

        elif fraqueza_2 == 'eletricidade':
            vida_2 -= int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f"Turno: 3\nIsso! São João usou {turno3} e acertou a fraqueza do adversário! A magia causou {int((ataque_1 - defesa_2) + (ataque_1 - defesa_2) * 0.7)} de dano em {nome} que agora tem {int(vida_2)} de vida.")
        else:
            vida_2 -= int((ataque_1 - defesa_2))
            if vida_2 < 0:
                vida_2 = 0
            int(vida_2)
            print(
                f'Turno: 3\nSão João usou {turno3} e causou {ataque_1 - defesa_2} de dano em {nome} que agora tem {int(vida_2)} de vida.')



if vida_1 > 0 and vida_2 > 0:
    print("Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")

elif vida_1 > 0 and vida_2 <= 0:
    print("Vitória! Parece que o Nahobino São João reinará nesse solstício!")

else:
    print(f"Morremos… Parece que {nome} tem mais chances de ascender ao trono da Midsommar…")






