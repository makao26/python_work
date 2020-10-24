class Player:
    # hands = [] statis val
    def __init__(self,name,card):
        self.name = name
        self.hands = []
        self.hands.append(card)
        self.is_effect = True
        self.is_turn = False
    
    def drow_card(self,card):
        self.hands.append(card)
    
    def discard_card(self,card):
        self.hands.remove(card)
    
    def choice_card(self):
        print('hands:{0}'.format(self.hands))
        choice = int(input('input hands: '))
        print('choice card:{0}'.format(choice))
        self.hands.remove(choice)
        print('hands:{0}'.format(self.hands))
        return choice
    
    def show_hands(self):
        print('hands:{0}'.format(self.hands))

    def show_name(self):
        print('player name:{0}'.format(self.name))

    def get_name(self):
        return self.name
