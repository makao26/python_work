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

    def show_enmy_name(self, player_list):
        print('show enemy name')
        for idx, player in enumerate(player_list):
            print('{0}: {1}'.format(idx,player.get_name()))

    def choice_enemy(self,player_list):
        print('choice player')
        player_index = int(input('input player index: '))
        return player_index

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
    
    
    def drow_card(self, player, deck):
        p_new_hands = deck[-1]
        player.drow_card(p_new_hands)
        deck.pop()
    
    def discard_hand_choice(self, player, cemetery):
        player.show_hands()
        card = int(input('input player hands card: '))
        player.discard_card(card)
        cemetery.append(card)

class Spirit(Card):
    def show_effect(self):
        print('effect name: Exchange')
        print('Exchange the hand of the nominated opponent with the hand you have')
    
    def exe_effect(self):

    

    
    

    









