"""Tests for LeetCode 704: Binary Search."""

import pytest
from p704_binary_search import linear_search, search


class TestSearch:
    """Test the exact-match binary search."""

    def test_found_middle(self):
        assert search([-1, 0, 3, 5, 9, 12], 9) == 4

    def test_not_found(self):
        assert search([-1, 0, 3, 5, 9, 12], 2) == -1

    def test_single_found(self):
        assert search([5], 5) == 0

    def test_single_not_found(self):
        assert search([5], -5) == -1

    def test_first_element(self):
        assert search([1, 2, 3, 4, 5], 1) == 0

    def test_last_element(self):
        assert search([1, 2, 3, 4, 5], 5) == 4

    def test_two_elements_first(self):
        assert search([1, 3], 1) == 0

    def test_two_elements_second(self):
        assert search([1, 3], 3) == 1

    def test_two_elements_not_found(self):
        assert search([1, 3], 2) == -1

    def test_negative_numbers(self):
        assert search([-10, -5, -2, 0, 3], -5) == 1

    def test_empty(self):
        assert search([], 1) == -1


class TestLinearMatch:
    """Linear search should agree with binary search."""

    @pytest.mark.parametrize(
        "nums,target",
        [
            ([-1, 0, 3, 5, 9, 12], 9),
            ([-1, 0, 3, 5, 9, 12], 2),
            ([5], 5),
            ([5], -5),
            ([], 1),
        ],
    )
    def test_matches_binary(self, nums, target):
        assert linear_search(nums, target) == search(nums, target)
