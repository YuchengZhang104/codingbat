def make_bricks(small, big, goal):
  rest = goal%5
  if small>=rest and (small*1+big*5) >= goal:
    return True
  else:
    return False
