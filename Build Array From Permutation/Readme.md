# 🔗 Problem: Build Array from Permutation
[Link to the Problem](https://leetcode.com/problems/build-array-from-permutation/description/?envType=daily-question&envId=2025-05-07)

## 📝 Problem Statement
Given a 0-indexed integer array `nums` of length `n`, build an array `ans` where:

- `ans[i] = nums[nums[i]]` for every `0 <= i < n`, and return it.

## ✅ Python Solution
```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
# 📌 Explanation:
# - We use list comprehension to construct a new list.
# - For each index i:
#     - nums[i] gives the index we need to access next.
#     - nums[nums[i]] fetches the final value.
# - This approach runs in O(n) time and uses O(n) extra space.
