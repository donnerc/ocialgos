class Grille(object):
    
    def __init__(self, string):
        
        self.string = string.rstrip()
        
    def _to_list(self):
        return [int(i) for i in self.string]
        