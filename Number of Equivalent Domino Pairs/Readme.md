# 🧩 Number of Equivalent Domino Pairs

🔗 [LeetCode Problem Link](https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-07)

## ❓ Problem Statement

Given a list of dominoes, where each domino is represented as a list of two integers, return the number of pairs `(i, j)` such that:

- `0 <= i < j < dominoes.length`, and  
- `dominoes[i]` is equivalent to `dominoes[j]`

Two dominoes `[a, b]` and `[c, d]` are considered equivalent if:

- `(a == c and b == d)` or `(a == d and b == c)`  
(i.e., one can be rotated to match the other)

---
### 📌 Example 1:

## 🧠 Explanation (Simplified)

- To ignore the order of domino numbers, we **normalize** each domino (e.g., `[2,1]` becomes `[1,2]`)
- We keep a counter to track how many times each normalized domino appears
- Every time a duplicate is found, it contributes to the total number of pairs
- We use the formula for combinations:  
  `If a domino appears k times => total pairs = k * (k - 1) / 2`  
  But we update the count on the go using a Counter.

---

## ✅ Constraints

- `1 <= dominoes.length <= 4 * 10^4`
- `dominoes[i].length == 2`
- `1 <= dominoes[i][j] <= 9`

---
