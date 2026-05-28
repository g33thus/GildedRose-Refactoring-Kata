import unittest

from item import Item
from item_names import ItemName


class TestItemValidation(unittest.TestCase):

    # ---------- Valid construction ----------

    def test_normal_item_in_range_builds(self):
        item = Item("foo", 5, 10)
        self.assertEqual(10, item.quality)

    def test_quality_at_bounds_builds(self):
        self.assertEqual(0, Item("foo", 5, 0).quality)
        self.assertEqual(50, Item("foo", 5, 50).quality)

    # ---------- Quality range (non-legendary) ----------

    def test_quality_above_50_raises(self):
        with self.assertRaises(ValueError):
            Item("foo", 5, 51)

    def test_quality_below_0_raises(self):
        with self.assertRaises(ValueError):
            Item("foo", 5, -1)

    # ---------- sell_in must be an integer ----------

    def test_string_sell_in_raises(self):
        with self.assertRaises(TypeError):
            Item("foo", "5", 10)

    def test_float_sell_in_raises(self):
        with self.assertRaises(TypeError):
            Item("foo", 1.5, 10)

    # ---------- Legendary exemption ----------

    def test_sulfuras_quality_80_builds(self):
        item = Item(ItemName.SULFURAS, 0, 80)
        self.assertEqual(80, item.quality)

    def test_sulfuras_negative_quality_builds(self):
        # off-spec input is allowed for legendary: it never alters anyway
        item = Item(ItemName.SULFURAS, 5, -5)
        self.assertEqual(-5, item.quality)


if __name__ == '__main__':
    unittest.main()
