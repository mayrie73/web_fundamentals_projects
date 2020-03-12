# This program prints all the odd numbers from 1 to 1000 

for x in xrange(1, 1000):
 if x % 2!=0:
    print x 


# This program prints the sum of all the values a list

# List of numbers
a = [1, 2, 5, 10, 255, 3] 

# variable to store the sum
sum=0 

# iterate over the list 
for val in a: 
 sum =sum+val

 # Output: The sum is 276
print ('The sum is', sum)

#This program prints the average of the values in a list.

# List of numbers
a = [1, 2, 5, 10, 255, 3] 

# variable to store the sum
sum=0 

# iterate over the list 
for val in a: 
 sum =sum+val

 # Output: Average =sum/number of list items
print ('The average is', sum/len(a))

