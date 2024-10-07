"""AbstractEnchantment provides an abstract baseclass for classes
representing enchantments in Minecraft."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import BaseObject
from worktoy.desc import AttriBox


class AbstractEnchantment(BaseObject):
  """AbstractEnchantment provides an abstract baseclass for classes
  representing enchantments in Minecraft."""

  itemId = AttriBox[str]()
  level = AttriBox[int](1)
  penalty = AttriBox[int]()
  