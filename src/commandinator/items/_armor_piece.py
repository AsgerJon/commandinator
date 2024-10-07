"""ArmorPiece subclasses AbstractItem providing a class representation of
armor pieces in Minecraft."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.desc import AttriBox

from commandinator.items import AbstractItem, ArmorSlot, ArmorMaterial, \
  TrimPattern, TrimMaterial


class ArmorPiece(AbstractItem):
  """ArmorPiece subclasses AbstractItem providing a class representation of
  armor pieces in Minecraft."""

  equipSlot = AttriBox[ArmorSlot]()
  material = AttriBox[ArmorMaterial]()
  enchantments = AttriBox[list]()
  trimPattern = AttriBox[TrimPattern](TrimPattern.NULL)
  trimMaterial = AttriBox[TrimMaterial](TrimMaterial.NULL)
