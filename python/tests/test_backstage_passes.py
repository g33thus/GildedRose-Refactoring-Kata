import unittest

from gilded_rose import Item, GildedRose
from item_names import ItemName


class TestBackstagePasses(unittest.TestCase):

    def test_quality_increases_by_1_when_more_than_10_days(self):
        items = [Item(ItemName.BACKSTAGE, 15, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(21, items[0].quality)

    def test_quality_increases_by_2_when_10_days_or_less(self):
        items = [Item(ItemName.BACKSTAGE, 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(22, items[0].quality)

    def test_quality_increases_by_3_when_5_days_or_less(self):
        items = [Item(ItemName.BACKSTAGE, 5, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(23, items[0].quality)

    def test_quality_drops_to_zero_after_concert(self):
        items = [Item(ItemName.BACKSTAGE, 0, 30)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_capped_at_50_when_bumping_by_2(self):
        items = [Item(ItemName.BACKSTAGE, 10, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_capped_at_50_when_bumping_by_3(self):
        items = [Item(ItemName.BACKSTAGE, 5, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)


if __name__ == '__main__':
    unittest.main()
