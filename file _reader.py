# create file by 'x'
# file_name=open("my_first_file.txt","x")

# write in the file
# with open("my_first_file.txt","w") as file_name:
#     file_name.write("ASSALAM O ALAIKUM! my name is Hadia and i am currently making python projects.\n"
#                      "I am doing this because i want to be an AI/ML engenieer in the future.\n"
#                      "So i am currently studying this to be a data-scientist then pursue my career with some experience.\n"
#                     "IN'SHA'ALLAH")
    
# read the file
# with open("my_first_file.txt","r") as file_name:
#     print(file_name.read())
# file_name=open("my_first_file.txt","r")

with open("my_first_file.txt", "r") as file_name:
    content = file_name.read()  

#  for counting characters

char=0
for i in content:
    # print(i)
    char_len=len(i)
    char=char+char_len

print(f"total characters: {char}")

# for counting lines

lines=content.count("\n") + 1
# for i in content:
#     if char == "\n":
#         lines=lines+1
# lines +=1
print(f"total lines are: {lines}")

#  for counting words

word_count = 0
inside_word = False

for char in content:
    if char != " " and char != "\n" and char != "\t":
        if not inside_word:
            word_count += 1
            inside_word = True
    else:
        inside_word = False

print(f"Total words: {word_count}")

file_name.close()