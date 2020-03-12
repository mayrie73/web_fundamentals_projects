import random 
def coinToss():
	head_count = 0
	tail_count = 0
	toss_count = 0
	for toss in range(5001): 
		toss = round(random.random())
		if toss == 0:
			head_count += 1
			toss_count += 1
			print "Attempt #", toss_count , ": Throwing a coin... It's a head! ... Got " , head_count , "head(s) so far and " , tail_count , "tail(s) so far"
		elif toss==1: 
			tail_count += 1
			toss_count += 1
			print "Attempt #", toss_count , ": Throwing a coin... It's a tail! ... Got " , head_count , "head(s) so far and " , tail_count , "tail(s) so far"

coinToss()
