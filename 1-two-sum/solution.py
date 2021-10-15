
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    if (len(nums) == 2):
        return [0,1]
    
    for x in nums:
        for y in nums:
            if (x + y == target):
                return [nums.index(x), nums.index(y)]

    # newNums = [nums.index(x) for x in nums if x < target]

    

    return []