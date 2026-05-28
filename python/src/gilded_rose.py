from item_names import ItemName
from helpers import increase_quality, decrease_quality, decrement_sell_in


class ItemUpdater:
    """Normal item: degrades by 1, twice as fast once expired."""

    def update(self, item):
        self._before_expiry(item)
        decrement_sell_in(item)
        if item.sell_in < 0:
            self._after_expiry(item)

    def _before_expiry(self, item):
        decrease_quality(item)

    def _after_expiry(self, item):
        decrease_quality(item)


class AgedBrieUpdater(ItemUpdater):
    """Increases in quality with age, faster once expired."""

    def _before_expiry(self, item):
        increase_quality(item)

    def _after_expiry(self, item):
        increase_quality(item)


class BackstageUpdater(ItemUpdater):
    """Rises faster as the concert nears, worthless afterwards."""

    def _before_expiry(self, item):
        amount = 1
        if item.sell_in < 11:
            amount += 1
        if item.sell_in < 6:
            amount += 1
        increase_quality(item, amount)

    def _after_expiry(self, item):
        item.quality = 0


class ConjuredUpdater(ItemUpdater):
    """Degrades twice as fast as a normal item."""

    def _before_expiry(self, item):
        decrease_quality(item, 2)

    def _after_expiry(self, item):
        decrease_quality(item, 2)


class LegendaryUpdater(ItemUpdater):
    """Sulfuras: never alters."""

    def update(self, item):
        pass


_EXACT = {
    ItemName.AGED_BRIE: AgedBrieUpdater(),
    ItemName.BACKSTAGE: BackstageUpdater(),
    ItemName.SULFURAS: LegendaryUpdater(),
}

# Name-category rules: tried only when no exact name matches.
# This is the one place where behaviour is keyed off a name pattern.
_NAME_CATEGORY_RULES = (
    (lambda name: name.startswith(ItemName.CONJURED_PREFIX), ConjuredUpdater()),
)
_DEFAULT = ItemUpdater()


def updater_for(item):
    if item.name in _EXACT:
        return _EXACT[item.name]
    for matches, updater in _NAME_CATEGORY_RULES:
        if matches(item.name):
            return updater
    return _DEFAULT


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater_for(item).update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
