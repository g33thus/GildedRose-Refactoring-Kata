"""Per-item update strategies and the dispatch that picks one.

Each item type has its own updater. `updater_for` maps an item to the updater
that matches its name.
"""

from item_names import ItemName
from helpers import increase_quality, decrease_quality, decrement_sell_in


class ItemUpdater:
    """Base rule = a normal item: degrades by 1, twice as fast once expired."""

    def update(self, item):
        # One day's change: adjust quality, age the item, then apply the
        # post-sell-date penalty only once sell_in has gone negative.
        self._before_expiry(item)
        decrement_sell_in(item)
        if item.sell_in < 0:
            self._after_expiry(item)

    def _before_expiry(self, item):
        # Quality change applied every day, before the sell date passes.
        decrease_quality(item)

    def _after_expiry(self, item):
        # Extra change applied only on days past the sell date.
        decrease_quality(item)


class AgedBrieUpdater(ItemUpdater):
    """Aged Brie: gains quality with age, twice as fast once expired."""

    def _before_expiry(self, item):
        increase_quality(item)

    def _after_expiry(self, item):
        increase_quality(item)


class BackstageUpdater(ItemUpdater):
    """Backstage passes: rise faster as the concert nears, worthless after it."""

    def _before_expiry(self, item):
        # +1 normally, +2 within 10 days, +3 within 5 days (cumulative tiers).
        amount = 1
        if item.sell_in < 11:
            amount += 1
        if item.sell_in < 6:
            amount += 1
        increase_quality(item, amount)

    def _after_expiry(self, item):
        # After the concert the pass is worthless.
        item.quality = 0


class ConjuredUpdater(ItemUpdater):
    """Conjured items: degrade twice as fast as a normal item (-2, -4 expired)."""

    def _before_expiry(self, item):
        decrease_quality(item, 2)

    def _after_expiry(self, item):
        decrease_quality(item, 2)


class LegendaryUpdater(ItemUpdater):
    """Sulfuras: legendary, never changes. update() is a deliberate no-op."""

    def update(self, item):
        pass


# Exact-name lookup: the fast path for items identified by their full name.
_EXACT = {
    ItemName.AGED_BRIE: AgedBrieUpdater(),
    ItemName.BACKSTAGE: BackstageUpdater(),
    ItemName.SULFURAS: LegendaryUpdater(),
}

# Name-category rules: tried only when no exact name matches. This is the one
# place where behaviour is keyed off a name pattern rather than an exact name.
_NAME_CATEGORY_RULES = (
    (lambda name: name.startswith(ItemName.CONJURED_PREFIX), ConjuredUpdater()),
)

# Fallback for any item that matches no rule above.
_DEFAULT = ItemUpdater()


def updater_for(item):
    """Pick the updater for an item: exact name, then category rule, then default."""
    if item.name in _EXACT:
        return _EXACT[item.name]
    for matches, updater in _NAME_CATEGORY_RULES:
        if matches(item.name):
            return updater
    return _DEFAULT
