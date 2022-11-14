# Partie bonus :

def or_bit_a_bit(bin1,bin2):
    """Fonction permettant d'appliquer l'operateur ou bit à bit
    param bin1,bin2 : (str) Nombre binaire en chaîne de caractère
    return : (str) résultat de l'opération"""
    #Mise en forme :
    if bin1[:2] == '0b' :
        bin1 = bin1[2:]
    if bin2[:2] == '0b' :
        bin2 = bin2[2:]
    #Calcul :
    res = ''
    len_min = min(len(bin1),len(bin2))
    i = -1
    # Attention on ajoute à gauche, on part de la fin c'est pour cela que i est négatif.
    while -i <= len_min :
        if bin1[i] == "0" and bin2[i] == "0" :
            res = "0" + res
        else :
            res = "1" + res
        i -=1
    #Lorsqu'on a atteint la longueur du plus petit nombre :
    #On ajoute la suite du plus grand nombre
    if -i == len(bin1)+1:
        while -i <= len(bin2) :
            res = bin2[i] + res
            i-=1
        #Autre méthode :
        #res = bin2[:i] + res
    if -i == len(bin2)+1:
        while -i <= len(bin1) :
            res = bin1[i] + res
            i-=1
        #Autre méthode :
        #res = bin1[:i] + res
    return res
    

def et_bit_a_bit(bin1,bin2):
    """Fonction permettant d'appliquer l'operateur et bit à bit
    param bin1,bin2 : (str) Nombre binaire en chaîne de caractère
    return : (str) résultat de l'opération"""
    #Mise en forme :
    if bin1[:2] == '0b' :
        bin1 = bin1[2:]
    if bin2[:2] == '0b' :
        bin2 = bin2[2:]
    #Calcul :
    res = ''
    len_min = min(len(bin1),len(bin2))
    i = -1
    # Attention on ajoute à gauche, on part de la fin c'est pour cela que i est négatif.
    while -i <= len_min :
        if bin1[i] == "1" and bin2[i] == "1" :
            res = "1" + res
        else :
            res = "0" + res
        i -=1
    #Utilisation des slices pour enlever les 0 de gauches (inutiles), tout en laissant au minimum un 0
    j = 0
    while res[j] == '0' and j != len(res)-1 :
        j+=1
    return res[j:]

def non_bit_a_bit(bin1):
    #Mise en forme :
    if bin1[:2] == '0b' :
        bin1 = bin1[2:]
    res = ''
    for i in bin1 :
        if i == '0':
            res += '1'
        else :
            res += '0'
    j = 0
    #Utilisation des slices pour enlever les 0 de gauches (inutiles), tout en laissant au minimum un 0
    while res[j] == '0' and j != len(res)-1:
        j+=1
    return res[j:]
        
        
        

print(or_bit_a_bit(bin(5),bin(40)))
print(et_bit_a_bit(bin(5),bin(40)))
print(non_bit_a_bit(bin(40)))