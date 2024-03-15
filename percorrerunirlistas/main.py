#verificar se a solução é suficiente visto que devido à função
#set(), a lista se tranforma em um conjunto {} e não em lista []
def juntarListas_set(L1, L2):

    L = L1 + L2

    L = set(L)


    print(L)
    return L

L1=[0, 1, 3, 4, 5, 6, 7]
L2 = [2,3, 4, 7, 8, 9,10]

juntarListas_set(L1, L2)