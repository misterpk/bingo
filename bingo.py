'''Look into using a counter to keep track of the position, then write the
number if it equals it

http://usingpython.com/python-programming-challenges/

Fix code so it doesn't error when you're out of values
fix code so the loop works properly. it should process the next guess
'''

import random


def generate_numbers():
    possible_numbers = [i for i in range(1, 101)]
    random.shuffle(possible_numbers)
    numbers = possible_numbers[:10]
    numbers.sort()
    return numbers


def draw_board(numbers):
    board = ''
    counter = 1
    print('Bingo!\nHere\'s your board:\n')
    pos = 0
    while counter < 100:
        # print(pos)
        # print(counter)
        # print(numbers[i])
        # print(numbers[i] % 10)
        # if counter == numbers[i] and numbers[i] % 10 == 0:
        #     board = board + '{:3d}\n\n'.format(numbers[i])
        #     # found = True
        if counter == numbers[pos]:
            board = board + '{:3d} '.format(numbers[pos])
            if pos < len(numbers) - 1:
                pos = pos + 1
        else:
            board = board + '___ '

        if counter % 9 == 0:
            board = board + '\n\n'

        counter = counter + 1
    print(board)


if __name__ == "__main__":
    values = generate_numbers()
    print(values)

    draw_board(values)

    while len(values) != 0:
        user_input = input('Enter the called number \'q\' to quit: ')
        if user_input.lower() == 'q':
            exit(1)
        if values.count(int(user_input)) == 1:
            values.remove(int(user_input))
            draw_board(values)
        else:
            user_input = input('Number not on board. Enter the called number'
                               ' \'q\' to quit: ')

    print("BINGO!")
