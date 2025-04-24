def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False
def push(stk,item):
    stk.append(item)
    top=len(stk)-1
def pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]
def display(stk):
    if isEmpty(stk):
        print("Stack is empty.")
    else:
        top=len(stk)-1
        print(stk[top],"<-- Top")
        for i in range(top-1,-1,-1):
            print(stk[i])

Stack=[]
top=None
while True:
    print("STACK OPERATIONS")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        item=int(input("Enter item: "))
        push(Stack,item)
    elif choice==2:
        item=pop(Stack)
        if item=="Underflow":
            print("Underflow! Stack is empty.")
        else:
            print("Popped item: ",item)
    elif choice==3:
        item=peek(Stack)
        if item=="Underflow":
            print("Underflow! Stack is empty.")
        else:
            print("Top item: ",item)
    elif choice==4:
        display(Stack)
    elif choice==5:
        break
    else:
        print("Invalid choice.")