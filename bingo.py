"""Look into using a counter to keep track of the position, then write
the number if it equals it

http://usingpython.com/python-programming-challenges/

Look into making the number length a variable and have it auto-format
field size
"""

import random

BOARD_SIZE = 100
MIN_VALUE = 1
MAX_VALUE = BOARD_SIZE + 1
USED_VALUES = 10
COLUMNS = 10


def generate_numbers():
    """
    Generate USED_VALUES number of values between MIN_VALUE and
    MAX_VALUE.
    :return: list of USED_VALUES number of values
    """
    # generate a list with numbers MIN_VALUE through MAX_VALUE
    possible_numbers = [i for i in range(MIN_VALUE, MAX_VALUE)]

    # shuffle the numbers in the list so USED_VALUES can be selected
    random.shuffle(possible_numbers)
    numbers = possible_numbers[:USED_VALUES]

    # sort numbers to make drawing the board easier
    numbers.sort()

    return numbers


def draw_board(numbers):
    """
    Draw the board of numbers received from generate_numbers()
    :param numbers: received from generate_numbers()
    """
    board = ""
    counter = 1
    pos = 0

    while counter < BOARD_SIZE:
        if counter == numbers[pos]:
            board = board + '{:3d} '.format(numbers[pos])
            if pos < len(numbers) - 1:
                pos = pos + 1
        else:
            board = board + '___ '

        if counter % (COLUMNS - 1) == 0:
            board = board + '\n\n'

        counter = counter + 1
    print(board)


def get_input():
    """
    Get user input
    :return: user input
    """
    user_input = input("Enter the number called or type Q to Quit: ")
    if user_input.upper() == "Q":
        exit(1)
    return int(user_input)


def process_value(values_list, value):
    """
    Check if number is present on board, remove if it is and return
    True. Otherwise return false.
    :param values_list: list of values from generate_values()
    :param value: user input from get_input()
    :return: True if value is present and removed. False if value not
    present
    """
    if values_list.count(value) == 1:
            values_list.remove(value)
            return True
    return False


if __name__ == "__main__":
    """
    Generate a board with a set number of values. Game is over when
    user either quits or all values are removed from board.
    """
    values = generate_numbers()
    print(values)

    print('Bingo!\nHere\'s your board:\n')

    while True:
        if len(values) > 0:
            draw_board(values)
            if process_value(values, get_input()) is True:
                continue
            else:
                print("Number not on board")
                continue
        else:
            print("Bingo!")
            break
