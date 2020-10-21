import random
import player
import card

def shuffle(deck):
    random.shuffle(deck)

deck = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10]
print(deck)
shuffle(deck)
print(deck)

# # init testcode
# # pass
# p1_nm = input('input player 1 name:')
# # print(p1_nm)
# new_hands_p1 = deck[-1]
# p1 = player.Player(p1_nm, new_hands_p1)
# p1.show_name()
# p1.show_hands()
# deck.pop()
# p2_nm = input('input player 2 name:')
# # print(p2_nm)
# new_hands_p2 = deck[-1]
# p2 = player.Player(p2_nm, new_hands_p2)
# p2.show_name()
# p2.show_hands()
# deck.pop()
# print(deck)

# # player choice test code 
# # pass
# p1.show_name()
# choice_card = p1.choice_card()

#player_list test code
# init pass
def player_init(play_num,deck):
    player_list = []
    for i in range(play_num):
        p_nm = input('input player name:')
        p_new_hands = deck[-1]
        p = player.Player(p_nm, p_new_hands)
        p.show_name()
        p.show_hands()
        deck.pop()
        player_list.append(p)
    return player_list, deck
player_list , deck = player_init(2,deck)
print('deck:{0}'.format(deck))
# get enemy player list test code


# card test code
hero = card.Hero(10)
hero.show_num() #pass






