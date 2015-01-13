nombres = [1, 4, 7, 3, 9, 24]

# pour que l'algorithme fonctionne, il faut que la liste soit triée
nombres.sort()

def search(liste, item):
    
    low = 0
    high = len(liste) -1
    
    while low <= high:
        middle = (low + high) // 2
        guess = liste[middle]
        
        if guess == item:
            return middle
            
        if guess >= item:
            high = middle - 1
        else:
            low = middle + 1
            
    return None
        
def test():        
    for (i, n) in enumerate(nombres + [30]):
        print(search(nombres, n), i)