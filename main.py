import sys
from game import Game


def process_arguments(args):
    Game().start()

if __name__ == '__main__':
    process_arguments(sys.argv)
