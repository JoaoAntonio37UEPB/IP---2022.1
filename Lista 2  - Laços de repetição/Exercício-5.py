boas = ruins = tot = 0


while(True):

    piada = input()
    
    if piada == 'Fim do Show!':
            break
    
    reacao = input()
    if reacao == 'BAZINGA!':
        boas += 1
        tot += 1

    else:
        ruins += 1
        tot += 1








if boas > (0.6*tot):
    
    print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')

elif ruins > (0.6*tot):
    
    print("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")
    
else:
     print("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")
    
    
    
    
    
    
