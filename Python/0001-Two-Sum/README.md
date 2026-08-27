# LeetCode #1 — Two Sum

* **Difficulty:** Easy
* **Language:** Python
* **Runtime:** 0 ms
* **Memory:** 13.26 MB
* **Runtime Beats:** 100.00%
* **Memory Beats:** 36.55%

## Approach

1. Find the length of the array using `len(nums)`.
2. Create an empty hash map `hash_map` to store numbers and their indices.
3. Iterate through the array using `i`.
4. Calculate the required value using `remains = target - nums[i]`.
5. Check if `remains` is already present in the hash map.
6. If it is present, return its stored index and the current index.
7. Otherwise, store the current number and its index in the hash map.
8. Continue until the required pair is found.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

## Status

✅ Accepted
