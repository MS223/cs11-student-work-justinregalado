list= [3,4,7,13,54,32,653,256,1,41,65,83,92,31]
def find_odds(input):
    for x in list:
        if x % 2 == 1:
            print (x)
find_odds(list)

def odd_sum(input):
    odd_list=[]
    for x in list:
        if x % 2 == 1:
            odd_list.append(x)
    print sum(odd_list)

odd_sum(list)

list= [3,4,7,13,54,32,653,256,1,41,65,83,92,31]
def find_even(input):
    even_list=[]
    for x in input:
        if x % 2 == 0:
            even_list.append(x)
    print sum(even_list)
find_even(list)

import random
my_randoms = random.sample(range(100), 15)
list= [3,4,7,13,54,32,653,256,1,41,65,83,92,31]
def find_even(input):
    even_list=[]
    for x in input:
        if x % 2 == 0:
            even_list.append(x)
    print sum(even_list)
find_even(my_randoms)
