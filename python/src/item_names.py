
from enum import Enum


class ItemName(str, Enum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    CONJURED_PREFIX = "Conjured"          # category prefix: any "Conjured ..." item
    CONJURED_CAKE = "Conjured Mana Cake"  # one concrete conjured item
