import unittest

from gilded_rose import Item, GildedRose
from item_names import ItemName


class TestAgedBrie(unittest.TestCase):

    # ---------- Quality increases ----------

    def test_quality_increases(self):
        items = [Item(ItemName.AGED_BRIE, 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(11, items[0].quality)

    def test_quality_increases_twice_after_sell_date(self):
        items = [Item(ItemName.AGED_BRIE, -1, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(12, items[0].quality)

    def test_quality_increases_by_2_on_transition_day(self):
        # sell_in=0 is the transition day: degrades-twice rule applies, so +2
        items = [Item(ItemName.AGED_BRIE, 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(12, items[0].quality)

    # ---------- 50-quality cap ----------

    def test_quality_capped_at_50(self):
        items = [Item(ItemName.AGED_BRIE, 5, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_capped_at_50_past_sell_date(self):
        items = [Item(ItemName.AGED_BRIE, -1, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_49_past_sell_date_caps_not_overflows(self):
        # 49 + 2 would be 51; must cap to 50
        items = [Item(ItemName.AGED_BRIE, -1, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    # ---------- sell_in ----------

    def test_sell_in_decrements_into_negative(self):
        items = [Item(ItemName.AGED_BRIE, 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
