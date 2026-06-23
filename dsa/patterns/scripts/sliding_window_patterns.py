from typing import List, Dict, Optional
from collections import defaultdict, Counter

class SlidingWindow:
    """Complete sliding window patterns collection"""

    @staticmethod
    def max_sum_subarray_of_size_k(arr: List[int], k: int) -> int:
        """
        Problem 1: Maximum Sum Subarray of Size K
        Time: O(n), Space: O(1)
        """
        if not arr or k > len(arr):
            return -1

        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]
            max_sum = max(max_sum, window_sum)

        return max_sum

    @staticmethod
    def smallest_subarray_with_sum_given(arr: List[int], target: int) -> int:
        """
        Problem 2: Smallest Subarray with Sum >= Target
        Time: O(n), Space: O(1)
        """
        window_start = 0
        window_sum = 0
        min_length = float('inf')

        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            while window_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1

        return min_length if min_length != float('inf') else 0

    @staticmethod
    def longest_substring_with_k_distinct(s: str, k: int) -> int:
        """
        Problem 3: Longest Substring with K Distinct Characters
        Time: O(n), Space: O(k)
        """
        if k == 0 or not s:
            return 0

        window_start = 0
        char_freq = {}
        max_length = 0

        for window_end in range(len(s)):
            right_char = s[window_end]
            char_freq[right_char] = char_freq.get(right_char, 0) + 1

            while len(char_freq) > k:
                left_char = s[window_start]
                char_freq[left_char] -= 1
                if char_freq[left_char] == 0:
                    del char_freq[left_char]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

    @staticmethod
    def longest_substring_without_repeating(s: str) -> int:
        """
        Problem 4: Longest Substring Without Repeating Characters
        Time: O(n), Space: O(min(n, alphabet))
        """
        window_start = 0
        char_index = {}
        max_length = 0

        for window_end in range(len(s)):
            if s[window_end] in char_index and char_index[s[window_end]] >= window_start:
                window_start = char_index[s[window_end]] + 1

            char_index[s[window_end]] = window_end
            max_length = max(max_length, window_end - window_start + 1)

        return max_length

    @staticmethod
    def character_replacement(s: str, k: int) -> int:
        """
        Problem 5: Longest Repeating Character Replacement
        Time: O(n), Space: O(26)
        """
        window_start = 0
        char_freq = {}
        max_count = 0
        max_length = 0

        for window_end in range(len(s)):
            char_freq[s[window_end]] = char_freq.get(s[window_end], 0) + 1
            max_count = max(max_count, char_freq[s[window_end]])

            while (window_end - window_start + 1) - max_count > k:
                char_freq[s[window_start]] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

    @staticmethod
    def max_consecutive_ones(nums: List[int], k: int) -> int:
        """
        Problem 6: Max Consecutive Ones After Flipping K Zeros
        Time: O(n), Space: O(1)
        """
        window_start = 0
        max_ones = 0
        zeros_count = 0

        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                zeros_count += 1

            while zeros_count > k:
                if nums[window_start] == 0:
                    zeros_count -= 1
                window_start += 1

            max_ones = max(max_ones, window_end - window_start + 1)

        return max_ones

    @staticmethod
    def find_anagrams(s: str, p: str) -> List[int]:
        """
        Problem 7: Find All Anagrams in a String
        Time: O(n), Space: O(1)
        """
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        s_count = [0] * 26
        result = []

        for char in p:
            p_count[ord(char) - ord('a')] += 1

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            if s_count == p_count:
                result.append(i - len(p) + 1)

        return result

    @staticmethod
    def max_vowels_in_substring(s: str, k: int) -> int:
        """
        Problem 8: Maximum Number of Vowels in a Substring of Length K
        Time: O(n), Space: O(1)
        """
        vowels = set('aeiou')
        window_start = 0
        max_vowels = 0
        current_vowels = 0

        for window_end in range(len(s)):
            if s[window_end] in vowels:
                current_vowels += 1

            if window_end - window_start + 1 > k:
                if s[window_start] in vowels:
                    current_vowels -= 1
                window_start += 1

            if window_end - window_start + 1 == k:
                max_vowels = max(max_vowels, current_vowels)

        return max_vowels

    @staticmethod
    def subarray_product_less_than_k(nums: List[int], k: int) -> int:
        """
        Problem 9: Subarray Product Less Than K
        Time: O(n), Space: O(1)
        """
        if k <= 1:
            return 0

        count = 0
        product = 1
        window_start = 0

        for window_end in range(len(nums)):
            product *= nums[window_end]

            while product >= k and window_start <= window_end:
                product //= nums[window_start]
                window_start += 1

            count += window_end - window_start + 1

        return count

    @staticmethod
    def longest_subarray_with_ones_after_deleting(nums: List[int]) -> int:
        """
        Problem 10: Longest Subarray of 1's After Deleting One Element
        Time: O(n), Space: O(1)
        """
        window_start = 0
        zeros_count = 0
        max_length = 0

        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                zeros_count += 1

            while zeros_count > 1:
                if nums[window_start] == 0:
                    zeros_count -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length - 1 if max_length > 0 else 0

    @staticmethod
    def min_window_substring(s: str, t: str) -> str:
        """
        Problem 11: Minimum Window Substring
        Time: O(n), Space: O(m) where m = len(t)
        """
        if not s or not t:
            return ""

        required = Counter(t)
        formed = 0
        window_counts = defaultdict(int)

        left = 0
        min_len = float('inf')
        min_left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1

            if char in required and window_counts[char] == required[char]:
                formed += 1

            while formed == len(required):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in required and window_counts[left_char] < required[left_char]:
                    formed -= 1
                left += 1

        return s[min_left:min_left + min_len] if min_len != float('inf') else ""

    @staticmethod
    def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
        """
        Problem 12: Contains Duplicate II (within K distance)
        Time: O(n), Space: O(min(n, k))
        """
        window = set()

        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - k - 1])

            if nums[i] in window:
                return True

            window.add(nums[i])

        return False

    @staticmethod
    def max_sum_subarray_size_k_sliding(arr: List[int], k: int) -> List[int]:
        """
        Problem 13: Return the subarray with maximum sum of size K
        Time: O(n), Space: O(k)
        """
        if not arr or k > len(arr):
            return []

        window_sum = sum(arr[:k])
        max_sum = window_sum
        max_start_index = 0

        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]
            if window_sum > max_sum:
                max_sum = window_sum
                max_start_index = i - k + 1

        return arr[max_start_index:max_start_index + k]

    @staticmethod
    def longest_turbulent_subarray(arr: List[int]) -> int:
        """
        Problem 14: Longest Turbulent Subarray
        Time: O(n), Space: O(1)
        """
        if len(arr) <= 1:
            return len(arr)

        max_len = 1
        window_start = 0

        for window_end in range(1, len(arr)):
            compare = (arr[window_end - 1] - arr[window_end])

            if compare == 0:
                window_start = window_end
            elif window_end == len(arr) - 1 or (arr[window_end] - arr[window_end + 1]) * compare >= 0:
                max_len = max(max_len, window_end - window_start + 1)
                window_start = window_end

        return max_len


