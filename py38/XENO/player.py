import random

class Player:
    # hands = [] statis val
    def __init__(self,name,card):
        self.name = name
        self.hands = []
        self.hands.append(card)
        self.is_effect = True
        self.is_turn = False
        self.is_choice_drow = False

    def add_hands(self,card):
        self.hands.append(card)

    def discard_card(self,card):
        self.hands.remove(card)

    def random_discard_card(self, hand_index):
        card = self.hands[hand_index]
        self.hands.pop(hand_index)
        return card

    def choice_card(self):
        print('hands:{0}'.format(self.hands))
        if 10 in self.hands:
            hand_idx_hero = self.hands.index(10)
            if hand_idx_hero == 0:
                return self.hands[1]
            else:
                return self.hands[0]

        count = 0
        while count < 10:
            count = count + 1
            choice = int(input('input hands: '))
            if self.check_input(self.hands,choice):
                print('choice card:{0}'.format(choice))
                if choice == 10:
                    print('Hero cards cannot be put into play')
                else:
                    self.hands.remove(choice)
                    print('hands:{0}'.format(self.hands))
                    break
            else:
                print('miss input hands')

        if count >=  10:
            hand_idx = random.randrange(len(self.hands))
            choice = self.hands[hand_idx]

        return choice

    def drow_deck_and_add_hands(self, deck):
        if(self.is_choice_drow):
            self.choice_card_1_from_3(deck)
        else:
            new_hands = deck[-1]
            deck.pop()
            self.add_hands(new_hands)

    def choice_card_1_from_3(self, deck):
        candidate_cards = []
        for i in range(3):
            top_deck = deck[-1]
            deck.pop()
            candidate_cards.append(top_deck)

        print('candidate cards: {0}'.format(candidate_cards))
        count = 0
        while count < 10:
            count = count + 1
            choice = int(input('input candidate cards num: '))
            if self.check_input(candidate_cards, choice):
                print('choice card:{0}'.format(choice))
                break
            else:
                print('miss input candidate cards')

        if count >=  10:
            hand_idx = random.randrange(len(candidate_cards))
            choice = candidate_cards[hand_idx]

        self.add_hands(choice)
        candidate_cards.remove(choice)
        for candidate_card in candidate_cards:
            deck.append(candidate_card)
        random.shuffle(deck)

    def show_hands(self):
        print('hands:{0}'.format(self.hands))

    def show_name(self):
        print('player name:{0}'.format(self.name))

    def get_name(self):
        return self.name

    def get_hands(self):
        return self.hands

    def set_is_choice_drow(self, flag):
        self.is_choice_drow = flag

    def set_isturn(self, flag):
        self.is_turn = flag

    def get_isturn(self):
        return self.is_turn

    def set_is_effect(self, flag):
        self.is_effect = flag

    def reincarnation_init(self, deck):
        self.hands.clear()
        new_card = deck[-1]
        self.add_hands(new_card)

    def check_input(self, candidate, input):
        return input in candidate
