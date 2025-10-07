def twoSum(nums, target):
    hash_map = {}
    for i, v in enumerate(nums):
        diff = target - v
        if diff in hash_map:
            return [v, hash_map[diff]]
        hash_map[v] = i
