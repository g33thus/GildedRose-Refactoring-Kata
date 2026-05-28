from item_names import ItemName
from helpers import is_legendary, increase, decrease, decrement_sell_in


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if is_legendary(item):
                continue
            if item.name == ItemName.AGED_BRIE:
                self._update_brie(item)
            elif item.name == ItemName.BACKSTAGE:
                self._update_backstage(item)
            elif self._is_conjured(item):
                self._update_conjured(item)
            else:
                self._update_normal(item)

            decrement_sell_in(item)

    def _update_normal(self, item):
        decrease(item)

        if item.sell_in <= 0:
            decrease(item)

    def _is_conjured(self, item):
        return item.name.startswith(ItemName.CONJURED_PREFIX)

    def _update_conjured(self, item):
        decrease(item, 2)

        if item.sell_in <= 0:
            decrease(item, 2)

    def _update_brie(self, item):
        increase(item)

        if item.sell_in <= 0:
            increase(item)

    def _update_backstage(self, item):
        increase(item)

        if item.sell_in <= 10:
            increase(item)

        if item.sell_in <= 5:
            increase(item)

        if item.sell_in <= 0:
            item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
