from card import Card, CardValue, CardSuit
import random

class Game:
    def __init__(self):
        self.deck = []
        self.discard_pile = []
        self.player_1_hand = []
        self.player_2_hand = []

    def render_game(self):
        print(f'# of cards in Deck: {len(self.deck)}')
        print(f'Top of Discard Pile: {self.discard_pile[len(self.discard_pile)-1]}')
        print(f'Player 1 Hand: ', end='')
        print(*self.player_1_hand)
        print(f'Player 2 Hand: ', end='')
        print(*self.player_2_hand)

    def handle_player_1_input(self):
        pass

    def handle_player_2_input(self):
        pass

    def initialize_game(self):
        temp_deck = []

        # Initialize temp deck
        for value in range(13):
            for suit in range(4):
                temp_deck.append(Card(CardValue.fromValue(value+1), CardSuit.fromValue(suit+1)))

        # 'Shuffle' deck by picking cards randomly from the temp deck
        for i in range(52):
            self.deck.append(temp_deck.pop(random.randrange(52-i)))

        print('Deck pre picking:')
        print(*self.deck)

        # Put the first card of the deck on top of the discard pile
        self.discard_pile.append(self.deck.pop())

        # Hand 10 cards to each player
        for _ in range(10):
            self.player_2_hand.append(self.deck.pop())
            self.player_1_hand.append(self.deck.pop())

        print('Deck post picking:')
        print(*self.deck)

    def main_loop(self):
        game_running = True


        while game_running:
            self.render_game()
            self.handle_player_2_input()
            self.render_game()
            self.handle_player_1_input()
            game_running = False

    def start(self):
        self.initialize_game()
        self.main_loop()
