def sum67(nums):                
    res = 0
    length = len(nums)
    i=0  
    while i < length:
        if nums[i] == 6:
            while nums[i] != 7:
                i+=1
            i+=1
        if i<length and nums[i]!=6:  
                res += nums[i]
                i+=1
    return res   
     