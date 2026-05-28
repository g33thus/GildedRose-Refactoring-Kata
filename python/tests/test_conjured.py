import unittest

from gilded_rose import Item, GildedRose
from item_names import ItemName




class TestConjured(unittest.TestCase):

    # ---------- Degradation rate ----------

    def test_degrades_twice_as_fast(self):
        items = [Item(ItemName.CONJURED_CAKE, 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(8, items[0].quality)

    def test_degrades_four_times_after_sell_date(self):
        items = [Item(ItemName.CONJURED_CAKE, 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(6, items[0].quality)

    def test_quality_49_drops_to_47(self):
        # confirms conjured is not treated as Brie (would go up); no cap interaction
        items = [Item(ItemName.CONJURED_CAKE, 5, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(47, items[0].quality)

    # ---------- Quality floor (never negative) ----------

    def test_quality_never_negative(self):
        items = [Item(ItemName.CONJURED_CAKE, 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_floors_at_zero_past_sell_date_from_one(self):
        # 1 - 4 must floor at 0, not -2
        items = [Item(ItemName.CONJURED_CAKE, 0, 1)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_floors_at_zero_past_sell_date_from_three(self):
        # 3 - 4 must floor at 0, not -1
        items = [Item(ItemName.CONJURED_CAKE, 0, 3)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
