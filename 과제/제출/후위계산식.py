from tokenize import Double

class stack:
    def __init__(self):   # 스택 객체 생성
        self.items = []
    def push(self, item):  # 스택 요소 추가 push(.append())
        self.items.append(item)
    def pop(self):   # 스택 요소 삭제 pop()
        return self.items.pop()

acc = stack()
str = input().split()

for c in str:
    a = 0
    b = 0
    
    if c == '+':
        a = acc.pop()
        b = acc.pop()
        acc.push(a+b)
        
    elif c == '*':
        a = acc.pop()
        b = acc.pop()
        acc.push(a*b)
        
    elif c == '-':
        a = acc.pop()
        b = acc.pop()
        acc.push(b-a)
        
    elif c == '/':
        a = acc.pop()
        b = acc.pop()
        acc.push(b/a)
        
    else:
        c = int(c)
        acc.push(c)

print(acc.pop())
