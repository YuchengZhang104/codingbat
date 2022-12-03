def has22(nums):
    length = len(nums)
    for i in range (length-1):
        if (nums[i] == 2) and (nums[i+1] == 2):
            return True        
    return False
