# Code de recherche binaire dans une liste triée (version récursive)

nombres = [1, 4, 7, 3, 9, 24]

# pour que l'algorithme fonctionne, il faut que la liste soit triée
nombres.sort()

def search(n, start=0, end=None):
    
    # pour donner à la variable locale 'end' une valeur par défaut de len(nombres) - 1
    end = end or len(nombres) - 1
    
    middle = (start + end) // 2
    if start == middle:
        if n == nombres[start]:
            return start
        else:
            return None
            
    if n < nombres[middle]:
        return search(n, start=start, end=middle)
        
    elif n > nombres[middle]:
        return search(n, start=middle, end=end)
        
    else:
        # n se trouve forcément dans la liste
        return middle
        
        
for (i, n) in enumerate(nombres):
    print(n, search(n), i)
        
