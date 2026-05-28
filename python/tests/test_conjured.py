import unittest

from support import make, tick
from item_names import ItemName


class TestConjured(unittest.TestCase):

    # ---------- Degradation rate ----------

    def test_degrades_twice_as_fast(self):
        item = tick(make(ItemName.CONJURED_CAKE, 5, 10))
        self.assertEqual(8, item.quality)

    def test_degrades_four_times_after_sell_date(self):
        item = tick(make(ItemName.CONJURED_CAKE, 0, 10))
        self.assertEqual(6, item.quality)

    def test_quality_49_drops_to_47(self):
        # confirms conjured is not treated as Brie (would go up); no cap interaction
        item = tick(make(ItemName.CONJURED_CAKE, 5, 49))
        self.assertEqual(47, item.quality)

    # ---------- Quality floor (never negative) ----------

    def test_quality_never_negative(self):
        item = tick(make(ItemName.CONJURED_CAKE, 5, 0))
        self.assertEqual(0, item.quality)

    def test_floors_at_zero_past_sell_date_from_one(self):
        # 1 - 4 must floor at 0, not -2
        item = tick(make(ItemName.CONJURED_CAKE, 0, 1))
        self.assertEqual(0, item.quality)

    def test_floors_at_zero_past_sell_date_from_three(self):
        # 3 - 4 must floor at 0, not -1
        item = tick(make(ItemName.CONJURED_CAKE, 0, 3))
        self.assertEqual(0, item.quality)


if __name__ == '__main__':
    unittest.main()
