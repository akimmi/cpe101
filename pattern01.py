import driver
# the purpose of this function is to match the puzzle with the code
# int, int --> string
def letter(row,col):
    if (0 <= row <= 19):
        if (row % 2 == 0):
            if (0 <= col <= 2):
                return 'L'
            else:
                return 'G'

        elif (row % 2 == 1):
            if (row == 9) and (col == 9):
                return 'Z'

            elif (17 <= col <= 19):
                return 'O'
            else:
                return 'G'

if __name__ == '__main__':
   driver.comparePatterns(letter)

