# the purpose of this list is to return the list that only contains even numbers
# list --> list
def are_even(list):
    newlist = [x for x in list if x%2 == 0]
    return newlist

# the purpose of this list is to return the list of the elements inside without the duplicate
# list --> list

def remove_duplicates(list):
    newlist = []
    x = 0
    while x < len(list):
        if list[x] not in newlist:
           newlist.append(list[x])
        x+=1
    return newlist

# purpose is to return the elemetn in the list if its divisible by the number input
# list , int --> list
def are_divisible_by_n(list,number):
    divis = []
    for x in list:
        if x % number == 0:
           divis.append(x)
        x +=1
    return divis
