def array_front9(nums):
  four = nums[0:4]
  count = 0
  for i in four:
    if i == 9:
      count += 1
  if count > 0:
    return True
  else:
    return False