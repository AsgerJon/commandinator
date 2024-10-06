"""AbstractItem provides an abstract baseclass for Minecraft items."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import json
from abc import abstractmethod

from worktoy.base import FastObject, BaseObject, overload
from worktoy.desc import AttriBox, Field, THIS
from worktoy.parse import maybe
from worktoy.text import typeMsg

from commandinator import Enchantment
from commandinator.data import Text, Lore
from moreworktoy import dict2str


class AbstractItem(BaseObject):
  """AbstractItem provides an abstract baseclass for Minecraft items."""

  #  Private variables
  __enchant_levels__ = None
  __custom_name__ = None
  __item_lore__ = None

  #  Fields
  components = Field()  # Here be hate
  enchantments = Field()
  customName = Field()
  lore = Field()

  @overload(str, int)
  def enchant(self, name: str, level: int) -> None:
    """Add an enchantment to the item."""
    self.enchantments.append(Enchantment(name, level))

  @overload(Enchantment)
  def enchant(self, enchantment: Enchantment) -> None:
    """Add an enchantment to the item."""
    self.enchantments.append(enchantment)

  @overload(str)
  def enchant(self, name: str) -> None:
    """Add an enchantment to the item."""
    self.__init__(name, 1)

  def _getEnchantLevels(self) -> dict:
    """Return a dictionary of the enchantment levels."""
    return maybe(self.__enchant_levels__, {})

  @components.GET
  def _getComponents(self) -> str:
    """The 1.20.5 introduced a vastly improved text system that motivated
    the author to create this package. What started of great, quickly
    turned to hate as multiple hours later, the author discovered the
    scam: The syntax for an item, CHANGES COMPLETELY when the item is to
    be in a container. This wasted so many hours. Fuck you!"""
    out = []
    if self.customName:
      out.append("""custom_name: %s""" % self.customName)
    if self.lore:
      out.append("""lore: %s""" % self.customName)
    enchantLevels = self._getEnchantLevels()
    enchants = []
    for (key, val) in self._getEnchantmentsDict().items():
      enchants.append("""%s: %d""" % (key, val))
    if enchants:
      out.append("""enchantments: {levels: {%s}}""" % (', '.join(enchants)))
    return ', '.join(out)

  @enchantments.GET
  def _getEnchantmentsDict(self) -> dict:
    """It was so close to not being a piece of shit, but at the finish
    line, a compromise were reached: 'We will let you make the item
    definition be non-shit', but we will subtly keep it shit when in a
    container.'"""
    return {'levels': self._getEnchantLevels()}

  def _createCustomName(self) -> None:
    """Creator-function for the customName contribution"""
    self.__custom_name__ = Text()

  @customName.GET
  def _getCustomName(self, **kwargs) -> Text:
    """Getter-function for the customName contribution to the components. """
    if self.__custom_name__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createCustomName()
      return self._getCustomName(_recursion=True)
    if isinstance(self.__custom_name__, Text):
      return self.__custom_name__
    e = typeMsg('__custom_name__', self.__custom_name__, Text)
    raise TypeError(e)

  def _createLore(self, ) -> None:
    """Creator-function for the lore"""
    self.__item_lore__ = Lore()

  def _getLore(self, **kwargs) -> Lore:
    """Getter-function for the lore"""
    if self.__item_lore__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createLore()
      return self._getLore(_recursion=True)
    if isinstance(self.__item_lore__, Lore):
      return self.__item_lore__
    e = typeMsg('__item_lore__', self.__item_lore__, Lore)
    raise TypeError(e)
