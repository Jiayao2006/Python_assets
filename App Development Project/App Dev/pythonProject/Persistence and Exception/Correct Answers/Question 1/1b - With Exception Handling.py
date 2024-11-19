"""
In this question, the possible exceptions are:
- ValueError (user may enter not a number)
- ZeroDivisionError (possible divide by 0 - sum(numList)/len(numList))
- as there might be other exceptions so you handle using except
"""
try:
    count = int(input('How many number you want to capture?'))
    numList = []
    for i in range(count):
        msg = 'Enter number #' + str(i+1)
        num = int(input(msg))
        numList.append(num)

    print('The lowest number in the list:', min(numList))
    print('The highest number in the list:', max(numList))
    print('The total of the number in the list:', sum(numList))
    print('The average of the number in the list:', sum(numList)/len(numList))
except ValueError:
    print('Invalid integer')
except ZeroDivisionError:
    print('Zero Division Error')
except: 
    print('An unknown error occurred')
