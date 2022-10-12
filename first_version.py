for i in range(1,101):
    if i % 5==0 and i % 3 ==0:
        print('fizzbuzz')
        continue
    elif i % 5 ==0:
        print('Buzz')
        continue
    elif i % 3 == 0:
        print('fizz')
        continue
    else:
        print(i)
        
    
