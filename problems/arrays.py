from typing import List

"""
    - Zawsze jak jest missing number albo cos takiego warto uzyc set()
"""


def containsDuplicate_217(nums):
    """
    PROBLEM:
        Check list for duplicates

        Input: nums = [1,2,3,1]

        Output: true
    SOLUTION:
        Time and Space: O(N): Iterate through list and create set, Space = size of set

    NOTES:
        Sets are fast, Note that set cannot be created through {}, it creates dictionary
    unless you include values

        Set is implemented as a hash table, so you can lookup/insert/delete in O(1) average
    """
    if len(set(nums)) == len(nums):
        return False
    else:
        return True


def missingNumber_268(nums: List[int]) -> int:
    """
    PROBLEM:
        Check list for one missing number in range [0,n]

        Input: nums = [3,0,1]

        Output: 2
    SOLUTION:
        O(N): Iterate through list and sum (twice: once for given list and once for
    expected using range)

    NOTES:
        len(nums) = O(1)
        range(len(nums)+1) = O(1)
        sum(range(len(nums)+1)) = O(N)

        +1 in range because range is excluding last element so sum of range(0,3)
        would be 3, not 6

    BEST APPROACH:
        n = len(nums)
        expected_sum = n *  (n + 1) // 2
        return expected_sum - sum(nums)
    """
    return sum(range(len(nums) + 1)) - sum(nums)


def findDisappearedNumbers_448(nums):
    """
    PROBLEM:
        Check given list for missing numbers range(1, len(nums))

        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [5,6]
    SOLUTION:
       Time: O(N): Iterate through range and append to new list if not in
    given list. O(N) space.

    NOTES:

    """
    set_nums = set(nums)
    missing = []
    for i in range(1, len(nums) + 1):
        if i not in set_nums:
            missing.append(i)
    return missing


def twoSum_1(nums, target):
    """
    PROBLEM:
        Return the indices of two numbers in list that add up to a given target.

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
    SOLUTION:
        O(N) Time by using set for lookup, otherwise would be O(N2) with a list

    NOTES:
        Look to reduce repeated code for cleanliness and readability
    """
    hashMap = {}

    for i, v in enumerate(nums):
        diff = target - v
        if diff in hashMap:
            return [i, hashMap[diff]]
        hashMap[v] = i


def smallerNumbersThanCurrent(nums):
    """
    PROBLEM:
        Return new list, where for each num[i] in original list, the value in new list is the total of numbers num[i] is bigger than.

        Input: nums = [8,1,2,2,3]
        Output: [4,0,1,1,3]
    SOLUTION:
        Instead of iterating twice O(n2)time O(N)space. Sort the list to temp list, dict the value for each num (not identical) in
        temp list, where index of first new number also represents previous numbers bigger than: O(nlogn)time –sorting & O(n)space dict.

    NOTES:
        Time complexity > Space complexity (space is cheap)
    """
    temp = sorted(nums)
    hashMap = {}
    ret = []

    for i, v in enumerate(temp):
        if v not in hashMap:
            hashMap[v] = i

    for i in nums:
        ret.append(hashMap[i])

    return ret


def minTimeToVisitAllPoints(points):
    """
    PROBLEM:
        From a list of points, calculate the min distance between first and last point (x1, y1)
    SOLUTION:
        If the next node is +10x and -5y away, it's going to take exactly 10 steps,
        because you can only move 1 x at a time and the difference in y is
        made up by diagonal moves during the process of overcoming the difference in x. Time: O(N), Space: O(1)

    NOTES:
        Coding shouldn’t be the difficult part e.g: If you understand one or two things,
        rest of problem is easy: distance between two
        points is maximum difference of one coord

    """
    res = 0
    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        res += max(abs(y2 - y1), abs(x2 - x1))
        x1, y1 = x2, y2
    return res


def spiralOrder(matrix):
    ret = []

    while matrix:
        # dodaj wszystkie elementy z pierwszej listy do ret
        ret += matrix.pop(0)
        print(f"matrix po pierwszym stepie: {matrix}")

        # dodaj ostatnie elementy z pozostalych list do ret jezeli istnieje
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        print(f"matrix po drugim stepie: {matrix}")

        # dodaj ostatnia liste w rewersie
        if matrix:
            ret += matrix.pop()[::-1]
        print(f"matrix po trzecim stepie: {matrix}")

        # append first element of all rows in reverse
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
        print(f"matrix po czwartym stepie: {matrix}")

    return ret


# matrix = [[4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))
