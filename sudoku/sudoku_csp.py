# -*- coding: utf-8 -*-

from constraint import *
from grille import Grille

problem = Problem(BacktrackingSolver())

n_cases = 81

# Définition des blocs de cases
blocs = [0]*9
blocs[0] = [0,1,2,9,10,11,18,19,20]
blocs[1] = [3,4,5,12,13,14,21,22,23]
blocs[2] = [6,7,8,15,16,17,24,25,26]
blocs[3] = [27,28,29,36,37,38,45,46,47]
blocs[4] = [30,31,32,39,40,41,48,49,50]
blocs[5] = [33,34,35,42,43,44,51,52,53]
blocs[6] = [54,55,56,63,64,65,72,73,74]
blocs[7] = [57,58,59,66,67,68,75,76,77]
blocs[8] = [60,61,62,69,70,71,78,79,80]

# Définition des contraintes
taille = 9

cases = [c for c in range(81)]
domain = [n+1 for n in range(9)]

rows = [c for c in range(9)]
cols = [c for c in range(9)]

# ajout des variables entières au problème
problem.addVariables(cases, domain)

# définition des contraintes
# contraintes de bloc
for bloc in blocs:
    for i in range(9):
        for j in [k for k in range(9) if k > i]:
            problem.addConstraint(lambda x, y: x != y, (bloc[i],bloc[j]))
            
# Contraintes de colonnes
for i in cols:
    for j in rows:
        problem.addConstraint(lambda x, y: x != y, (i, i + 9*j))
            
# Contraintes de lignes
for i in rows:
    for j in cols:
        problem.addConstraint(lambda x, y: x != y, (i*9, i*9 + j))
        
# chargement de la grille
with open('problemes.txt', 'r') as fd:
    grilles = fd.readlines()
    
sudoku = Grille(grilles[1])._to_list()
print(sudoku)

for case in cases:
    valeur = sudoku[case]
    if valeur != 0:
        problem.addConstraint(lambda x: x == valeur, (case,))
        
solutions = problem.getSolution()

print solutions