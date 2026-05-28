import unittest

from support import make, tick
from item_names import ItemName


class TestSulfuras(unittest.TestCase):

    # ---------- Legendary: never alters ----------

    def test_negative_quality_input_unchanged(self):
        # defensive: legendary never alters, even with off-spec inputs
        item = tick(make(ItemName.SULFURAS, 5, -5))
        self.assertEqual(-5, item.quality)

    def test_unchanged_past_sell_date(self):
        item = tick(make(ItemName.SULFURAS, -1, 80))
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_quality_stays_80_over_many_days(self):
        # spec: legendary quality is 80 and never alters
        item = tick(make(ItemName.SULFURAS, 10, 80), days=20)
        self.assertEqual(80, item.quality)
        self.assertEqual(10, item.sell_in)


if __name__ == '__main__':
    unittest.main()
