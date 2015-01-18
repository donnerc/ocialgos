#!/usr/bin/python
# -*- coding: utf-8 -*-

class Side(object):
    L = 0
    R = 1

def opposite_side(side):
    return (side + 1) % 2

class TreeNode(object):

    def __init__(self, key, val, left=None, right=None, parent=None, side_in_parent=None):
        self.key = key
        self.payload = val
        self.child = [left, right]
        self.parent = parent
        self.side_in_parent = side_in_parent

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

    def has_2_children(self):
        return self.child[Side.R] or self.child[Side.L]

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.child[Side.L] = lc
        self.child[Side.R] = rc

        for side in [Side.L, Side.R]:
            if self.has_child(side):
                self.child[side] = self


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
    >>> 

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
                key,
                val,
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

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.child[Side.L])
        else:
            return self._get(key, current_node.child[Side.R])

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

    # que fait cette fonction exactement ???
    def splice_out(self):
        if self.is_leaf():
            self.parent.child[self.side_in_parent] = None

            # splice out suppose qu'il y a au maximum un seul fils ... j'ai
            # l'impression que cette fonction splice_out n'est pas bien foutue
        elif self.has_any_child():


                self.parent.child[self.side_in_parent] = self.child[side]
        elif self.has_any_child():
            # l'impresion que ce n'est pas bon ... 
            if self.has_child(Side.L):
                if self.is_child(Side.L):
                    self.parent.child[Side.L] = self.child[Side.L]
                else:
                    self.parent.child[Side.R] = self.child[Side.L]
                self.child[Side.L].parent = self.parent

            else:  # has no left child but has right child 
                if self.isSide.LChild():
                    self.parent.child[Side.L] = self.child[Side.R]
                else:
                    self.parent.child[Side.R] = self.child[Side.R]
                self.child[Side.R].parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.child[Side.R].findMin()
        else:
            if self.parent:
                if self.isSide.LChild():
                    succ = self.parent
                else:
                    self.parent.child[Side.R] = None
                    succ = self.parent.findSuccessor()
                    self.parent.child[Side.R] = self
        return succ

    def findMin(self):
        current = self
        while current.hasSide.LChild():
            current = current.child[Side.L]
        return current

    def remove(self, currentNode):
        if currentNode.is_leaf():  # leaf
            if currentNode == currentNode.parent.child[Side.L]:
                currentNode.parent.child[Side.L] = None
            else:
                currentNode.parent.child[Side.R] = None
        elif currentNode.hasBothChildren():  # interior

            succ = currentNode.findSuccessor()
            succ.splice_out()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
               # this node has one child

            if currentNode.hasSide.LChild():
                if currentNode.isSide.LChild():
                    currentNode.child[Side.L].parent = currentNode.parent
                    currentNode.parent.child[Side.L] = currentNode.child[Side.L]
                elif currentNode.isRightChild():
                    currentNode.child[Side.L].parent = currentNode.parent
                    currentNode.parent.child[Side.R] = \
                        currentNode.child[Side.L]
                else:
                    currentNode.replaceNodeData(currentNode.child[Side.L].key,
                        currentNode.child[Side.L].payload,
                        currentNode.child[Side.L],
                        currentNode.child[Side.L].child[Side.R]
                    )
            else:
                if currentNode.isSide.LChild():
                    currentNode.child[Side.R].parent = currentNode.parent
                    currentNode.parent.child[Side.L] = \
                        currentNode.child[Side.R]
                elif currentNode.isRightChild():
                    currentNode.child[Side.R].parent = currentNode.parent
                    currentNode.parent.child[Side.R] = \
                        currentNode.child[Side.R]
                else:
                    currentNode.replaceNodeData(currentNode.child[Side.R].key,
                        currentNode.child[Side.R].payload,
                        currentNode.child[Side.R].child[Side.L],
                        currentNode.child[Side.R].child[Side.R]
                    )


def test():
    mytree = BinarySearchTree()
    mytree[3] = 'red'
    mytree[4] = 'blue'
    mytree[6] = 'yellow'
    mytree[2] = 'at'

    print(mytree[6])
    print(mytree[2])


if __name__ == '__main__':
    test()