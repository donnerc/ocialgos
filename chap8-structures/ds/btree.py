#!/bin/python3

'''

Ce fichier contient une définition d'un arbre binaire en Python

'''

class Node(object):
    
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def left(self):
        return self.left
        
    def right(self):
        return self.right
        
    def __str__(self):
        return 'Node(root={}, left={}, right={})'.format(self.value, self.left, self.right)
        


class BTree(object):
    
    def __init__(self, root=None):
        # code à compléter
        self.root = root or Node(None)
        self.current_node = self.root
        self.size = 1
    
    def depth(self):
        # todo : à implémenter par la suite, d'abord comme une fonction et ensuite
        # en utilisant un attribut depth qu'il faut mettre à jour
        pass
    
    def size(self):
        return self.size()
        
    def draw(self):
        pass
    
    
if __name__ == '__main__':
    tree = BTree(Node(10, Node(5)))
    print(tree.root.left)