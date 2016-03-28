for groot in range(1,101):
    if groot % 3 == 0 and groot % 5 == 0:#looking for multiples of 3 and 5
        print('fizzbuzz')
    elif groot % 3 == 0:#looking for multibles of 3
        print('fizz')
    elif groot % 5 == 0:#looking for muiltibles of 5
        print('buzz')
    else:
        print groot
