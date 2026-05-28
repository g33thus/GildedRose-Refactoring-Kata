"""Helpers for an item's quality and sell_in.

Rules every item shares: quality never exceeds 50 and never
drops below 0.
"""

# Shared quality bounds: the single source for the 0-50 clamps and for
# Item construction validation.
MIN_QUALITY = 0
MAX_QUALITY = 50


def increase_quality(item, amount=1):
    """Raise quality by amount, capped at the maximum."""
    item.quality = min(MAX_QUALITY, item.quality + amount)


def decrease_quality(item, amount=1):
    """Lower quality by amount, floored at the minimum (never negative)."""
    item.quality = max(MIN_QUALITY, item.quality - amount)


def decrement_sell_in(item):
    """Age the item by one day."""
    item.sell_in -= 1
