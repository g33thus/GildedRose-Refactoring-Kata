import unittest

from gilded_rose import Item, GildedRose
from item_names import ItemName


class TestAgedBrie(unittest.TestCase):

    def test_quality_increases(self):
        items = [Item(ItemName.AGED_BRIE, 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(11, items[0].quality)

    def test_quality_increases_twice_after_sell_date(self):
        items = [Item(ItemName.AGED_BRIE, -1, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(12, items[0].quality)

    def test_quality_capped_at_50(self):
        items = [Item(ItemName.AGED_BRIE, 5, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_capped_at_50_past_sell_date(self):
        items = [Item(ItemName.AGED_BRIE, -1, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)


if __name__ == '__main__':
    unittest.main()
