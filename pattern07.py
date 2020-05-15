import driver

def letter(row, col):
   if (0 <= row <= 9) and (0 <= col <= 19):
        if (row == 2 or row ==3) and ( 4 <= col <= 9):
            return 'Y'
        elif (row == 4 or row == 5) and ( 4 <= col <= 12):
            if (4 <= col <= 6):
              return 'Y'
            elif (7 <= col <= 9):
              return 'X'
            elif (10 <= col <= 12):
              return 'B'
        elif (row == 6) and (7 <= col <= 12):
            return 'B'
        else:
            return 'K' 

   elif (row == 10):
        return 'B'


if __name__ == '__main__':
   driver.comparePatterns(letter)
