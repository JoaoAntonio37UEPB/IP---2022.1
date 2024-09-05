temp = 30
fome = False
net = 0



while(True):

    acao = input()
    if acao == 'ir para o grad' or acao == 'sair para a rua' or acao == 'comer uma quentinha' or acao == 'conectar no wifi' or acao == 'parar':

        if acao == "ir para o grad":
            temp -= 5
            net += 300

        if acao == "sair para a rua":
            temp += 5

        if acao == "comer uma quentinha":
            fome = True

        if acao == "conectar no wifi":
            net += 100



    else:
        print("Entrada inválida")



    if(acao == 'parar'):
        break


#temperatura
if temp >= 30:
    print("A temperatura aqui não está agradável")
elif temp <= 25:
    print("Agora sim, está aconchegante")

#fome
if fome == False:
    print("Meu corpo precisa de comida")

#internet
if net<100:
    print("Essa conexão está horrível")


if temp <= 25 and fome == True and net >= 300:
    print("Finalmente um lugar preciso para mim!")
