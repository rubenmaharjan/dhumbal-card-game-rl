from itertools import combinations, chain
from src.cards import Card

class Player:

    def __init__(self, player_id:int):
        self.player_id: int = player_id
        self.hand:list[Card] = []
        self.score = 100

    def get_player_id(self) -> int:
        '''
            Return Player's id
        '''
        return self.player_id

    def print_current_hand(self):
        '''
            Print the players current hand
        '''
        for card in self.hand:
            print(card.suit, " ", card.value)

    # TODO Implement the function
    def valid_plays(self):
        '''
            Return the players valid moves
        '''
        return

    # TODO Implement the function
    def finish_game(self):
        '''
            Finish the game by showing your hand
            Need to validate the hand. 
            total needs to be less than 6
        '''
        return


    def get_sequence(self):

        def is_sequence_consecutive(sequence: list[tuple[Card]]):
            return all(a.value == (b.value - 1) for a, b in zip(sequence[:-1], sequence[1:]))

        def card_combination_of_size(n:int):
            return list(combinations(self.hand,n))

        possible_sequence = []
        for i in range(3, len(self.hand)):
            seq = card_combination_of_size(i) # Get the combination of cards in hand

            # Filter out the card combinations that has different suite
            seq = [group for group in seq if len(set(item.suit for item in group)) == 1]
            for s in seq:
                if is_sequence_consecutive(s):
                    possible_sequence.append(s)
        return possible_sequence
