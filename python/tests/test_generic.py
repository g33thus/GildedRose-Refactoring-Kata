import unittest

from gilded_rose import Item, GildedRose
from support import make, tick
from item_names import ItemName


class TestNormalItem(unittest.TestCase):

    # ---------- Quality degradation ----------

    def test_quality_degrades_by_1(self):
        item = tick(make("foo", 5, 10))
        self.assertEqual(9, item.quality)

    def test_quality_degrades_twice_as_fast_after_sell_date(self):
        item = tick(make("foo", 0, 10))
        self.assertEqual(8, item.quality)

    def test_quality_drops_to_zero_from_one(self):
        item = tick(make("foo", 5, 1))
        self.assertEqual(0, item.quality)

    # ---------- Quality floor (never negative) ----------

    def test_quality_never_negative(self):
        item = tick(make("foo", 5, 0))
        self.assertEqual(0, item.quality)

    def test_quality_never_negative_past_sell_date(self):
        item = tick(make("foo", -1, 0))
        self.assertEqual(0, item.quality)

    def test_quality_floors_at_zero_when_double_degrade_from_one(self):
        # transition day with quality=1: 1 - 2 must floor at 0, not -1
        item = tick(make("foo", 0, 1))
        self.assertEqual(0, item.quality)

    # ---------- sell_in ----------

    def test_sell_in_decreases(self):
        item = tick(make("foo", 5, 10))
        self.assertEqual(4, item.sell_in)


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
        item = tick(items)
        self.assertEqual(0, item.sell_in)
        self.assertEqual(9, item.quality)
        item = tick(items)
        # day two: now past sell date, degrades by 2
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(7, item.quality)


if __name__ == '__main__':
    unittest.main()
