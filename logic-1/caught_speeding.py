def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed<= 60:
      return 0
    elif 61<=speed<=80:
      return 1
    elif 81<=speed:
      return 2
    else:
      if speed<=65:
        return 0
  elif is_birthday:
    if speed > 65 and speed <= 85:
        return 1
    elif speed > 85:
      return 2
    return 0