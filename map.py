# the purpose of this function is to cube the elements inside the list
# list --> list
def cube_all(list):
    newlist = []
    for i in list:
        newlist.append(i**3)
    return newlist

# the purpose  of this list is to add the number input to the elements inside the list
# list, int --> list

def add_n_to_all(list,number):
    add = []
    i = 0
    while i<len(list):
          add.append(list[i]+number)
          i +=1
    return add

# the purpose of this list is to check if the elements inside the list are divisible by 5
# list --> boolean

def div_by_5_all(list):
    return [x%5 == 0 for x in list]
