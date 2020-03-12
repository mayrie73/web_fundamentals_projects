# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list=[]
for val in word_list:
    if char in val:
        new_list.append(val)
        print(new_list)

