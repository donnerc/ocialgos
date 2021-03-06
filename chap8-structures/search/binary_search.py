# Code de recherche binaire dans une liste triée (version récursive)

nombres = [1, 4, 7, 3, 9, 24]

# pour que l'algorithme fonctionne, il faut que la liste soit triée
nombres.sort()

def search(n, start=0, end=None):

    # pour donner à la variable locale 'end' une valeur par défaut de len(nombres) - 1
    end = end or len(nombres) - 1

    middle = (start + end) // 2
    if end - start <= 0:
        if n == nombres[middle]:
            return nombres[middle]
        else:
            return None
            
    if n < nombres[middle]:
        return search(n, start=start, end=middle-1)

    elif n > nombres[middle]:
        return search(n, start=middle+1, end=end)
    else:
        # n se trouve forcément dans la liste à la position middle
        return middle

def test():
    for (i, n) in enumerate(nombres):
        print(n, search(n), i)
    print(30, search(30))

test()