subtotal = 0
Total = 0
Taxes = 0
while True:
  y = int(input("Select your order "))
  if y == 1:
    print("You have ordered a McWhopper")
    subtotal += 6.89
  elif y == 2:
    print("You have ordered a Crispy McFish")
    subtotal += 4.99
  elif y == 3:
    print("You have ordered Fries")
    v = int(input("Choose a size "))
    if v == 1:
      print("You've ordered a small box of fries")
      subtotal += 0.99
    elif v == 2:
      print("You've ordered a medium box of fries")
      subtotal += 1.99
    elif v == 3:
      print("You've ordered a large box of fries")
      subtotal += 2.99
  elif y == 4:
      print("You've ordered Soda")
      v = int(input("Select a size "))
      if v == 1:
        print("You've chosen a small cane of soda")
        subtotal += 0.50
      elif v == 2:
        print("You've chosen a medium cane of soda")
        subtotal += 1.50
      elif v == 3:
        print("You've chosen a large cane of soda")
        subtotal += 2.00
  elif y == 5:
      print("You've ordered an happy meal")
      subtotal += 6.99
  elif y == 6:
      print("You've ordered a Family Deal")
      subtotal += 19.99
  elif y == 7:
      break
      print("Thank you for shopping with us")
      subtotal += 0
  else:
      print("Invalid option -- Please choose again")
  Taxes = subtotal * 0.08875
  Total = subtotal + Taxes
  print(f"Your subtotal is {subtotal}")
  print(f"Tax is {Taxes}")
  print(f"Your total is {Total}")
  y += 1
  


