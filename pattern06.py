import driver

def letter(row, col):
   if (row == 0 or row == 8 or col == 0 or col == 8):
      return 'C'
   elif (1 <= row <= 7) and (1 <= col <= 7):
      if (row==col) or (row+col==8):
          return 'E'
      else:
          return 'O'
   

if __name__ == '__main__':
   driver.comparePatterns(letter)

