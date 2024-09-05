cont_beleza = 0
cont_vida = 0
cont_agua = 0
cont_temp = 0
cont_luas = 0

# contadores galaxia..

cont_buraco_s = 0

# contadores buraco negro..

cont_spin = 0
#true o false
TF = 0

instru = input()

if instru == '0001':
    instru = 1
elif instru == '0010':
    instru = 2
elif instru == '0011':
    instru = 3
elif instru == '0100':
    instru = 4

for c in range(0, instru):

    ler = input()
    # planeta..................................................................................

    if ler == '0101':

        while True:

            planeta = input()

            if planeta == 'End':
                break

            elif planeta == 'Quantidade de luas':

                quant_luas = input()

                if quant_luas == '0001':
                    quant_luas = 1
                elif quant_luas == '0010':
                    quant_luas = 2
                elif quant_luas == '0011':
                    quant_luas = 3


                cont_luas = quant_luas


            elif planeta == 'Beleza' or planeta == 'Possibilidade de vida extraterrestre' or planeta == 'Agua aparente' or planeta == 'Temperatura adequada':

                torf = input()

                if torf == 'End':
                    break

                TF = int(torf)



            if planeta == 'Beleza' and TF == 1:

                cont_beleza = 1
            
            elif planeta == 'Beleza' and TF == 0:
                cont_beleza = 0

            
            if planeta == 'Possibilidade de vida extraterrestre' and TF == 1:

                cont_vida = 1
            
            elif planeta == 'Possibilidade de vida extraterrestre' and TF == 0:
                
                cont_vida = 0
                
            
            if planeta == 'Agua aparente' and TF == 1:

                cont_agua = 1
            elif planeta == 'Agua aparente' and TF == 0:
              
                cont_agua = 0
               

            if planeta == 'Temperatura adequada' and TF == 1:

                cont_temp = 1
            
            elif planeta == 'Temperatura adequada' and TF == 0:
                cont_temp = 0
               

        #saidas :planeta....

        if cont_agua == 1 and cont_temp == 1 and cont_beleza == 1 and cont_vida == 1:

                print(f"Achamos o planeta ideal e ainda tem {cont_luas} lua(s)!")
                print("Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?")
                cont_beleza = 0
                cont_vida = 0
                cont_agua = 0
                cont_temp = 0
                cont_luas = 0

        elif cont_agua == 1 and cont_temp == 1 and cont_beleza == 1 and cont_vida == 0:

                print("Ainda nao sabemos se o planeta e habitavel, parece nao haver vida")
                cont_beleza = 0
                cont_vida = 0
                cont_agua = 0
                cont_temp = 0
                cont_luas = 0

        elif cont_agua == 1 and cont_temp == 1 and cont_beleza == 0 and cont_vida == 1:

                print(f"O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {cont_luas} lua(s) vamos omitir esse do relatorio!")
                cont_beleza = 0
                cont_vida = 0
                cont_agua = 0
                cont_temp = 0
                cont_luas = 0

        else:
                print("Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo")
                cont_beleza = 0
                cont_vida = 0
                cont_agua = 0
                cont_temp = 0
                cont_luas = 0

        

    # galaxia.....................................................................................

    elif ler == '1101':
        galaxia = input()

        if galaxia == '01100100':
            galaxia = 100

        elif galaxia == '11001000':
            galaxia = 200

        elif galaxia == '100101100':
            galaxia = 300

        buraco_super = input()
        if buraco_super == '1':
            cont_buraco_s = 1

        # saidas para Galáxia

        if cont_buraco_s == 1:
            print(f"Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de {galaxia} milhoes de planetas")

        else:
            print(f"Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham! Nao importa, ainda temos {galaxia} milhoes de planetas para observar algum deve apresentar possiblidade de vida")


    # buraco-negro.............................................................................

    elif ler == '0000':

        buraco_negro = input()

        if buraco_negro == '0101':
            buraco_negro = 5
        elif buraco_negro == '1010':
            buraco_negro = 10
        elif buraco_negro == '1111':
            buraco_negro = 15

        spin = input()
        if spin == '1':
            cont_spin = 1

        carga = input()

        if carga == '0000':
            carga = 'Carga neutra'

        elif carga == '0001':
            carga = 'Carga positiva'

        else:
            carga = 'Carga negativa'

        #saidas buraco negro

        print("Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!")
        print("De acordo com as analises, o buraco negro:")
        print(f"- Tem massa de aproximadamente {buraco_negro} milhoes massas solares")
        print(f"- Possui em media {cont_spin} rotacao(oes) por segundo")


        if carga == 'Carga neutra':
            print("- Apresenta carga inexistente ou nula")

        elif carga == 'Carga positiva':
            print("- Apresenta carga positiva")

        elif carga == 'Carga negativa':
            print("- Apresenta carga negativa")



    cont_buraco_s = 0


    cont_spin = 0
