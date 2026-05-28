import unittest

from support import make, tick


class TestNormalItem(unittest.TestCase):

    # ---------- Quality degradation ----------

    def test_quality_degrades_by_1(self):
        item = tick(make("foo", 5, 10))
        self.assertEqual(9, item.quality)

    def test_quality_degrades_twice_as_fast_after_sell_date(self):
        item = tick(make("foo", 0, 10))
        self.assertEqual(8, item.quality)

    def test_quality_drops_to_zero_from_one(self):
        item = tick(make("foo", 5, 1))
        self.assertEqual(0, item.quality)

    # ---------- Quality floor (never negative) ----------

    def test_quality_never_negative(self):
        item = tick(make("foo", 5, 0))
        self.assertEqual(0, item.quality)

    def test_quality_never_negative_past_sell_date(self):
        item = tick(make("foo", -1, 0))
        self.assertEqual(0, item.quality)

    def test_quality_floors_at_zero_when_double_degrade_from_one(self):
        # transition day with quality=1: 1 - 2 must floor at 0, not -1
        item = tick(make("foo", 0, 1))
        self.assertEqual(0, item.quality)

    # ---------- sell_in ----------

    def test_sell_in_decreases(self):
        item = tick(make("foo", 5, 10))
        self.assertEqual(4, item.sell_in)


if __name__ == '__main__':
    unittest.main()
