
def func(N):
    list = []
    for i in range(1, 100):
        if i % N == 0:
            list.append(i)
    return list
print(func(6))
