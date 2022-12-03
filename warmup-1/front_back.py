def front_back(str):
  mid = str[1:-1]
  first = str[0]
  last = str[-1]
  newstr = last+mid+first
  return newstr

print(front_back("chocolate"))