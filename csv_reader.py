with open("prac.csv","r") as read_csv:
    file=read_csv.readlines()
    # print(file)

desired_col=3
col_val=[]

for i in file[1:]:
    row=i.strip().split(",")
    # print(row)
    value=float(row[desired_col])
    # print(value)
    col_val.append(value)
    # print(col_val)

total=0
no_of_elements=len(col_val)
for i in col_val:
    total=total+i

average=total/no_of_elements
print(f"the average of math is:{average}")