# 🔒LeetCode #1134 — Armstrong Number

- **Difficulty:** Easy
- **Language:** Python
- **Status:** ✅ Solved Locally
- **Submission:** Not submitted — Premium problem

## Approach

1. Store the original number in `copy2`.
2. Use `copy` to count the number of digits.
3. Extract each digit using `% 10`.
4. Raise each digit to the power of the number of digits.
5. Add the results to `total`.
6. Remove the last digit using `// 10`.
7. Compare `total` with the original number stored in `copy2`.
8. If both are equal, the number is an Armstrong number.

## Complexity

- **Time:** O(log₁₀ n)
- **Space:** O(1)

## Status

✅ Solved and tested locally.

> This is a LeetCode Premium problem, so the solution was not submitted on LeetCode.