# Function-based interface for easy calling
def sliding_window_examples():
    """Demonstrate all sliding window functions with examples"""

    sw = SlidingWindow()

    print("=" * 80)
    print("SLIDING WINDOW PATTERN - COMPLETE EXAMPLES")
    print("=" * 80)

    # Example 1: Maximum Sum Subarray of Size K
    print("\n1. Maximum Sum Subarray of Size K")
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    result1 = sw.max_sum_subarray_of_size_k(arr1, k1)
    print(f"   Array: {arr1}, K={k1}")
    print(f"   Result: {result1}")

    # Example 2: Smallest Subarray with Sum >= Target
    print("\n2. Smallest Subarray with Sum >= Target")
    arr2 = [2, 1, 5, 2, 3, 2]
    target2 = 7
    result2 = sw.smallest_subarray_with_sum_given(arr2, target2)
    print(f"   Array: {arr2}, Target={target2}")
    print(f"   Result: {result2}")

    # Example 3: Longest Substring with K Distinct Characters
    print("\n3. Longest Substring with K Distinct Characters")
    s3 = "araaci"
    k3 = 2
    result3 = sw.longest_substring_with_k_distinct(s3, k3)
    print(f"   String: '{s3}', K={k3}")
    print(f"   Result: {result3}")

    # Example 4: Longest Substring Without Repeating Characters
    print("\n4. Longest Substring Without Repeating Characters")
    s4 = "abcabcbb"
    result4 = sw.longest_substring_without_repeating(s4)
    print(f"   String: '{s4}'")
    print(f"   Result: {result4}")

    # Example 5: Character Replacement
    print("\n5. Longest Repeating Character Replacement")
    s5 = "AABABBA"
    k5 = 1
    result5 = sw.character_replacement(s5, k5)
    print(f"   String: '{s5}', K={k5}")
    print(f"   Result: {result5}")

    # Example 6: Max Consecutive Ones
    print("\n6. Max Consecutive Ones After Flipping K Zeros")
    nums6 = [1, 1, 0, 1, 1, 0, 1, 1, 1]
    k6 = 2
    result6 = sw.max_consecutive_ones(nums6, k6)
    print(f"   Array: {nums6}, K={k6}")
    print(f"   Result: {result6}")

    # Example 7: Find All Anagrams
    print("\n7. Find All Anagrams in a String")
    s7 = "cbaebabacd"
    p7 = "abc"
    result7 = sw.find_anagrams(s7, p7)
    print(f"   String: '{s7}', Pattern: '{p7}'")
    print(f"   Result: {result7}")

    # Example 8: Maximum Vowels in Substring
    print("\n8. Maximum Vowels in Substring of Length K")
    s8 = "abciiidef"
    k8 = 3
    result8 = sw.max_vowels_in_substring(s8, k8)
    print(f"   String: '{s8}', K={k8}")
    print(f"   Result: {result8}")

    # Example 9: Subarray Product Less Than K
    print("\n9. Subarray Product Less Than K")
    nums9 = [10, 5, 2, 6]
    k9 = 100
    result9 = sw.subarray_product_less_than_k(nums9, k9)
    print(f"   Array: {nums9}, K={k9}")
    print(f"   Result: {result9}")

    # Example 10: Longest Subarray of 1's After Deleting One Element
    print("\n10. Longest Subarray of 1's After Deleting One Element")
    nums10 = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    result10 = sw.longest_subarray_with_ones_after_deleting(nums10)
    print(f"   Array: {nums10}")
    print(f"   Result: {result10}")

    # Example 11: Minimum Window Substring
    print("\n11. Minimum Window Substring")
    s11 = "ADOBECODEBANC"
    t11 = "ABC"
    result11 = sw.min_window_substring(s11, t11)
    print(f"   String: '{s11}', Target: '{t11}'")
    print(f"   Result: '{result11}'")

    # Example 12: Contains Duplicate II
    print("\n12. Contains Duplicate II (within K distance)")
    nums12 = [1, 2, 3, 1, 2, 3]
    k12 = 2
    result12 = sw.contains_nearby_duplicate(nums12, k12)
    print(f"   Array: {nums12}, K={k12}")
    print(f"   Result: {result12}")

    # Example 13: Return Max Sum Subarray
    print("\n13. Return Subarray with Maximum Sum of Size K")
    arr13 = [2, 1, 5, 1, 3, 2]
    k13 = 3
    result13 = sw.max_sum_subarray_size_k_sliding(arr13, k13)
    print(f"   Array: {arr13}, K={k13}")
    print(f"   Result: {result13}")

    # Example 14: Longest Turbulent Subarray
    print("\n14. Longest Turbulent Subarray")
    arr14 = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    result14 = sw.longest_turbulent_subarray(arr14)
    print(f"   Array: {arr14}")
    print(f"   Result: {result14}")

    print("\n" + "=" * 80)
    print("All sliding window patterns demonstrated successfully!")
    print("=" * 80)


