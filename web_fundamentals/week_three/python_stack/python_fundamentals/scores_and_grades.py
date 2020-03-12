def scores_grades():  
    from random import randint  
    for num in range (10):  
        num=randint(60,100)
        if num>=90 and num<=100:
            print('Score: '+str(num)+'.' ' Your grade is an A.')
        elif  num>=80 and num<89:
            print('Score: '+str(num)+'.' ' Your grade is a B.')
        elif  num>=70 and num<79:
            print('Score: '+str(num)+'.' ' Your grade is a C.')
        elif  num>=60 and num<69:
            print('Score: '+str(num)+'.' ' Your grade is a D.')    
scores_grades()
print("End of the program. Bye!")