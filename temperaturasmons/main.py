def temperatura_Mons(T):

    tamaño = len(T)
    frio = 0
    menosfrio = 0


    for i in range(tamaño):
        if T[i] > menosfrio:
            menosfrio = T[i]
        elif T[i] < frio:
            frio = T[i]

    print(frio, menosfrio)

    mediaTemperatura = sum(T) / tamaño


    print(f"a menor temperatura foi de {frio}Cº\na temperatura mais alta foi de {menosfrio}Cº\na media de temperatura é de {mediaTemperatura}Cº")



temperatura_Mons(T = [-10,-9,0,1,2,5,-2,-4])