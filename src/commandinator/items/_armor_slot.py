"""ArmorSlot enumerates the four armour slots in the game."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from enum import auto

from worktoy.keenum import KeeNum


class ArmorSlot(KeeNum):
  """ArmorSlot enumerates the four armour slots in the game."""

  HELMET = auto()
  CHESTPLATE = auto()
  LEGGINGS = auto()
  BOOTS = auto()
