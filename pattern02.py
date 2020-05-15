import driver

def letter(row, col):
    if (0 <= row <= 9) and (0 <= col <= 19):
       if ( 5 <= row <= 7) and ( 5 <= col <= 10):
          return 'M'
       else: 
          return 'N'

    elif (10 <= row <= 19) and (0 <= col <= 19):
       if (12 <= row <= 14) and ( 5 <= col <= 10):
          return 'M'
       else:
          return 'Z'


if __name__==  '__main__':
   driver.comparePatterns(letter)

       
