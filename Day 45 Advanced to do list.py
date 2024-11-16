

import os ,time
os.system("cls")

todo = []

def edit():
    time.sleep(0.5)
    os.system("cls")
    find = input("Name of the list to edit >")
    found = False
    for row in todo:
        if find in row:
            found = True
    if not found:
        print(f"Could not find the list with the name:{find}")
        return
    for row in todo:
        if find in row:
            print(f"Found the list with the name{find}")
            time.sleep(1)
            os.system("cls")
            print("The list has been removed!")
            time.sleep(1)
            todo.remove(row)
    name = input("Name >")
    pri = input("Priorty >").capitalize()
    due = input("Due >")
    row = [name, pri, due]
    todo.append(row)
    time.sleep(0.5)
    os.system("cls")
    print("Added")
    time.sleep(0.5)
    os.system("cls")


def add(): #adds things to the list by asking name priority and due date 
    time.sleep(0.5)
    os.system("cls")
    name = input("Name >")
    pri = input("Priorty >").capitalize()
    due = input("Due >")
    row = [name, pri, due]
    todo.append(row)
    time.sleep(0.5)
    os.system("cls")
    print("Added")
    time.sleep(0.5)
    os.system("cls")


def view():  
    
    options = input("1) All\n2) Priority\n")
    time.sleep(0.5)
    os.system("cls")
    if options == "1": #shows all the things
        
        for row in todo:
            for item in row:
                
                print(item , end=" | ",)
            print()
        print()    
        time.sleep(4)
        os.system("cls")    
    else:   #only shows the things which have the priority that the user has promoted
        priority = input("What priority? >").capitalize()
        os.system("cls")
        for row in todo:
            if priority in row:
                for item in row:
                  print(item,end=" | ")
                print()
        print()    
        time.sleep(3)
        os.system("cls")


def remove():
    time.sleep(0.5)
    os.system("cls")
    find = input("Name of the list to remove >")
    
    for row in todo:
        if find in row:
            print(f"Found the list with the name{find}")
            time.sleep(1)
            os.system("cls")
            print("The list has been removed!")
            time.sleep(1)
            todo.remove(row)
    time.sleep(0.5)
    os.system("cls")   


while True: #menu and menu acsses
    menu = input("1) Add\n2) View\n3) Edit\n4) Remove\n")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    else:
        remove()
    time.sleep(1)
    os.system("cls")


