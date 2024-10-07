"""Enchantment provides a class representation of the enchantments in
Minecraft. The class provides for both applied and stored enchantments. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import BaseObject, overload
from worktoy.desc import AttriBox
from worktoy.parse import maybe


class Enchantment(BaseObject):
  """Enchantment provides a class representation of the enchantments in
  Minecraft. The class provides for both applied and stored enchantments. """

  name = AttriBox[str]('')
  level = AttriBox[int](1)

  def __init__(self, name: str, level: int = None) -> None:
    self.name = name
    self.level = maybe(level, 1)

  def __str__(self, ) -> str:
    """String representation"""
    return """%s: %d""" % (self.name, self.level)

  def __int__(self) -> int:
    """Integer representation"""
    return self.level
