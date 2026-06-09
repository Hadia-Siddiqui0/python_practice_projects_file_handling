from datetime import datetime

with open("expense.csv","w") as tracker:
    expense_track=tracker.write("Date,category,amount\n")

while True:
    question=int(input("1. add data:\n"
                       "2. check total\n"
                       "3. read file\n"
                       "4.exit the programe\n"))
    if(question==1):
        date=datetime.now()
        category=input("enter the item category name: ")
        amount=int(input("enter the amount: "))
        row=f"{date},{category},{amount}\n"
        with open("expense.csv","a") as inserting:
            insert_values=inserting.write(row)
        
        print(f"ALHAMDULILAH! {date} , {category}, {amount} added succefully")
    elif(question==2):
        with open("expense.csv","r") as total:
            read_lines=total.readlines()

        desired_row_name=input("enter the name of column you want the total: ")
        desired_list=[]
        if(desired_row_name=="date" or desired_row_name=="category"):
            print("no strings total allowed")
        elif(desired_row_name=="amount"):
            desired_row=2
            for i in read_lines[1:]:
                row=i.strip().split(",")
                value=float(row[desired_row])
                desired_list.append(value)

            print(desired_list)
            total=0
            for i in desired_list:
                total=total+i

            print(total)
        else:
            print("please write the correct name")
    elif(question==3):
        with open("expense.csv","r") as readit:
            print(readit.read())  
    elif(question==4):
        print("ALHAMDULILAH! ALLAH HAFIZ")
        break
    else:
        print("please choose from above options")