import unittest

from helpers import make, tick
from item_names import ItemName


class TestSulfuras(unittest.TestCase):

    # ---------- Legendary: quality unchanged ----------

    def test_quality_never_changes(self):
        item = tick(make(ItemName.SULFURAS, 5, 80))
        self.assertEqual(80, item.quality)

    def test_negative_quality_input_unchanged(self):
        # defensive: legendary never alters, even with off-spec inputs
        item = tick(make(ItemName.SULFURAS, 5, -5))
        self.assertEqual(-5, item.quality)

    # ---------- Legendary: sell_in unchanged ----------

    def test_sell_in_never_changes(self):
        item = tick(make(ItemName.SULFURAS, 5, 80))
        self.assertEqual(5, item.sell_in)

    def test_sell_in_zero_unchanged(self):
        item = tick(make(ItemName.SULFURAS, 0, 80))
        self.assertEqual(0, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_unchanged_past_sell_date(self):
        item = tick(make(ItemName.SULFURAS, -1, 80))
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(80, item.quality)


if __name__ == '__main__':
    unittest.main()
