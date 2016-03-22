for groot in range(1,101):
    if groot % 3 == 0: #checking for multiples of 3
        print('fizz')
    elif groot % 5 == 0: # checking for multiples of 5
        print('buzz')
    elif groot % 3 == 0 and groot % 5 == 0: #checking for multiples of 3 AND 5
        print('fizzbuzz')
    else:
        print groot

# Why isn't the code finding the multiples of 3 AND 5? What is it checking for first?
