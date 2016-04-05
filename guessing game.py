user=raw_input("whats your name? ")
number=input('whats the biggest number you want to  guess?')
guess=input("pick a number!")
from random import randint
random=(randint(1,number))
answer= random
while guess != random:
     if guess > random:
        print "too high"
        guess=input("pick a number!")
     else:
        print 'too low'
        guess=input("pick a number!")

print"great you got it!!"