# Individual function calls - easy to use
def get_max_sum_subarray(arr, k):
    """Wrapper function for max sum subarray"""
    return SlidingWindow.max_sum_subarray_of_size_k(arr, k)


def get_smallest_subarray_sum(arr, target):
    """Wrapper for smallest subarray with sum >= target"""
    return SlidingWindow.smallest_subarray_with_sum_given(arr, target)


def get_longest_k_distinct(s, k):
    """Wrapper for longest substring with k distinct characters"""
    return SlidingWindow.longest_substring_with_k_distinct(s, k)


def get_longest_unique_substring(s):
    """Wrapper for longest substring without repeating"""
    return SlidingWindow.longest_substring_without_repeating(s)


def get_max_consecutive_ones(nums, k):
    """Wrapper for max consecutive ones after flipping"""
    return SlidingWindow.max_consecutive_ones(nums, k)


def find_all_anagrams(s, p):
    """Wrapper for finding anagrams"""
    return SlidingWindow.find_anagrams(s, p)


def get_min_window_substring(s, t):
    """Wrapper for minimum window substring"""
    return SlidingWindow.min_window_substring(s, t)


# Main execution
if __name__ == "__main__":
    # Run all examples
    sliding_window_examples()

    # Or call individual functions:
    print("\n\nINDIVIDUAL FUNCTION CALLS:")
    print("-" * 50)

    # Example: Using individual functions
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    result = get_max_sum_subarray(arr, k)
    print(f"Max sum of subarray of size {k}: {result}")

    s = "pwwkew"
    result = get_longest_unique_substring(s)
    print(f"Longest substring without repeating in '{s}': {result}")

    nums = [1, 1, 0, 1, 1, 1]
    k = 1
    result = get_max_consecutive_ones(nums, k)
    print(f"Max consecutive ones after flipping {k} zeros: {result}")

    print()

    # Example: Get longest substring without repeating
    result = SlidingWindow.longest_substring_without_repeating("abcabcbb")
    print(result)  # Output: 3

"""
14 Different Sliding Window Problems:
Maximum Sum Subarray of Size K
Smallest Subarray with Sum >= Target
Longest Substring with K Distinct Characters
Longest Substring Without Repeating Characters
Longest Repeating Character Replacement
Max Consecutive Ones After Flipping K Zeros
Find All Anagrams in a String
Maximum Vowels in Substring of Length K
Subarray Product Less Than K
Longest Subarray of 1's After Deleting One Element
Minimum Window Substring
Contains Duplicate II
Return Max Sum Subarray
Longest Turbulent Subarray

"""