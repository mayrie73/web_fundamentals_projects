# Find and Replace
words="It's thanksgiving day. It's my birthday too!"
print(words.find("day"))
print "Index for day:", words.index("day")
words=words.replace("day", "month", 1)
print words

#Min and Max
x = [2,54,-2,7,12,98]
print min(x),
print max(x)

# Print First and Last 
x = ["hello",2,54,-2,7,12,98,"world"]

print x[0],
print x[-1],

#New List 
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
newList = x[0:len(x)/2]
del x[0:len(x)/2]
x.insert(0,newList)
print x




