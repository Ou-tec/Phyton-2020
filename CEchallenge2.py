import math
l =[0.3, 0.4, 0.6, 0.9]
def distance(velocity, angles, acceleration):
    Degrees_list = []
    sinus_list = []
    for elements in angles:
        Degrees_list.append(elements*180/3.14)
    return Degrees_list
    for elements in Degrees_list:
        sinus_list.append(math.sin(2*elements))
    return sinus_list
    for elements in sinus_list:
        R = velocity*elements/acceleration
    return R
print(distance(2.5, l, 9))
        