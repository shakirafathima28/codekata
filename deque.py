print("QUEUE IMPLEMENTATION")
queue= []
while True:
    print("What you want to perform? \n 1.Insert an element,2.Remove an element,3.check Size of queue,4.Emptiness of stack,5.EXIT")
    n = int(input())
    if n == 1:
      
        print("enter the element you want to insert:")
        l = input()
        
        print("where you want to insert?\n 1.Front,2.Rear")
        z = int(input())
        if z == 1:
            queue.insert(0,l)
        elif z == 2:
            queue.append(l)
       
        print("Elements in queue are:",queue)
    elif n == 2:
        
        if queue==[]:
            print("Empty queue.You cannot delete!!")
        else:
            
            print("Where you want to remove?\n 1.Front,2.Rear")
            y= int(input())
            if y == 1:
                queue.pop(0)
            elif y == 2:
                queue.pop()
            print ("Elements in queue are :",queue)
    elif n==3:
        print("Size of queue is:",len(queue))
        
    elif n==4:
        if queue==[]:
            print("Your queue is Empty!!")
        else:
            print("You have ",len(queue),"elements in your queue")
        
    elif n==5:
        print("Exit")
        break

     
