i = int(input("Enter a year "))
if i in range (1700, 2701):
    if i % 4 != 0:
        print(f"In {i}, the day of the programmer was or will be observed on the 256th day")
    elif i % 400 != 0 and i % 4 != 0:
        print(f"The day of the programmer was or will be observed on the 256th day of {i}")
    elif i % 100 == 0:
        print(f"The day of the programmer was or will be observed on the 265th day of {i}")
    elif i == 1918:
        print("This year, the day of the programmer is 09.26")
    elif i % 4 == 0 and i % 100 != 0:
        print("This year, the day of the programmer is 09.12")
    elif i % 400 == 0:
        print("This year, the day of the programmer is 09.12")
elif i < 1700:
    print("Invalid year. Pick another year in the range 1700 - 2700")
elif i > 2700:
    print("Invalid year. Pick another year in the range 1700 - 2700")
    
else:
    print("This year, the day of the programmer is 09.13")