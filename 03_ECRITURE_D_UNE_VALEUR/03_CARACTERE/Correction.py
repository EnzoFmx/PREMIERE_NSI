def up_pour_Bob(chaine):
    resultat_final = ''
    for i in chaine :
        if ord(i) < ord("z") and ord(i)>ord('a'):
            resultat_final += chr(ord(i)-32)
        else :
            resultat_final += i
    return resultat_final

def cesar(texte,v) :
    #Methode avec chr/ord
    s= ''
    for lettre in texte :
        num_nouvelle_lettre = ord(lettre) + v
        if num_nouvelle_lettre > 90 :
            s += chr(num_nouvelle_lettre - 26)
        else :
            s += chr(num_nouvelle_lettre)
    return s

def cesar(texte,cle):
    #Methode avec alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for ind in range(len(texte)) :
        nouvelle_lettre = (alphabet.index(texte[lettre])+cle)%25
        s += alphabet[nouvelle_lettre]
    return s

def vigenere(texte,cle):
    #Methode avec alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for ind in range(len(texte)) :
        cle_decal = alphabet.index(cle[ind%len(cle)])
        nouvelle_lettre = (alphabet.index(texte[lettre])+cle_decal)%25
        s += alphabet[nouvelle_lettre]
    return s