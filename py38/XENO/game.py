import random
import player
import card

def shuffle(deck):
    random.shuffle(deck)
def show_cemetery(cemetery):
    print('cemetery: {0}'.format(cemetery))

deck = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10]
print(deck)
shuffle(deck)
print(deck)

cemetery = []

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
# hero card test @pass
# hero = card.Hero(10)
# hero.show_num()
# emperor card test @pass
# emperor = card.Emperor(9)
# emperor.exe_effect(player_list, deck, cemetery)
# player_list[1].show_hands()
# spirit card test @pass
# spirit = card.Spirit(8)
# spirit.exe_effect(player_list[0], player_list)
# player_list[0].show_hands()
# player_list[1].show_hands()
# sage card test code @pass
# sage = card.Sage(7)
# sage.exe_effect(player_list[0])
# player_list[0].drow_deck_and_add_hands(deck)
# player_list[0].show_hands()







