#First Comparison
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

if str(list_one) == str(list_two):
    print("the lists are the same")
else:
    print("the lists are not the same")

# Second Comparison
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
if str(list_one) == str(list_two):
    print("the lists are the same")
else:
    print("the lists are not the same")

#Third Comparison
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
if str(list_one) == str(list_two):
    print("the lists are the same")
else:
    print("the lists are not the same")

#Final Comparison
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
if str(list_one) == str(list_two):
    print("the lists are the same")
else:
    print("the lists are not the same")
