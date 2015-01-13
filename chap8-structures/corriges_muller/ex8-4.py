# 3 parcours en profondeur d'un arbre binaire

arbre = [
    20, 5, 25, 3, 12, 21, 28, None, None, 8, 13, None, None, None, None,
    None, None, None, None, 6, None, None, None, None, None, None, None, None, None, None, None
]

def fils_gauche(t):
    g = 2 * t + 1
    if g < len(arbre):
        return g
    else:
        return None

def fils_droit(t):
    d = 2 * t + 2
    if d<len(arbre):
        return d
    else:
        return None

def pere(t):
    return (t - 1) // 2

def parcours_prefixe(t):
    print(arbre[t], end=" ")
    g = fils_gauche(t)
    if (g != None) and (arbre[g] != None):
        parcours_prefixe(g)
    d = fils_droit(t)
    if (d != None) and (arbre[d] != None):
        parcours_prefixe(d)

def parcours_infixe(t):
    g = fils_gauche(t)
    if (g != None) and (arbre[g] != None):
        parcours_infixe(g)
    print(arbre[t], end=" ")
    d = fils_droit(t)
    if (d != None) and (arbre[d] != None):
        parcours_infixe(d)

def parcours_suffixe(t):
    g = fils_gauche(t)
    if (g != None) and (arbre[g] != None):
        parcours_suffixe(g)
    d = fils_droit(t)
    if (d != None) and (arbre[d] != None):
        parcours_suffixe(d)
    print(arbre[t], end=" ")
    
def afficher(t, niveau=0):
    if t is not None:
        print(niveau * '  ', arbre[t])
        g = fils_gauche(t)
        d = fils_droit(t)
        afficher(g, niveau+1)
        afficher(d, niveau+1)

print("Parcours préfixé:")
parcours_prefixe(0)
print()
print("Parcours infixé:")
parcours_infixe(0)
print()
print("Parcours suffixé:")
parcours_suffixe(0)
print()

print(afficher(0))