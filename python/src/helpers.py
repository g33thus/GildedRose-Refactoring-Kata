from item_names import ItemName


def is_legendary(item):
    return item.name == ItemName.SULFURAS


def increase_quality(item, amount=1):
    item.quality = min(50, item.quality + amount)


def decrease_quality(item, amount=1):
    item.quality = max(0, item.quality - amount)


def decrement_sell_in(item):
    item.sell_in -= 1
