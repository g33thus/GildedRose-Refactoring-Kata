import unittest

from gilded_rose import Item, GildedRose


class TestNormalItem(unittest.TestCase):

    # ---------- Quality degradation ----------

    def test_quality_degrades_by_1(self):
        items = [Item("foo", 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].quality)

    def test_quality_degrades_twice_as_fast_after_sell_date(self):
        items = [Item("foo", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(8, items[0].quality)

    def test_quality_drops_to_zero_from_one(self):
        # plain decrement on a normal day
        items = [Item("foo", 5, 1)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    # ---------- Quality floor (never negative) ----------

    def test_quality_never_negative(self):
        items = [Item("foo", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_negative_past_sell_date(self):
        items = [Item("foo", -1, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_floors_at_zero_when_double_degrade_from_one(self):
        # transition day with quality=1: 1 - 2 must floor at 0, not -1
        items = [Item("foo", 0, 1)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    # ---------- sell_in ----------

    def test_sell_in_decreases(self):
        items = [Item("foo", 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(4, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
