print("QUEUE IMPLEMENTATION")
queue= []
while True:
    print("What you want to perform? \n 1.Insert an element,2.Remove an element,3.check Size of queue,4.Emptiness of stack,5.EXIT")
    n = int(input())
    if n == 1:
        print("enter the element you want to insert:")
        l = input()
        queue.append(l)
        print("Elements in queue are:",queue)
    elif n == 2:
        if queue==[]:
            print("Empty queue.You cannot delete!!")
        else:
            queue.pop(0)
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

