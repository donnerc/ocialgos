#!/bin/python3

'''

Ce fichier contient une définition d'une file en Python

'''

class Queue(object):
    
    def __init__(self):
        self._elements = []
        
    def enqueue(self, item):
        self._elements.append(item)
        
    def dequeue(self):
        element = self._elements[0]
        del(self._elements[0])
        self._size -= 1
        return element
    
    def empty(self):
        return self._numbers == 0
    
    def size(self):
        return self._numbers
        
    def __str__(self):
        return ' '.join([str(e) for e in self._elements])
        