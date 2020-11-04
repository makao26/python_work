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
        if player.get_isturn() == False :
            enemy_player_list.append(player)
    return enemy_player_list

# turn test code
def turn_start(player,deck):
    print('turn start Phase')
    player.set_isturn(True)
    player.drow_deck_and_add_hands(deck)

def turn_main(player_list, deck, cemetery, player_list_idx):
    print('turn main Phase')
    card_num = player_list[player_list_idx].choice_card()
    use_card(card_num, player_list, deck, cemetery, player_list_idx)


def turn_end(player):
    print('turn end Phase')
    player.set_isturn(True)

def use_card(card_num, plater_list, deck, cemetery, player_list_idx):
    if card_num == 1:
        enemy_player_list = get_enemy_player(player_list)
        boy = card.Boy(1)
        boy.exe_effect(enemy_player_list, deck, cemetery)
    elif card_num == 2:
        enemy_player_list = get_enemy_player(player_list)
        soldier = card.Soldier(2)
        soldier.exe_effect(enemy_player_list, player_list)
    elif card_num == 3:
        enemy_player_list = get_enemy_player(player_list)
        diviner = card.Diviner(3)
        diviner.exe_effect(enemy_player_list)
    elif card_num == 4:
        maiden = card.Maiden(4)
        maiden.exe_effect(player_list[player_list_idx])
    elif card_num == 5:
        enemy_player_list = get_enemy_player(player_list)
        grimreaper = card.GrimReaper(5)
        grimreaper.exe_effect(enemy_player_list, deck, cemetery)
    elif card_num == 6:
        enemy_player_list = get_enemy_player(player_list)
        noble = card.Noble(6)
        noble.exe_effect(cemetery, enemy_player_list)
    elif card_num == 7:
        sage = card.Sage(7)
        sage.exe_effect(player_list[player_list_idx])
    elif card_num == 8:
        enemy_player_list = get_enemy_player(player_list)
        spirit = card.Spirit(8)
        spirit.exe_effect(player_list[player_list_idx], enemy_player_list)
    elif card_num == 9:
        enemy_player_list = get_enemy_player(player_list)
        emperor = card.Emperor(9)
        emperor.exe_effect(enemy_player_list, deck, cemetery)


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
# soldier card test @pass
# player_list[0].set_isturn(True)
# enemy_player_list = get_enemy_player(player_list)
# soldier = card.Soldier(2)
# soldier.exe_effect(enemy_player_list, player_list)
# boy card test code
# cemetery.append(1)
# player_list[0].set_isturn(True)
# enemy_player_list = get_enemy_player(player_list)
# boy = card.Boy(1)
# boy.exe_effect(enemy_player_list, deck, cemetery)
# player_list[1].show_hands()
# Reincarnation test code @pass
# test_deck = [1,1,2,2,3,3,4,4,5,5,6,7,6,7,8,8,10,9]
# player_list , deck = player_init(4,test_deck)
# print('deck:{0}'.format(test_deck))
# cemetery.append(1)
# player_list[0].set_isturn(True)
# enemy_player_list = get_enemy_player(player_list)
# boy = card.Boy(1)
# boy.exe_effect(enemy_player_list, test_deck, cemetery)
# player_list[1].show_hands()


while(len(player_list) > 1):
    for idx, player in enumerate(player_list):
        turn_start(player, deck)
        turn_main(player_list, deck, cemetery, idx)
        turn_end(player)
