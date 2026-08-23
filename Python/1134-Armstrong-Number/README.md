# 🔒LeetCode #1134 — Armstrong Number

* **Difficulty:** Easy
* **Language:** Python
* **Status:** ✅ Solved Locally
* **Submission:** Not submitted — Premium problem

## Approach

1. Store the original number in `copy`.
2. Count the number of digits using `len(str(n))`.
3. Extract each digit using `% 10`.
4. Raise each digit to the power of the number of digits.
5. Add the results to `total`.
6. Compare `total` with the original number.
7. If they are equal, the number is an Armstrong number.

## Complexity

* **Time:** O(d), where `d` is the number of digits
* **Space:** O(d) due to converting the number to a string

## Status

✅ Solved and tested locally.

> This is a LeetCode Premium problem, so the solution was not submitted on LeetCode.
