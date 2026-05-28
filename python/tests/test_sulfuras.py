import unittest

from gilded_rose import Item, GildedRose
from item_names import ItemName


class TestSulfuras(unittest.TestCase):

    # ---------- Legendary: quality unchanged ----------

    def test_quality_never_changes(self):
        items = [Item(ItemName.SULFURAS, 5, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(80, items[0].quality)

    def test_negative_quality_input_unchanged(self):
        # defensive: legendary never alters, even with off-spec inputs
        items = [Item(ItemName.SULFURAS, 5, -5)]
        GildedRose(items).update_quality()
        self.assertEqual(-5, items[0].quality)

    # ---------- Legendary: sell_in unchanged ----------

    def test_sell_in_never_changes(self):
        items = [Item(ItemName.SULFURAS, 5, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(5, items[0].sell_in)

    def test_sell_in_zero_unchanged(self):
        items = [Item(ItemName.SULFURAS, 0, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_unchanged_past_sell_date(self):
        items = [Item(ItemName.SULFURAS, -1, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


if __name__ == '__main__':
    unittest.main()
