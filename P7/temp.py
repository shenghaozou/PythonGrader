def calculate_food(user_type, gets_discount):
  cost = raw_input("Food cost: $")
  cost = float(cost)
  if user_type == "S":
    if gets_discount == True:
      cost = cost*.90
    else:
      cost = cost*.95
  else:
    if gets_discount == True:
      cost = cost*.80
    else:
      cost = cost*.95
  print cost


def calculate_other():
  cost = raw_input("Non-food cost: $")
  cost = float(cost)
  print cost*1.055

def calculate_total():
  user_type = raw_input("(S)tudent or (F)aculty")
  if user_type != "F" and user_type != "S":
    print "Invalid input, S or F only."
    quit()
  elif user_type == "S":
    dorm = raw_input("Dorm resident? (Y/N)")
    if dorm == "Y":
      x = True
    elif dorm == "N":
      x = False
    else:
      print "Invalid input, Y or N only"
      exit()
  else:
    meal_plan = raw_input("Meal Plan? (Y/N)")
    if meal_plan == "Y":
      y = True
    elif meal_plan == "N":
      x = False
    else:
      print "Invalid input, Y or N only"
      exit()
  return calculate_food(user_type,x)

