list = [9, 2, 3]
list2 = [1, 2, 3]
def func(a_list):
    another_list = []
    for i in range(1, len(a_list)):
        if a_list[0] < a_list[1]:
            another_list.append(a_list[0])
            a_list.pop(0)
            if len(another_list) == len(a_list)-1:
                return("The list is in ascending order")
            else:
                return("The list is not in ascending order")
        else:
            return("The list is not in ascending order")
print(func(list))
print(func(list2))
