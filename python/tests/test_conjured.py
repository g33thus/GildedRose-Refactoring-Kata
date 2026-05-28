import unittest

from gilded_rose import Item, GildedRose


class TestConjured(unittest.TestCase):

    def test_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(8, items[0].quality)

    def test_degrades_four_times_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(6, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
