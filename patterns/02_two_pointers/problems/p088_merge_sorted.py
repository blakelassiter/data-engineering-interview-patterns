"""
LeetCode 88: Merge Sorted Array

Pattern: Two Pointers - Two Sequences (Reverse Direction)
Difficulty: Easy
Time Complexity: O(n + m)
Space Complexity: O(1)
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge nums2 into nums1 in-place. nums1 has enough space at the end.

    The trick is to fill from the back. Start at the end of both
    arrays and place the larger element at the end of nums1. This
    avoids overwriting elements we haven't processed yet.

    Args:
        nums1: First sorted array with m elements followed by n zeros.
        m: Number of real elements in nums1.
        nums2: Second sorted array with n elements.
        n: Number of elements in nums2.

    Example:
        >>> nums1 = [1, 2, 3, 0, 0, 0]
        >>> merge(nums1, 3, [2, 5, 6], 3)
        >>> nums1
        [1, 2, 2, 3, 5, 6]
    """
    # Start from the end of both arrays
    p1 = m - 1  # last real element in nums1
    p2 = n - 1  # last element in nums2
    write = m + n - 1  # last position in nums1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[write] = nums1[p1]
            p1 -= 1
        else:
            nums1[write] = nums2[p2]
            p2 -= 1
        write -= 1

    # If nums2 has remaining elements, copy them
    # (if nums1 has remaining elements, they're already in place)
    while p2 >= 0:
        nums1[write] = nums2[p2]
        p2 -= 1
        write -= 1


def merge_new_array(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Merge two sorted arrays into a new sorted array.

    Simpler version that creates a new list. Useful when
    in-place isn't required.

    Time: O(n + m)  Space: O(n + m)
    """
    result: list[int] = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    result.extend(nums1[i:])
    result.extend(nums2[j:])
    return result


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    print(f"In-place merge: {nums1}")
    assert nums1 == [1, 2, 2, 3, 5, 6]

    result = merge_new_array([1, 3, 5], [2, 4, 6])
    print(f"New array merge: {result}")
    assert result == [1, 2, 3, 4, 5, 6]
