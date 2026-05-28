from gilded_rose import Item, GildedRose


def make(name, sell_in, quality):
    """Build a single-item list ready for GildedRose."""
    return [Item(name, sell_in, quality)]


def tick(items, days=1):
    """Run update_quality `days` times. Returns the first item for convenience."""
    rose = GildedRose(items)
    for _ in range(days):
        rose.update_quality()
    return items[0]
