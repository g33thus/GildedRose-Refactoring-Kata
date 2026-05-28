import unittest

from support import make, tick
from item_names import ItemName


class TestBackstagePasses(unittest.TestCase):

    # ---------- Tier increases ----------

    def test_quality_increases_by_1_when_more_than_10_days(self):
        item = tick(make(ItemName.BACKSTAGE, 15, 20))
        self.assertEqual(21, item.quality)

    def test_quality_increases_by_2_when_10_days_or_less(self):
        item = tick(make(ItemName.BACKSTAGE, 10, 20))
        self.assertEqual(22, item.quality)

    def test_quality_increases_by_3_when_5_days_or_less(self):
        item = tick(make(ItemName.BACKSTAGE, 5, 20))
        self.assertEqual(23, item.quality)

    # ---------- Post-concert ----------

    def test_quality_drops_to_zero_after_concert(self):
        item = tick(make(ItemName.BACKSTAGE, 0, 30))
        self.assertEqual(0, item.quality)

    def test_quality_stays_zero_when_already_zero_post_concert(self):
        item = tick(make(ItemName.BACKSTAGE, 0, 0))
        self.assertEqual(0, item.quality)

    # ---------- 50-quality cap ----------

    def test_quality_capped_at_50_when_bumping_by_2(self):
        item = tick(make(ItemName.BACKSTAGE, 10, 49))
        self.assertEqual(50, item.quality)

    def test_quality_capped_at_50_when_bumping_by_3(self):
        item = tick(make(ItemName.BACKSTAGE, 5, 49))
        self.assertEqual(50, item.quality)

    def test_quality_lands_exactly_on_50_bumping_by_2(self):
        # boundary: 48 + 2 = 50 exactly
        item = tick(make(ItemName.BACKSTAGE, 10, 48))
        self.assertEqual(50, item.quality)

    def test_quality_lands_exactly_on_50_bumping_by_3(self):
        # boundary: 47 + 3 = 50 exactly
        item = tick(make(ItemName.BACKSTAGE, 5, 47))
        self.assertEqual(50, item.quality)

    # ---------- Day-transition behaviour ----------

    def test_last_day_then_post_concert(self):
        # sell_in=1 -> +3 today, then sell_in=0 next day -> drops to 0
        items = make(ItemName.BACKSTAGE, 1, 20)
        item = tick(items)
        self.assertEqual(23, item.quality)
        self.assertEqual(0, item.sell_in)
        item = tick(items)
        self.assertEqual(0, item.quality)


if __name__ == '__main__':
    unittest.main()
