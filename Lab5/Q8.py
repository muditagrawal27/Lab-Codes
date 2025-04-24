def cls():
    print("\n" * 100)
def isEmpty(Queue):
    if Queue == []:
        return True
    else:
        return False
def enqueue(Queue,item):
    Queue.append(item)
    if len(Queue)==1:
        front=rear=0
    else:
        rear=len(Queue)-1
def dequeue(Queue):
    if isEmpty(Queue):
        return "Underflow"
    else:
        item=Queue.pop(0)
        if len(Queue)==0:
            front=rear=None
        return item
def peek(Queue):
    if isEmpty(Queue):
        return "Underflow"
    else:
        front=0
        return Queue[front]
def display(Queue):
    if isEmpty(Queue):
        print("Queue is empty.")
    else:
        front=0
        rear=len(Queue)-1
        print(Queue[front],"<-- Rear")
        for i in range(1,rear):
            print(Queue[i])
        print(Queue[rear],"<-- Front")

Queue=[]
front=None
while True:
    cls()
    print("QUEUE OPERATIONS")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        item=int(input("Enter item: "))
        enqueue(Queue,item)
        input("Press Enter to continue...")
    elif choice==2:
        item=dequeue(Queue)
        if item=="Underflow":
            print("Underflow! Queue is empty.")
        else:
            print("Dequeued item: ",item)
        input("Press Enter to continue...")
    elif choice==3:
        item=peek(Queue)
        if item=="Underflow":
            print("Underflow! Queue is empty.")
        else:
            print("Front item: ",item)
        input("Press Enter to continue...")
    elif choice==4:
        display(Queue)
        input("Press Enter to continue...")
    elif choice==5:
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")