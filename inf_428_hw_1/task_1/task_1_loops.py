from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        current_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1

        max_len = max(max_len, current_len)

        return max_len

# test
if __name__ == "__main__":
    solution = Solution()  # Create an instance of Solution

    # Test case 1
    nums1 = [1, 3, 5, 4, 7]
    print(solution.findLengthOfLCIS(nums1))  # output: 3

    # Test case 2
    nums2 = [2, 2, 2, 2, 2]
    print(solution.findLengthOfLCIS(nums2))  # output: 1
