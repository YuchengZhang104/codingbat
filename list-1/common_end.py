def common_end(a, b):
    lengthA = len(a)
    lengthB = len(b)
    if a[0] == b[0] or a[lengthA-1] == b[lengthB-1]:
        return True
    return False