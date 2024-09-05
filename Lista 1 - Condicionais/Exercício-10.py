n1 = input()
v1 = int(input())


n2 = input()
v2 = int(input())


n3 = input()
v3 = int(input())



#valor1 menor
if v1<v2 and v1<v3:
    print(f"{n1} {v1}")
    if v2<v3:
        print(f"{n2} {v2}")
        print(f"{n3} {v3}")
    else:
        print(f"{n3} {v3}")
        print(f"{n2} {v2}")

#valor2 menor

elif v2<v1 and v2<v3:
    print(f"{n2} {v2}")
    if v1<v3:
        print(f"{n1} {v1}")
        print(f"{n3} {v3}")
    else:
        print(f"{n3} {v3}")
        print(f"{n1} {v1}")

#valor3 menor
elif v3<v2 and v3<v1:
    print(f"{n3} {v3}")
    if v1<v2:
        print(f"{n1} {v1}")
        print(f"{n2} {v2}")
    else:
        print(f"{n2} {v2}")
        print(f"{n1} {v1}")
        

#Todos os valores iguais

elif v1 == v2  and v2 == v3:
    if n1<n2 and n1<n3:
        print(f"{n1} {v1}")
        if n2<n3:
            print(f"{n2} {v2}")
            print(f"{n3} {v3}")
        else:
            print(f"{n3} {v3}")
            print(f"{n2} {v2}")

    elif n2<n1 and n2<n3:
        print(f"{n2} {v2}")
        if n1<n3:
            print(f"{n1} {v1}")
            print(f"{n3} {v3}")
        else:
            print(f"{n3} {v3}")
            print(f"{n1} {v1}")

    elif n3<n1 and n3<n2:
        print(f"{n3} {v3}")
        if n1<n2:
            print(f"{n1} {v1}")
            print(f"{n2} {v2}")
        else:
            print(f"{n2} {v2}")
            print(f"{n1} {v1}")        
        
#empate v1 e v2

elif v1 == v2 and v1<v3:
    if n1<n2:
        print(f"{n1} {v1}")
        print(f"{n2} {v2}")
        print(f"{n3} {v3}")
    else:
        print(f"{n2} {v2}")
        print(f"{n1} {v1}")
        print(f"{n3} {v3}")
        
        
#empate v1 e v3

elif v1 == v3 and v1<v2:
    if n1<n3:
        print(f"{n1} {v1}")
        print(f"{n3} {v3}")
        print(f"{n2} {v2}")
    else:
        print(f"{n3} {v3}")
        print(f"{n1} {v1}")
        print(f"{n2} {v2}")

#empate v2 e v3

elif v2 == v3 and v2<v1:
    if n2<n3:
        print(f"{n2} {v2}")
        print(f"{n3} {v3}")
        print(f"{n1} {v1}")
    else:
        print(f"{n3} {v3}")
        print(f"{n2} {v2}")
        print(f"{n1} {v1}")        
        
