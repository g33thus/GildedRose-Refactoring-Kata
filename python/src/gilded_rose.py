from item_names import ItemName
from helpers import is_legendary, increase_quality, decrease_quality, decrement_sell_in


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if is_legendary(item):
                continue
           
            self.update_quality_value(item)
            decrement_sell_in(item)
            self.update_after_expiry(item)


    def update_quality_value(self, item):
        if item.name == ItemName.AGED_BRIE:
            increase_quality(item)
        elif item.name == ItemName.BACKSTAGE:
            increase_quality(item)
            if item.sell_in < 11:
                increase_quality(item)
            if item.sell_in < 6:
                increase_quality(item)
        else:
            decrease_quality(item)


    def update_after_expiry(self, item):
        if item.sell_in >= 0:
            return
        if item.name == ItemName.AGED_BRIE:
            increase_quality(item)
        elif item.name == ItemName.BACKSTAGE:
            item.quality = 0
        else:
            decrease_quality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
