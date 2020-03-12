#Program that takes a list and prints a message for each element in the list, based on that element's data type.
list= ['magical unicorns',19,'hello',98.98,'world']
sum=0
string=("String: ")
for val in list:
    if isinstance(val, str):
        string +=val + " "
    elif isinstance(val, int) or isinstance(val, float):
        sum+=val
    if int != 0 and str !=0:
       print("The list you entered is of mixed type")
       print("Sum:" + str(sum))
       print(string)
     

        