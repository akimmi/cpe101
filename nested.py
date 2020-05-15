# so i have a 2D list and the purpose of this is to multiply the elements inside the 2Dlist and return the product in a new list
# list --> list
def product(list):
    newlist = []
    for i in list:
        product = 1
        for j in i:
            product *= j
        newlist.append(product)
    return newlist
