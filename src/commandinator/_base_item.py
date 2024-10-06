"""BaseItem represents the base class for all items in the 'commandinator'
library. Every item in Minecraft represented here subclass this. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.desc import AttriBox, Field
from worktoy.meta import BaseObject, overload
from worktoy.parse import maybe
from worktoy.text import typeMsg


class BaseItem(BaseObject):
  """BaseItem represents the base class for all items in the 'commandinator'
  library. Every item in Minecraft represented here subclass this. """

  __item_name__ = None
  __item_lore__ = None
  __lore_sig__ = """Created by commandinator!"""

  itemId = AttriBox[str]()
  name = AttriBox[str]()
  lore = AttriBox[str]()

  @overload(str)
  def __init__(self, itemId: str) -> None:
    self.__init__(itemId, itemId, '')

  @overload(str, str)
  def __init__(self, itemId: str, itemName: str) -> None:
    self.__init__(itemId, itemName, '')

  @overload(str, str, str)
  def __init__(self, *args) -> None:
    self.itemId = args[0]
    self.name = args[1]
    self.lore = '\n'.join([i for i in [args[2], self.__lore_sig__] if i])
