"""Unit tests for critical calculations.

Run with: pytest
"""

import math

def pct_poor(ratings, threshold=4):
    ratings = [r for r in ratings if r is not None]
    if len(ratings) == 0:
        return math.nan
    return sum(1 for r in ratings if r <= threshold) / len(ratings)

def test_pct_poor_basic():
    # 2 out of 5 are <= 4
    assert abs(pct_poor([10, 4, 3, 7, 8]) - 0.4) < 1e-9

def test_pct_poor_all_missing():
    assert math.isnan(pct_poor([None, None]))

def test_pct_poor_threshold_edge():
    assert abs(pct_poor([4, 4, 5], threshold=4) - (2/3)) < 1e-9
