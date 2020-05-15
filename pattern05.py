import driver

# B changes when row = col, 
def letter(row, col):
    if (row > col):
        return 'B'
    else: 
        return 'U'

if __name__ == '__main__':
   driver.comparePatterns(letter)
