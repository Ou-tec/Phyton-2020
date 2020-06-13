x = int(input("Choose the conversion type "))
y = 0
if x == 1:
  print("You are converting from Fahrenheit to Celsius")
  x = int(input("How many Fahrenheit would you like to convert? "))
  y = (x - 32) * 0.56
  print(f"{x} Fahrenheit is {y} Celsius")
elif x == 2:
  print("You are converting from Fahrenheit to Kelvin")
  x = int(input("How many Fahrenheit would you like to convert? "))
  y = (x-32) * 0.56
  y += 273.15
  print(f"{x} Fahrenheit is {y} Kelvin")