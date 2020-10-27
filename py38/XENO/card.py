import sys

class Card():
    def __init__(self, num):
        self.num = num

    def show_num(self):
        print('num={0}'.format(self.num))

    def show_effect(self):
        pass

    def exe_effect(self,plater_list):
        pass

    def drow_card(self, player, deck):
        p_new_hands = deck[-1]
        player.add_hands(p_new_hands)
        deck.pop()

    def show_enmy_name(self, player_list):
        print('show enemy name')
        for idx, player in enumerate(player_list):
            print('{0}: {1}'.format(idx,player.get_name()))

    def choice_enemy(self, player_list):
        print('choice player')
        player_index = int(input('input player index: '))
        return player_index

    def reincarnation(self, player_list, enemy_player_index, cemetery, used_card):
        if used_card == 9:
            player_list.pop(enemy_player_index)
        else:
            player_list[enemy_player_index].reincarnation_init(deck)


class Hero(Card):
    pass

class Emperor(Card):
    def show_effect(self):
        print('effect name: Public execution')
        print('Have the nominated opponent draw one card from the deck and reveal both cards in their hand. And specify one of them and let it be thrown away')

    def exe_effect(self,player_list, deck, cemetery):
        self.show_enmy_name(player_list)
        player_index = self.choice_enemy(player_list)
        self.drow_card(player_list[player_index], deck)
        # player_list[player_index].show_hands()
        self.discard_hand_choice(player_list[player_index], cemetery)

    def discard_hand_choice(self, player, cemetery):
        player.show_hands()
        card = int(input('input player hands card: '))
        player.discard_card(card)
        cemetery.append(card)

class Spirit(Card):
    def show_effect(self):
        print('effect name: Exchange')
        print('Exchange the hand of the nominated opponent with the hand you have')

    def exe_effect(self, player, player_list):
        self.show_enmy_name(player_list)
        player_index = self.choice_enemy(player_list)
        self.exchange_hands(player, player_list[player_index])

    def exchange_hands(self, player, enemy_player):
        player_hands = player.get_hands()
        player_card = player_hands[0]
        player.discard_card(player_card)
        enemy_player_hands = enemy_player.get_hands()
        enemy_player_card = enemy_player_hands[0]
        enemy_player.discard_card(enemy_player_card)
        player.add_hands(enemy_player_card)
        enemy_player.add_hands(player_card)

class Sage(Card):
    def show_effect(self):
        print('effect name: Choice')
        print('In the next turn, instead of drawing one from the deck, you can draw three and choose one of them. Return the remaining 2 cards to the deck')

    def exe_effect(self, player):
        player.set_is_choice_drow()


class Noble(Card):
    def show_effect(self):
        print('effect name: Showdown')
        print('The first one only shows the hand with the nominated opponent. The second card shows the hand with the nominated opponent, and the one with the smaller number drops out.')

    def exe_effect(self, cemetery, player_list, player_index, enemy_player_index):
        # is_drop = False
        # drop_player = 0
        if 6 in cemetery :
            player_hands = player_list[player_index].get_hands()
            player_card = player_hands[0]
            enemy_player_hands = player_list[enemy_player_index].get_hands()
            enemy_player_card = enemy_player_hands[0]
            if player_card > enemy_player_card:
                player_list.pop(enemy_player_index)
            elif player_card < enemy_player_card:
                plater_list.pop(player_index)
            else:
                pass
        else:
            player_list[player_index].show_hands()
            player_list[enemy_player_index].show_hands()

        return drop_player

class GrimReaper(Card):
    def show_effect(self):
        print('effect name: Plague')
        print('Have the nominated opponent draw one from the deck. Keep the opponent\'s hand that has become two cards private, and specify one card to discard.')

    def exe_effect(self, player_list, deck, cemetery):
        self.show_enmy_name(player_list)
        player_index = self.choice_enemy(player_list)
        self.drow_card(player_list[player_index], deck)
        self.random_discard_hand(player_list[player_index], cemetery)

    def random_discard_hand(self, player, cemetery):
        player_hands = player.get_hands()
        player.show_hands() #dewbug
        idx_list = []
        for i, x in enumerate(player_hands):
            idx_list.append(i)
        print('idx_list: {0}'.format(idx_list))
        hand_index = int(input('input player hands index: '))
        card = player.random_discard_card(hand_index)
        cemetery.append(card)
