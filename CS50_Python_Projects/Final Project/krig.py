import random

# Define the card suits, ranks, and values
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# ASCII art for cards
card_art = {
    '2': ' 2', '3': ' 3', '4': ' 4', '5': ' 5', '6': ' 6', '7': ' 7', '8': ' 8', '9': ' 9', '10': '10',
    'J': ' J', 'Q': ' Q', 'K': ' K', 'A': ' A'
}

def draw_card_art(card):
    art = f"""
     _____
    |{card_art[card.rank]}   |
    |     |
    |  {card.suit[0]}  |
    |     |
    |___{card_art[card.rank]}|
    """
    return art

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Deck class
class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# Simple card game
def simple_card_game():
    print("Welcome to the simple card game!")

    deck = Deck()
    player_card = deck.deal_one()
    computer_card = deck.deal_one()

    print("\nYour card:")
    print(draw_card_art(player_card))
    print(player_card)

    print("\nComputer's card:")
    print(draw_card_art(computer_card))
    print(computer_card)

    if player_card.value > computer_card.value:
        print("\nYou win!")
    elif player_card.value < computer_card.value:
        print("\nComputer wins!")
    else:
        print("\nIt's a tie!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        simple_card_game()
    else:
        print("Thanks for playing!")

# Start the game
simple_card_game()
