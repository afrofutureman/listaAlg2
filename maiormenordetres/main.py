
def maior(a, b, c):
    if a > b and a > c:
        maiorr = a
    elif b > a and b > c:
        maiorr = b
    elif c > b and c > a:
        maiorr = c
    print(maiorr)    
    return maiorr

def menor(a, b, c):
    if a < b and a < c:
        menorr = a
    elif b < a and b < c:
        menorr = b
    elif c < b and c < a:
        menorr = c
    print(menorr)    
    return menorr

a, b, c = input("digite 3 numeros (separados por espaços)").split(" ")
a = int(a)
b = int(b)
c = int(c)

maior(a,b,c)
menor(a,b,c)