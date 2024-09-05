mensagem = False
ganhou = 0
cont = 0

ultimo =''


while (mensagem == False):


    feitos = input()



    if feitos == 'Começou a Trabalhar na Caltech' and cont == 0:

        cont += 1
        ganhou += 1

    elif feitos == 'Trabalho sobre a String Theory' and cont == 1:

        cont += 1
        ganhou += 1

    elif feitos == 'Ganhar o Chancellor de ciência' and cont == 2:

        cont += 1
        ganhou += 1

    elif feitos == 'Pensar na Teoria de Cooper-Hofstader' and cont == 3:

        cont += 1
        ganhou += 1

    elif feitos == 'Criou a Super Assimetria' and cont == 4:

        cont += 1
        ganhou += 1

    elif feitos == 'Ganhar o Nobel' and cont == 5:
        ganhou += 1

    elif feitos == 'É o fim da Estrada pra Sheldon Cooper':
        mensagem = True


    elif feitos == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or feitos == 'Leonard seu anão covarde' or feitos == 'Tu é muito burro Raj':

        print('Não xingue seus amigos Sheldon!')



    elif feitos == 'Bazinga':

        if cont == 0:
            

            cont += 0
            ganhou += 0

        elif (ultimo == 'Começou a Trabalhar na Caltech' and cont == 1) or (ultimo == 'Trabalho sobre a String Theory' and cont == 2) or (ultimo == 'Ganhar o Chancellor de ciência' and cont == 3) or (ultimo == 'Pensar na Teoria de Cooper-Hofstader'  and cont == 4) or (ultimo == 'Criou a Super Assimetria' and cont == 5):

          
            cont -= 1
            ganhou -= 1

        else:

           
            cont += 0
            ganhou += 0

    ultimo = feitos
    


    if ganhou == 6:
        print('Você conseguiu Sheldon, o Nobel é seu!!!')
        mensagem = True


    elif feitos == 'É o fim da Estrada pra Sheldon Cooper' and cont == 0:
        print("Que potencial desperdiçado...")

    elif feitos == 'É o fim da Estrada pra Sheldon Cooper' and ganhou <= 2 and ganhou >= 1:
        print("Tão perto, mas tão longe")

    elif feitos == 'É o fim da Estrada pra Sheldon Cooper' and ganhou <= 4 and ganhou >= 3:
        print("Não desista Sheldon, você ainda têm muito para alcançar!")

    elif feitos == 'É o fim da Estrada pra Sheldon Cooper' and ganhou == 5:
        print("Nãoooooo, esse momento ia ser seu Sheldon")

