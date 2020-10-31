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
player_list , deck = player_init(4,deck)
print('deck:{0}'.format(deck))

def player_order_decision(player_list):
    player_num = len(player_list)
    print('player num: {0}'.format(player_num))
    start_player_idx = random.randint(0,player_num-1)
    print('start player idx :{0}'.format(start_player_idx))
    player_list[start_player_idx].set_isturn(True)
    for i in range(start_player_idx-1):
        player_temp = player_list[0]
        player_list.pop(0)
        player_list.append(player_temp)
    for player in player_list:
        player.show_name()

def get_enemy_player(player_list):
    enemy_player_list = []
    for player in player_list:
        if !player.get_isturn() :
            enemy_player_list.append(player)

# turn test code
def turn_start(player,deck):
    player.set_isturn(True)
    player.drow_deck_and_add_hands(deck)

def turn_main():
    pass

def turn_end(player):
    player.set_isturn(True)

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
# noble card test @pass
# noble = card.Noble(6)
# result = noble.exe_effect(cemetery, player_list[0],player_list[1])
# print(result)
# cemetery.append(6)
# result = noble.exe_effect(cemetery, player_list[0],player_list[1])
# print(result)
# grim reaper card test @pass
# grimreaper = card.GrimReaper(5)
# grimreaper.exe_effect(player_list, deck, cemetery)
# player_list[1].show_hands()
# show_cemetery(cemetery)
