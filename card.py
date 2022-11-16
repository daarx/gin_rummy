from enum import Enum

class CardValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    @staticmethod
    def fromValue(value):
        for enum in list(CardValue):
            if enum.value == value:
                return enum

    def __str__(self):
        match self:
            case CardValue.ACE:
                return 'A'
            case CardValue.TWO:
                return '2'
            case CardValue.THREE:
                return '3'
            case CardValue.FOUR:
                return '4'
            case CardValue.FIVE:
                return '5'
            case CardValue.SIX:
                return '6'
            case CardValue.SEVEN:
                return '7'
            case CardValue.EIGHT:
                return '8'
            case CardValue.NINE:
                return '9'
            case CardValue.TEN:
                return '10'
            case CardValue.JACK:
                return 'J'
            case CardValue.QUEEN:
                return 'Q'
            case CardValue.KING:
                return 'K'


class CardSuit(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4

    @staticmethod
    def fromValue(value):
        for enum in list(CardSuit):
            if enum.value == value:
                return enum

    def __str__(self):
        match self:
            case CardSuit.CLUB:
                return '♣'
            case CardSuit.DIAMOND:
                return '♦'
            case CardSuit.HEART:
                return '♥'
            case CardSuit.SPADE:
                return '♠'

class Card:
    def __init__(self, value: CardValue, suit: CardSuit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value}{self.suit}'