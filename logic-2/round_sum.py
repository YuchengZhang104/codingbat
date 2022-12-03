def round_sum(a, b, c):
  return round_(a) + round_(b) + round_(c)
 
def round_(n):
  if n % 10 >= 5:
    return n + 10 - (n % 10)
  return n - (n % 10)  