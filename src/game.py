from src.dealer import Dealer
from src.player import Player

class Game:

    def __init__(self):
        '''
            Set the players and agents of the game.
        '''
        self.player1 = Player(1)
        player2 = Player(2)
        self.players = [self.player1, player2]
        self.dealer = Dealer()

    def start_game(self):
        self.dealer.deal_card(self.players)

        self.winner = False

        while not self.winner:
            for player in self.players:
                self.play_turn(player)

    def play_turn(self, player:Player):

        print("\n Player Change!!!!!!!!!!!!!!!")
        print("Your Current Hand:")
        player.print_current_hand()
        print("    ------     ")
        print("Your Choice Cards:")
        print(self.dealer.choice_card)
        print("    ------     ")
        print("What do you want to play?")
        valid_plays =  player.valid_plays()
        for index, valid in enumerate(valid_plays,1):
            print(index,": ", valid)
        num = int(input("Enter the number: "))
        #TODO Check fi the num is valid
        throw = valid_plays[num-1]

        for card in throw:
            player.hand.remove(card)

        print("\n")
        print("Pick from Choice Cards of Deck?")
        print("1: Deck")
        for index, card in enumerate(self.dealer.choice_card, 2):
            print(index, ": ", card)

        choice_pick = int(input("Enter the number: "))
        print("\n")
        if choice_pick == 1:
            player.hand.append(self.dealer.current_deck.pop())
        else:
            #TODO check choice
            player.hand.append(self.dealer.choice_card.pop(choice_pick-2))
        player.print_current_hand()

        # Clear out the choice card as we are ending this players turn
        self.dealer.clear_choice_card()

        # Add new set of choice card for next player
        self.dealer.choice_card = throw
