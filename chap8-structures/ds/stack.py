class Stack(object):

    ''' Implémentation du type abstrait de pile à l'aide d'une liste Python '''

    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        element = self._items[len(self._items)-1]
        del(self._items[len(self._items)-1])
        return element

    def peek(self):
        return self._items[len(self._items)-1]

    def size(self):
        return len(self._items)
        
    def __str__(self):
        return str(self._items)
        
        
def test():
    s = Stack()
    s.isEmpty()
    print(s)
    s.push(4)
    print(s)
    s.push('dog')
    print(s)
    s.peek()
    print(s)
    s.push(True)
    print(s)
    s.size()
    print(s)
    s.isEmpty()
    print(s)
    s.push(8)
    print(s)
    s.pop()
    print(s)
    s.pop()
    print(s)
    s.size()
    print(s)
    
if __name__ == '__main__':
    test()