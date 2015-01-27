class Stack(object):

    ''' Implémentation du type abstrait de pile à l'aide d'une liste Python '''

    def __init__(self):
        self._items = []
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, item):
        self._items.append(item)
        self._size += 1

    def pop(self):
        element = self._items[-1]
        del(self._items[-1])
        self._size -= 1
        return element

    def peek(self):
        return self._items[-1]

    def size(self):
        return self._size
        
    def __str__(self):
        return ' '.join([str(e) for e in self._items])
        
        
def test():
    s = Stack()
    s.is_empty()
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
    s.is_empty()
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