list = []
for i in range(0, 13):
    list.append(i)
def Odd_list(first_list):
    a_list = []
    for i in range(0, len(first_list)):
        if i % 2 != 0:
            a_list.append(i)
    return a_list
print(Odd_list(list))
