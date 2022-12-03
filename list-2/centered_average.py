def centered_average(nums):
    res = 0
    length = len(nums)
    total = length-2
    largest = nums.index(max(nums))     
    smallest = nums.index(min(nums))    
    if largest == smallest:             
        for i in range(length):      
            if nums[i] == nums[smallest]:
                largest = i             
    for i in range(length):
        if i != largest and i != smallest:      
            res = res + nums[i] 
    if total > 0:
        return res / total         
    else:
        return res  