def no_teen_sum(a, b, c):
  return check(a) + check(b) + check(c)
 
def check(n):
  if n in [13, 14, 17, 18, 19]:
    return 0
  return n