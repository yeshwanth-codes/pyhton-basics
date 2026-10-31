    
task=["empty"]


def to_do():
    while True :
        
        print("_____Menu____")
        print("1.Add new task")
        print("2.Remove task")
        print("3.display list")
        user=int(input("Enter ur choice : "))
              
        if user == 1:    
          while True :
                
                useradd=input("Enter task to add (done to quit):").lower().strip()
                
                print(f"{useradd} added to the list ")
                if useradd =="done":
                        break
                else:
                        
                        task.append(useradd)
                            
                #remove task
        elif user ==2:
            userdel=input("Enter task name to remove from the list :")
            if userdel in task:
                            task.remove(userdel)
                            print(f"{userdel} removed from the list ")
                            print(f"Afet removing {userdel}from the list",task)
                            
                    
            else:
             print(f"{userdel} does not exist in the list ")
        elif user ==3:
                        
                        print(task)
                
        else:
                    print("invalid choice ") 
                


to_do()


    
    

    