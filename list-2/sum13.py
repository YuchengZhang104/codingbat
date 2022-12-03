def sum13(nums):    
    res = 0
    length = len(nums)
    for i in range (length):
        if nums[i] != 13:
            res += nums[i]
        elif nums[i] == 13 and i < length-1:
            nums[i]=0;
            nums[i+1] =0
    return res   