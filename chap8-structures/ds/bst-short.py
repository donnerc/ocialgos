#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# documentation pour pydot : https://pythonhaven.wordpress.com/tag/pydot/
import pydot

class Side(object):
    L = 0
    R = 1


class NodeError(Exception):

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return self.msg


def opposite_side(side):
    return (side + 1) % 2


class TreeNode(object):

    def __init__(
        self, key, val, left=None, right=None,
        parent=None, side_in_parent=None
    ):
        self.key = key
        self.payload = val
        self.child = [left, right]
        self.parent = parent
        self.side_in_parent = side_in_parent
        
    def __str__(self):
        return str(self.key)

    def has_child(self, side):
        return self.child[side]

    def is_child(self, side=None):
        return self.side_in_parent == side

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.child[Side.L] or self.child[Side.R])

    def has_any_child(self):
        return self.child[Side.R] or self.child[Side.L]

    def has_both_children(self):
        return self.child[Side.R] and self.child[Side.L]

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.child[Side.L] = lc
        self.child[Side.R] = rc

        for side in [Side.L, Side.R]:
            if self.has_child(side):
                self.child[side].parent = self
                
                
    def splice_out(self):
        '''

        Supprimer le noeud de l'arbre. On suppose que ce noeud n'a qu'un seul
        fils.

        '''
        if self.is_leaf():
            self.parent.child[self.side_in_parent] = None

        elif not self.has_both_children():
            child_side = Side.L
            if self.has_child(Side.R):
                child_side = Side.L
            unique_child = self.child[child_side]
            self.parent.child[self.side_in_parent] = unique_child
        else:
            raise NodeError('Error, cannot splice out node with two childs')

    def find_successor(self, down=True):
        '''

        Le paramètre 'down' indique s'il faut chercher le successeur dans le
        sous arbre ou en amont. Par défaut, on cherche le successeur dans le
        sous-arbre droit.

        Le successeur est en fait le prochain noeud dans l'ordre croissant. Il
        se trouve soit à l'extrême gauche du sous-arbre droit si ce sous-arbre
        existe. Dans le cas contraire, il s'agit du premier ancêtre qui
        contient le noeud courant dans son sous-arbre gauche.

        '''
        succ = None
        if down and self.has_child(Side.R):
            succ = self.child[Side.R].find_min()
        elif not down and self.parent is not None:
            if self.is_child(Side.L):
                succ = self.parent
            else:
                succ = self.parent.find_successor(down=False)
        return succ

    def find_min(self):
        current = self
        while current.has_child(Side.L):
            current = current.child[Side.L]
        return current


'''

Pour bien comprendre ce code, il faut faire les quelques tests suivants et
peut-être encore d'autres.

::

    >>> None or 'salut'
    'salut'
    >>> 'salut' and 'trois'
    'trois'
    >>> None and 'trois'
    >>> (None and 'trois') == None
    True

'''


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

    def _put(self, key, val, cur_node):
        if key < cur_node.key:
            side = Side.L
        else:
            side = Side.R

        if cur_node.has_child(side):
            self._put(key, val, cur_node.child[side])
        else:
            cur_node.child[side] = TreeNode(
                key, val,
                parent=cur_node,
                side_in_parent=side
            )

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

    def _get(self, key, cur_node):
        if not cur_node:
            return None
        elif cur_node.key == key:
            return cur_node
        elif key < cur_node.key:
            return self._get(key, cur_node.child[Side.L])
        else:
            return self._get(key, cur_node.child[Side.R])

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
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

    def remove(self, cur_node):
        if cur_node.is_leaf():  # leaf
            if cur_node.id_child(Side.L):
                cur_node.parent.child[Side.L] = None
            else:
                cur_node.parent.child[Side.R] = None

        elif cur_node.has_both_children():  # interior
            succ = cur_node.find_successor()
            succ.splice_out()
            cur_node.key = succ.key
            cur_node.payload = succ.payload

        else:  # this node has one child

            # déterminer de quel côté se situe le fils
            side = Side.L
            if cur_node.has_child[Side.R]:
                side = Side.R

            unique_child = cur_node.child[side]

            # changer la référence dans le parent
            cur_node.parent[cur_node.side_in_parent] = unique_child
            # changer la référence dans le fils vers le parent du noeud
            # courant
            unique_child.side_in_parent = cur_node.side_in_parent
            unique_child.parent = cur_node.parent

    def draw(self, current_node=None, graph=None, no_iter=None, filename=None):
        # parcourirdepuis la racine et rajouter les noeuds (faire un parcours préfixé ???)
        # TODO: write code...:
        # création du graphe permettant de représenter l'arbre
        graph = graph or pydot.Dot(graph_type='graph')
        current_node = current_node or self.root
        no_iter = no_iter or 1
        filename = filename or 'trees/bst.png'
        
        if no_iter == 1:
            with open('tree.html', mode='w') as fd:
                fd.write('<h1>Representation de l\'arbre</h1>\n')
                

        for (side, child) in enumerate(current_node.child):
            if child:
                edge = pydot.Edge(str(current_node), str(child))
                graph.add_edge(edge)
                self.draw(child, graph, no_iter=no_iter+1)
            else:
                side = str(side)
                empty_node = pydot.Node("empty-"+str(current_node)+"-"+side, style="filled", fillcolor="red", shape="point", width=".2", height=".2")
                graph.add_node(empty_node)
                edge = pydot.Edge(str(current_node), empty_node)
                graph.add_edge(edge)
                
        if current_node.is_root():
            graph.write_png(filename)

            
class HTML(object):
    
    def __init__(self, filename):
        self.filename = filename
        self.html = '<h1>Reprsentation de l\'arbre</h1>'
        
    def add_image(self, image):
        self.html += '<div style="display: inline; border: solid 1px black"><img src="{image}" />{image}</div>\n'.format(image=image)
        
    def __del__(self):
        
        with open(self.filename, mode='w') as fd:
            fd.write(self.html)
        
def snapshot(tree, html, i):
    filename = 'trees/tree' + str(i) + '.png'
    tree.draw(filename=filename)
    html.add_image(filename)

def test():
    from random import shuffle
    
    t = BinarySearchTree()
    keys = [1,2,3,4,5,6,7,8]
    keys = list(set((1,3,5,2,4,7,5,9,3,7,78, 10, 15, 21)))
    shuffle(keys)
    print(keys)
    
    html = HTML('tree.html')
    for i, k in enumerate(keys):
        t[k] = True
        snapshot(t, html, i)
        



if __name__ == '__main__':
    test()
