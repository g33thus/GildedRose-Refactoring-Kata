"""Gilded Rose engine: advance every item one day via its matching updater."""

from updaters import updater_for


class GildedRose(object):
    """The inventory. Public entry point: advance every item by one day."""

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # Advance each item one day using its matching updater.
        for item in self.items:
            updater_for(item).update(item)
