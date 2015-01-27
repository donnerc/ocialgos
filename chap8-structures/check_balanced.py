from ds.stack import Stack

def check_balanced(expr):
    
    opening = '([{'
    closing = ')]}'
    
    opening_d = {opening[i] : closing[i] for i in range(len(opening))}
    closing_d = {closing[i] : opening[i] for i in range(len(opening))}
    
    s = Stack()
    for i, c in enumerate(expr):
        if c in opening_d:
            s.push(c)
        if c in closing_d:
            if not s.is_empty() and opening_d[s.peek()] == c:
                s.pop()
            else:
                print('parenthèse fermante en trop au caractère', i+1)
                return False
                
    return s.size() == 0
    
    
def test():
    exprs = {
        '(())' : True,
        '({})' : True,
        '(1+3)*[(4+2)*2 + (5*1)*2]' : True,
        '((())' : False,
        '(()))' : False,
        '({)}' : False,
        '))((' : False,
        '}][{' : False,
    }
    
    for expr, expected in exprs.items():
        print(expr, expected == check_balanced(expr))
        
if __name__ == '__main__':
    test()
        
            
    