#purpose: to return a string with just the vowels
# string --> string 
def vowel_extractor(str):
    new_str = "" 
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for element in str:
        if element in vowels:
           new_str += element
    return new_str


#purpose: takes 3 inputs and returns a string where the old characer is replaced by the new character in the string input
# str, str, str --> str
# works

def str_translate(str, old, new):
    new_str = ""

    for element in str:
        if element == old:
           new_str += new
        else:
           new_str += element
    return new_str

# check if these 2 are right
#purpose is to rotate 13 characters back or front
# string --> string

def rot_13(s):
    new_s = ""
    for char in s:
        if (ord('A') <= ord(char)) and (ord(char) <= ord('Z')): 
            if (ord('A') <= ord(char)) and (ord(char) <= ord('M')):
                ask = ord(char) + 13
                new_s += chr(ask)
            else:
                ask = ord(char) - 13
                new_s += chr(ask)
        elif (ord('a') <= ord(char)) and (ord(char) <= ord('m')):
            if (ord('a') <= ord(char)) and (ord(char) <= ord('m')):
                ask = ord(char) + 13
                new_s += chr(ask)
            else:
                ask = ord(char) - 13
                new_s += chr(ask)
        else:
            new_s += char
    return new_s

# range functions
# the purpose of this function is to return a substring that begins from start index and ends at stop index
# str, int, int, int --> str

def make_substring(string, start, stop, step):
    new_string = ""

    for i in range(start, stop, step):
        new_string += string[i]
    
    return new_string 

# the purpose of this function is to return true if the string input is a palindrome and false if not
# string --> boolean

def is_palindrome(string):
    string = string.lower()
    for i in range(0, len(string)):
        if string[i] == string[len(string)-1-i]:
           return True
        else:
           return False
 
# the purpose of this function is to count characters by checking if the character is in the string
# string, string --> int
def count_characters(string, character):

    count = 0

    for i in range(len(string)):
        if character.isalpha():
           if string[i] == character.upper() or string[i] == character.lower():
               count += 1
        else:
           if character == string[i]:
               count += 1      
     
    if count == 0:
       count = -1
     
    return count 

