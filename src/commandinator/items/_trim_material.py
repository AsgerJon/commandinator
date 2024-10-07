"""TrimMaterial enumerates the materials that may be used to decorate
armor pieces with trim patterns in Minecraft."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import KeeNum, auto


class TrimMaterial(KeeNum):
  """TrimMaterial enumerates the materials that may be used to decorate
  armor pieces with trim patterns in Minecraft."""

  NULL = auto()
  AMETHYST = auto()
  COPPER = auto()
  DIAMOND = auto()
  EMERALD = auto()
  GOLD = auto()
  IRON = auto()
  LAPIS = auto()
  QUARTZ = auto()
  NETHERITE = auto()
  REDSTONE = auto()
