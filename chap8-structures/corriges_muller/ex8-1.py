class pile :
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

    def afficher(self):
        k = self.nb-1
        while k>=0:
            print(self.elements[k],end=" ")
            k-=1
    
stack = pile()
print("Empilement")
stack.empiler(1)
stack.empiler(2)
stack.empiler(3)
stack.empiler(4)
stack.afficher()
print()
print(stack.remplissage(), "element(s)")
print()
print("Depilement")
stack.depiler()
stack.depiler()
stack.afficher()
print()
print(stack.remplissage(), "element(s)")





