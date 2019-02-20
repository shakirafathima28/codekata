print("STACK IMPLEMENTATION")
stack= []
while True:
    print("What you want to perform? \n 1.Insert an element,2.Remove an element,3.check Size of stack,4.Emptiness of stack,5.EXIT")
    n = int(input())
    if n == 1:
        print("enter the element you want to insert:")
        l = input()
        stack.append(l)
        print("Elements in stack are:",stack)
    elif n == 2:
        if stack==[]:
            print("Empty Stack.You cannot delete!!")
        else:
            stack.pop()
            print ("Elements in stack are :",stack)
    elif n==3:
        print("Size of stack is:",len(stack))
        
    elif n==4:
        if stack==[]:
            print("Your stack is Empty!!")
        else:
            print("You have ",len(stack),"elements in tour stack")
        
    elif n==5:
        print("Exit")
        break
