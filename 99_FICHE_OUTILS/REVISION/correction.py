def premiers_elements(n):
    res = []
    for i in range(n+1):
        res.append(i)
    return res

def premieres_lettres(n):
    res = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(n) :
        res.append(alphabet[i])
    return res

def suite_mystere(a,b,c):
    etape = 0
    u0 = a+b
    while u0 <= 10000 :
        if u0%2 == 0 :
            u0 = (u0+a+b)*c
        else :
            u0 = (u0+a+c)*b
        etape= etape +1
    return etape

def add(l1,l2):
    return l1+l2

def inverse(tab):
    tab_final = []
    long = len(tab)-1
    for i in range len(tab):
        tab_final.append(tab[long])
        long =long-1
    return tab_final