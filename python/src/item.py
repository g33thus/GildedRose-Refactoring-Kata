"""The Item data model with construction-time validation."""

from dataclasses import dataclass

from item_names import ItemName
from helpers import MIN_QUALITY, MAX_QUALITY


@dataclass(repr=False)  # repr=False keeps the custom __repr__ below
class Item:
    """One stock item (name, days-to-sell, quality).

    Validated on construction: sell_in and quality must be ints, and quality
    must sit in MIN_QUALITY..MAX_QUALITY. Sulfuras is legendary (quality 80)
    and is exempt from the range check.
    """

    name: str
    sell_in: int
    quality: int

    def __post_init__(self):
        if not isinstance(self.sell_in, int):
            raise TypeError(f"sell_in must be int, got {type(self.sell_in).__name__}")
        if not isinstance(self.quality, int):
            raise TypeError(f"quality must be int, got {type(self.quality).__name__}")
        if self.name != ItemName.SULFURAS and not (MIN_QUALITY <= self.quality <= MAX_QUALITY):
            raise ValueError(f"quality must be {MIN_QUALITY}-{MAX_QUALITY}, got {self.quality}")

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
