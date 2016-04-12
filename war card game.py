player_name1=raw_input("player 1 your name ?")
player_name2=raw_input("player 2 your name?")
import random
def shuffled_deck():
	basic_deck = range(2, 15) * 4
	random.shuffle(basic_deck)
	return basic_deck
deck_of_cards=shuffled_deck()

def player_turn(player_name):
    card=deck_of_cards.pop()
    print player_name, 'drew card',(card)
    return (card)

while len(deck_of_cards)>0:
    a=player_turn(player_name1)
    b=player_turn(player_name2)
    if a>b:
        print " player 1 you won"

    elif a<b:
            print "player 2 you won"
