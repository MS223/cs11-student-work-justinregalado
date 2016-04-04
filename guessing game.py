user=raw_input("whats your name? ")
guess=input('whats the biggest number you want to  guess?')
number=input("pick a number!")
from random import randint
random=(randint(1,number))
answer=
while guess != number:
    if guess < number:
        print "too high"
    elif guess > number:
        print 'too low'
        #i must check what i will be putting in for answer
