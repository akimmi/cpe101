import driver

def letter(row, col):
    if (0 <= row <= 6) and (0 <= col <= 9):
       if (row == 0) or (row ==6):
          return 'W'
       elif (row == 1) or (row == 5):
          return 'S'
       elif (2 <= row <= 4): 
          if (3 <= col <= 6):
              return 'W'
          else:
              return 'S'

if __name__ == '__main__':
   driver.comparePatterns(letter)
