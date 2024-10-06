"""Lore data represents the lore of an item in Minecraft as a list of Text
instances. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import json

from worktoy.base import overload
from worktoy.desc import AttriBox

from commandinator.data import Text, AbstractData


class Lore(Text):
  """Lore data represents the lore of an item in Minecraft as a list of Text
  instances. """

  __iter_contents__ = None

  lines = AttriBox[list]()
  header = AttriBox[Text]()
  lineLength = AttriBox[int](50)

  def __iter__(self, ) -> Lore:
    """Implementation of the iterator protocol."""
    self.__iter_contents__ = [*self.lines, ]
    return self

  def __next__(self, ) -> Text:
    """Implementation of the iterator protocol."""
    if self.__iter_contents__:
      return self.__iter_contents__.pop(0)
    raise StopIteration

  def __getitem__(self, index: int) -> Text:
    """Implementation of the indexable protocol."""
    return self.lines[index]

  def __str__(self) -> str:
    """String representation"""
    if self.header or self.lines:
      out = []
      if self.header:
        out.append(str(self.header))
      for line in self.lines:
        out.append(str(line))
      return ', '.join(out)
    else:
      return ''

  def __bool__(self) -> bool:
    """Boolean representation"""
    return True if self.header or self.lines else False
