class file :
    "Definition d'une file"

    def __init__(self):
        self.nb = 0
        self.elements = []

    def vide(self):
        return self.nb==0

    def ajouter(self,k):
        self.elements.append(k)
        self.nb += 1

    def enlever(self):
        if not self.vide() :
            k = self.elements[0]
            del self.elements[0]
            self.nb -= 1
            return k
        else :
            print("La file est vide")

    def remplissage(self):
        return self.nb

    def afficher(self):
        k = 0
        while k<=self.nb-1:
            print(self.elements[k],end=" ")
            k+=1
    
queue = file()
print("Ajouts")
queue.ajouter(1)
queue.ajouter(2)
queue.ajouter(3)
queue.ajouter(4)
queue.afficher()
print()
print(queue.remplissage(), "element(s)")
print()
print("Suppressions")
queue.enlever()
queue.enlever()
queue.afficher()
print()
print(queue.remplissage(), "element(s)")





