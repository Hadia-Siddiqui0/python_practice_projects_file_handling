import os

while True:
    user_choice=int(input("1.you want to add task:\n"
                          "2.you want to read task:\n"
                          "3.exit the programe:\n"))
    
    if(user_choice==1):
        user_filename=input("enter the file name in which you want to save our task: ")
        user_task=input("enter the task: ")
        with open(user_filename,"w") as user_file:
            user_file.write(user_task)
    elif(user_choice==2):
        user_read=input("enter the file name in which you want to read: ")
        if (os.path.exists(user_read)):
            with open(user_read,"r") as read_file:
                print(read_file.read())
        else:
            print("there is no such file")
    elif(user_choice==3):
        print("ALLAH HAFIZ")
        break
    else:
        print("please choose from the given options")