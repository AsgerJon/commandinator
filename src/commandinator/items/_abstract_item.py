"""AbstractItem provides an abstract baseclass for Minecraft items."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import BaseObject, overload
from worktoy.desc import AttriBox

from commandinator.items import Enchantment
from commandinator.data import Text, Lore


class AbstractItem(BaseObject):
  """AbstractItem provides an abstract baseclass for Minecraft items."""

  itemId = AttriBox[str]()
  count = AttriBox[int](1)
  customName = AttriBox[Text]('')
  lore = AttriBox[Lore]('')
  enchants = AttriBox[dict]()

  @overload(str, int)
  def __init__(self, itemId: str, count: int) -> None:
    self.itemId = itemId
    self.count = count

  @overload(str)
  def __init__(self, itemId: str) -> None:
    self.__init__(itemId, 1)

  @overload(str)
  def enchant(self, name: str) -> None:
    self.enchant(name, 1)

  @overload(str, int)
  def enchant(self, name: str, level: int) -> None:
    """Add an enchantment to the item"""
    self.enchant(Enchantment(name, level))

  @overload(Enchantment)
  def enchant(self, enchantment: Enchantment) -> None:
    """Add an enchantment to the item"""
    self.enchants[enchantment.name] = enchantment.level

  def notInContainer(self) -> str:
    """Returns the not in container syntax."""
    ID = self.itemId
    levels = self.getEnchantLevels()
    name = str(self.customName)
    out = """%s[custom_name='%s', enchantments={%s}]"""
    return out % (ID, name, levels)

  def getName(self) -> str:
    """Getter-function for custom name"""
    fmtSpec = """custom_name:'%s'"""
    value = self.customName
    return fmtSpec % value if value else ''

  def getLore(self) -> str:
    """Getter-function for lore"""
    fmtSpec = """lore:%s"""
    value = self.lore
    return fmtSpec % value if value else ''

  def getEnchants(self) -> str:
    """Getter-function for enchants"""
    fmtSpec = """enchantments:{levels:{%s}}"""
    value = self.getEnchantLevels()
    return fmtSpec % value if value else ''

  def getComponents(self) -> str:
    """Getter-function for the components"""
    name, lore, enchants = self.getName(), self.getLore(), self.getEnchants()
    comps = [i for i in [name, lore, enchants] if i]
    if not comps:
      return ''
    return """components:{%s}""" % ', '.join(comps)

  def inContainer(self, ) -> str:
    """Returns the in container syntax"""
    totalSpec = """id:\"%s\", count:%d, %s"""
    totalValue = [self.itemId, self.count, self.getComponents()]
    out = totalSpec % (*totalValue,)
    out = out.strip()
    if out[-1] == ',':
      return out[:-1]
    return out

  def getEnchantLevels(self) -> str:
    """Getter function for enchant levels"""
    out = []
    for (key, val) in self.enchants.items():
      out.append("""'%s':%d""" % (key, int(val)))
    return ', '.join(out)

  def __str__(self) -> str:
    """Returns in container syntax"""
    return self.inContainer()
