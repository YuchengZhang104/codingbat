def close_far(a, b, c):
    if (abs(a-b) >= 2 and abs(b-c) >= 2):
      return True
    elif (abs(a-b) >= 2 and abs(a-c) >= 2):
      return True
    elif (abs(b-c) >= 2 and abs(a-c) >= 2):
        return True
    else:
        return False
