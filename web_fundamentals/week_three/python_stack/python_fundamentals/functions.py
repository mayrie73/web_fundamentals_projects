# we've named the function 'add' and we give it two parameters(inputs to the function)
'''def add(a,b):
  x = a + b
  return x  # we return something (more on this later)
print add(3,5)'''

'''# Example 2
# this function has one parameter(input)
def say_hi(name):
  print "Hi, " + name
# invoking the function passing in one argument
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')'''

'''#Example 3
def say_hi():
  return "Hi"
greeting = say_hi() #the returned value from say_hi function gets assigned to the 'greeting' variable
print greeting # this will output 'Hi'''
def add(a, b):
  x = a + b
  return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

print(sum1)
print(sum2)
print(sum3)
