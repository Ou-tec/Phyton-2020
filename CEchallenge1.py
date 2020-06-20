import math
list = [0.3, 0.51, 0.6, 1]
def time(angles, mass, lenght):
    Degrees_list = []
    sinus_list = []
    for elements in angles:
        Degrees_list.append(elements*180/3.14)
    return Degrees_list
    for element in Degrees_list:
        sinus_list.append(math.sin(element))
    return sinus_list
    for element in sinus_list:
        t_square = 2*lenght/(mass*9.81*element)
    t = math.sqrt(t_square)
    return t
print(time(list, 30, 4)) 