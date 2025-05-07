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
