def isEmpty(s):
    if len(s) == 0:
        print(True)
    else:
        print(False)
    
def Peek(s):
    if len(s) == 0:
        return False
    else:
        print(s[-1])

def Display(s):
    if len(s) == 0:
        print("Stack is Empty")
    else:
        print(s[-1], "<--Top")
        print(s[-1::-1])