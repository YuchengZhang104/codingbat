def end_other(a, b):
  newa = a.lower()
  newb = b.lower()
  return newa[-(len(newb)):] == newb or newa == newb[-(len(newa)):] 