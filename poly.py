import math
# the purpose of this function is add the values inside the list
# list, list --> list
def poly_add2(p1, p2):
    a= p1[0] + p2[0]
    b= p1[1] + p2[1]
    c= p1[2] + p2[2]
    return [a, b, c]

# the purpose of this function is to multiply the values inside the list (like a polynomial) by using the distributive method
# list, list --> list

def poly_mult2(p1,p2):
    a = p1[0] * p2[0]
    b = (p1[0] * p2[1]) + (p1[1] * p2[0])
    c = (p1[0] * p2[2]) + (p1[1] * p2[1]) + (p1[2] * p2[0])
    d = (p1[1] * p2[2]) + (p1[2] * p2[1])
    e = p1[2] * p2[2]

    return [a,b,c,d,e]
