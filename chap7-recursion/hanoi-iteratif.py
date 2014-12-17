# Les tours de Hanoi
# Methode non recursive
# Completez les parties manquantes signalees par :
    # *************** A COMPLETER ***************

class Pile :
    "Definition d'une pile"

    def __init__(self):
        self.nb = 0
        self.elements = []

    def vide(self):
        return self.nb==0

    def empiler(self,k):
        self.elements.append(k)
        self.nb += 1

    def depiler(self):
        if not self.vide() :
            k = self.elements[self.nb-1]
            del self.elements[self.nb-1]
            self.nb -= 1
            return k
        else :
            print("La pile est vide")

    def remplissage(self):
        return self.nb

    def sommet(self):
        # renvoie ce qui est au sommet de la pile, mais sans depiler
        return self.elements[self.nb-1]

    def afficher(self):
        for k in range(self.nb):
            print(self.elements[k], end=" ")

##        k = self.nb-1
##        while k>=0:
##            print(self.elements[k],end=" ")
##            k-=1

    
tour1 = Pile()
tour2 = Pile()
tour3 = Pile()
tours = [tour1, tour2, tour3]   # liste des trois piles
pos_petit_disque = 0            # no de la tour ou se trouve le plus petit disque
fin = False                     # True quand une tour sera entierement reconstruite


def initialiser():
    # Empile sur la premiere tour n disques numerotes de 1 (le plus petit) a n
    n = int(input("Taille de la tour : "))
    for i in range(n):
        tour1.empiler(n-i)


def afficher_tours():
    # affiche l'etat des trois tours (le haut est a gauche, le bas a droite)
    print("tour 1 : ",end=" ")
    tour1.afficher()
    print()
    print("tour 2 : ",end=" ")
    tour2.afficher()
    print()
    print("tour 3 : ",end=" ")
    tour3.afficher()
    print()
    print()

def suivante(position):
    return (position + 1) % 3

def deplacer_petit():
    global pos_petit_disque
    # decale circulairement le petit disque sur la tour de droite
    if not tours[pos_petit_disque].vide():
        pos_suivante = suivante(pos_petit_disque)
        tours[pos_suivante].empiler(tours[pos_petit_disque].depiler())
        pos_petit_disque = pos_suivante

def deplacer_autre():
    # deplace le seul disque possible autre que le plus petit
    # 1. trouver ou est le disque à deplacer
    # 2. le mettre au bon endroit
    # condition d'arret : le seul disque deplacable est le plus petit
    global fin

    # trouver le plus petit sommet de pile autre que le plus petit disque
    a_deplacer = suivante(pos_petit_disque)

    if tours[a_deplacer].vide() or (not tours[suivante(a_deplacer)].vide()
             and tours[a_deplacer].sommet() > tours[suivante(a_deplacer)].sommet()):
        a_deplacer = suivante(a_deplacer)
        if tours[a_deplacer].vide():
            fin = True
            return None

    destination = suivante(a_deplacer)
    # si la prochaine tour est occupée par le plus petit, il faut la
    # mettre à la suivante
    if destination == pos_petit_disque:
        destination = suivante(destination)

    # faire le déplacement
    tours[destination].empiler(tours[a_deplacer].depiler())

# programme principal
initialiser()
afficher_tours()
while not fin :
    deplacer_petit()
    afficher_tours()
    deplacer_autre()
    if not fin :
        afficher_tours()
