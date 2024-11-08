from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        # Use set intersection to find common elements
        result = list(set1 & set2)

        return result


# test
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(solution.intersection(nums1, nums2))  # output: [2]

    # Test case 2
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(solution.intersection(nums1, nums2))  # output: [4, 9] or [9, 4]
