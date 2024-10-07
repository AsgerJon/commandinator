"""ArmorMaterial encapsulates the materials that armor can be made of."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import KeeNum, auto


class ArmorMaterial(KeeNum):
  """ArmorMaterial encapsulates the materials that armor can be made of."""

  LEATHER = auto()
  GOLD = auto()
  CHAINMAIL = auto()
  IRON = auto()
  DIAMOND = auto()
  NETHERITE = auto()
  TURTLE = auto()
