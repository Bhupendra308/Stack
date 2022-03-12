s = []
def push(s):
    t = input("Enter your input : ")
    s.append(t)
    
def Pop(s):
    if len(s) == 0:
        print("stack is empty")
    else:
        t = s.pop()
        print(t)
        return t
