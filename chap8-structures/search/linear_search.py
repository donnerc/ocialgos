# Code de recherche binaire dans une liste triée issue du magnifique ouvrage
# "Grokking algorihthms, http://www.manning.com/bhargava/

nombres = [1, 4, 7, 3, 9, 24]

# pour que l'algorithme fonctionne, il faut que la liste soit triée
nombres.sort()

def linear_search(liste, item):
    
    low = 0
    high = len(liste) - 1
    
    while low <= high:
        guess = liste[low]
        
        if guess == item:
            return low
        else:
            low = low + 1
            
    return None
    
        
def test():
    # on rajoute [30] comme valeur qui ne se trouve pas dans la liste
    print(nombres)
    for (i, n) in enumerate(nombres + [30]):
        print(n, linear_search(nombres, n), i)

if __name__ == '__main__':
    test()
