guesses=1
user=raw_input("whats your name? ")#askes you whats your name
number=input('whats the biggest number you want to  guess?')#to get the outline of the number
guess=input("pick a number!")# picking the first numbre
from random import randint
random=(randint(1,number))
answer= random
while guess != random:# that the guess is not enqual to random
     if guess > random:
        print "too high"# if they guess too high
        guess=input("pick a number!")#they get to pick another number
        guesses=guesses+1#the guess if tghey get too high is adding one
     else:
        print 'too low'# it will print too low if the number is too low 
        guess=input("pick a number!")#they get anotther try at picking a numbre
        guesses=guesses+1# if they geuess too low it will
print"great you got it!!"
print "it took you " +str (guesses)+ " tries"
