def make_chocolate(small, big, goal):
  if big*5>goal:
    need = goal%5
  else:
    need = goal-big*5
  if small<need:
    return -1
  else:
    return need
