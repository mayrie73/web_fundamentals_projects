# Program creates a function called odd_even that counts from 1 to 2000
def odd_even():
    for i in range(1, 2001):
        if (i % 2 ==1):
            print("The number is: " + str(i)+ "." + " This is an odd number.")
        elif (i % 2 == 0):
            print("The number is: " + str(i) + "." + " This is an even number.")
odd_even()

# Program creates a function called 'multiply' that iterates through each value in a list 
# (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
multiply(a,b)

'''def layered_multiples(arr):
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
#>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]'''

