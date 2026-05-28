import unittest

from gilded_rose import Item, GildedRose


class TestNormalItem(unittest.TestCase):

    def test_quality_degrades_by_1(self):
        items = [Item("foo", 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].quality)

    def test_quality_degrades_twice_as_fast_after_sell_date(self):
        items = [Item("foo", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(8, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("foo", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_negative_past_sell_date(self):
        items = [Item("foo", -1, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sell_in_decreases(self):
        items = [Item("foo", 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(4, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
