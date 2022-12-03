def not_string(str):
  if str[:3] == "not":
    str = str
  else:
    str = "not " + str
  return str