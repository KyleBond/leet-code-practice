
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    if (len(nums) == 2):
        return [0,1]
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]

    # newNums = [nums.index(x) for x in nums if x < target]

    

    return []