import driver

def letter(row, col):
    if (0 <= row <= 19) and (0 <= col <= 9):
        return 'D'
    else: 
        return 'P'

if __name__ == '__main__':
   driver.comparePatterns(letter)
