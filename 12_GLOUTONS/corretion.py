systeme = [50,20,10,5,2,1]

def rendu_monnaie(a_rendre,systeme) :
    tab = []
    i = 0
    while a_rendre > 0 :
        element_sys = systeme[i]
        if a_rendre >= element_sys :
            tab.append(element_sys)
            a_rendre = a_rendre - element_sys
        else :
            i = i + 1
    return tab

# rendu_monnaie(49,systeme)
        