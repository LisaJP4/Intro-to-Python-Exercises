def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count

print(string_match("Mississippi", "LucazadeSport"))

def date_fashion(you, date):
  yes = 2
  maybe = 1
  no = 0
  if you >= 8 or date >= 2:
    return yes
  elif you <= 2 or date <= 2:
    return no
  else:
    return maybe

print(date_fashion(7, 2))


def squirrel_play(temp, is_summer):
  if temp in range(60, 100) and is_summer == True:
    return True
  elif is_summer == False and temp in range(60, 90):
    return True
  else:
    return False


print(squirrel_play(90, False))