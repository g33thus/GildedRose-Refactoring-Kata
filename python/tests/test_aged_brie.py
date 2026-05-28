import unittest

from support import make, tick
from item_names import ItemName


class TestAgedBrie(unittest.TestCase):

    # ---------- Quality increases ----------

    def test_quality_increases(self):
        item = tick(make(ItemName.AGED_BRIE, 5, 10))
        self.assertEqual(11, item.quality)

    def test_quality_increases_twice_after_sell_date(self):
        item = tick(make(ItemName.AGED_BRIE, -1, 10))
        self.assertEqual(12, item.quality)

    def test_quality_increases_by_2_on_transition_day(self):
        # sell_in=0 is the transition day: degrades-twice rule applies, so +2
        item = tick(make(ItemName.AGED_BRIE, 0, 10))
        self.assertEqual(12, item.quality)

    # ---------- 50-quality cap ----------

    def test_quality_capped_at_50(self):
        item = tick(make(ItemName.AGED_BRIE, 5, 50))
        self.assertEqual(50, item.quality)

    def test_quality_capped_at_50_past_sell_date(self):
        item = tick(make(ItemName.AGED_BRIE, -1, 49))
        self.assertEqual(50, item.quality)

    def test_quality_49_past_sell_date_caps_not_overflows(self):
        # 49 + 2 would be 51; must cap to 50
        item = tick(make(ItemName.AGED_BRIE, -1, 49))
        self.assertEqual(50, item.quality)

    # ---------- sell_in ----------

    def test_sell_in_decrements_into_negative(self):
        item = tick(make(ItemName.AGED_BRIE, 0, 10))
        self.assertEqual(-1, item.sell_in)


if __name__ == '__main__':
    unittest.main()
