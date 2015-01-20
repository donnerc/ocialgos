#!/usr/bin/python
# -*- coding: utf-8 -*-

import pydot


class TreeNode(object):

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        '''

        Si findSuccessor est appelé sur un noeud qui possède un fils droit, il
        retournera le plus petit noeud du sous-arbre correspondant. Le noeud
        retourné n'aura alors pas de fils gauche.

        '''
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        '''

        Supprimer le noeud de l'arbre. On suppose que ce noeud n'a qu'un seul
        fils.

        '''
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None

        # est-il possible qu'il y ait deux fils à ce stade? Si oui, je pense
        # que ce code peut créer des problèmes
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __str__(self):
        return str(self.key)


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior

            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
               # this node has one child

            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = \
                        currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild
                    )
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = \
                        currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = \
                        currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild
                    )


def draw(tree, current_node=None, graph=None, no_iter=None, filename=None):
    # parcourirdepuis la racine et rajouter les noeuds (faire un parcours
    # préfixé ???) TODO: write code...: création du graphe permettant de
    # représenter l'arbre
    graph = graph or pydot.Dot(graph_type='graph')
    current_node = current_node or tree.root
    no_iter = no_iter or 1
    filename = filename or 'trees/bst.png'

    if no_iter == 1:
        with open('tree.html', mode='w') as fd:
            fd.write('<h1>Representation de l\'arbre</h1>\n')

    for (side, child) in [(0, current_node.leftChild), (1, current_node.rightChild)]:
        if child:
            edge = pydot.Edge(str(current_node), str(child))
            graph.add_edge(edge)
            draw(tree, child, graph, no_iter=no_iter+1)
        else:
            side = str(side)
            empty_node = pydot.Node(
                "empty-"+str(current_node)+"-"+side,
                style="filled",
                fillcolor="red",
                shape="point",
                width=".2",
                height=".2"
            )
            graph.add_node(empty_node)
            edge = pydot.Edge(str(current_node), empty_node)
            graph.add_edge(edge)

    if current_node.isRoot():
        graph.write_png(filename)


class HTML(object):

    def __init__(self, filename):
        self.filename = filename
        self.html = '<h1>Repr&eacute;sentation de l\'arbre</h1>'

    def add_image(self, image):
        self.html += '<div style="display: inline; border: solid 1px black"><img src="{image}" style="display: inline" /><div style="display: inline-block">{image}</div></div>\n'.format(image=image)

    def __del__(self):

        with open(self.filename, mode='w') as fd:
            fd.write(self.html)


def snapshot(tree, html, i):
    filename = 'trees/tree-' + str(i) + '.png'
    draw(tree, filename=filename)
    html.add_image(filename)


def test():
    from random import shuffle

    t = BinarySearchTree()

    keys = [15, 5, 78, 21, 4, 1, 7, 10, 9, 2, 3]
    print(keys)

    html = HTML('tree.html')
    for i, k in enumerate(keys):
        t[k] = True
        snapshot(t, html, 'insert-'+str(k))

    for i, k in enumerate(keys):
        del t[k]
        snapshot(t, html, 'del-'+str(k))



if __name__ == '__main__':
    test()
