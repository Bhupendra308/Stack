from undo import *
from test import *
def main():
    t = """
1.Push 
2.Pop
3.Peek 
4.Check if empty 
5.Display
6.Exit

"""

    while True:
        print(t)
        choice = int(input("Enter your choice (1-6) :"))
        if choice == 1:
            push(s)
        elif choice == 2:
            Pop(s)
        elif choice == 3:
            Peek(s)
        elif choice == 4:
            isEmpty(s)
        elif choice == 5:
            Display(s)
        elif choice == 6:
            break
        else:
            print("Wrong Input : ")
main()