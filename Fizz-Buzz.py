N = int(input("Enter an integer "))
i = 1
while i in range (1, N+1):
    if i % 3 == 0 and i % 7 != 0:
      print(f"Fizz {i}")
    elif i % 7 == 0 and i % 3 != 0:
      print(f"Buzz {i}")
    elif i % 7 == 0 and i % 3 == 0:
      print(f"FizzBuzz {i}")
    elif i % 7 != 0 and i % 3 != 0:
      print(i)
    i += 1
