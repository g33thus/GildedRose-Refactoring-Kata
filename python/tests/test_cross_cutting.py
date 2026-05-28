import unittest

from gilded_rose import Item, GildedRose
from item_names import ItemName


class TestCrossCutting(unittest.TestCase):

    # ---------- Empty input ----------

    def test_empty_items_list_does_not_crash(self):
        rose = GildedRose([])
        rose.update_quality()  # must be a no-op, not raise
        self.assertEqual([], rose.items)

    # ---------- Mixed items in one call ----------

    def test_multiple_mixed_items_updated_independently(self):
        items = [
            Item("foo", 5, 10),                  # normal
            Item(ItemName.AGED_BRIE, 5, 10),     # brie
            Item(ItemName.SULFURAS, 5, 80),      # legendary
            Item(ItemName.BACKSTAGE, 5, 20),     # backstage (+3 tier)
        ]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].quality)
        self.assertEqual(11, items[1].quality)
        self.assertEqual(80, items[2].quality)
        self.assertEqual(23, items[3].quality)

    # ---------- Two-day simulation ----------

    def test_same_item_updated_twice(self):
        # two consecutive ticks on a normal item
        items = [Item("foo", 1, 10)]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(9, items[0].quality)
        rose.update_quality()
        # day two: now past sell date, degrades by 2
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(7, items[0].quality)


if __name__ == '__main__':
    unittest.main()
