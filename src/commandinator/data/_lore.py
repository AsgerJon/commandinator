"""Lore data represents the lore of an item in Minecraft as a list of Text
instances. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import overload
from worktoy.desc import AttriBox

from commandinator.data import Text


class Lore(Text):
  """Lore data represents the lore of an item in Minecraft as a list of Text
  instances. """

  __iter_contents__ = None

  lines = AttriBox[list]()
  header = AttriBox[Text]('')
  lineLength = AttriBox[int](50)

  def __init__(self, *args) -> None:
    """Initialize the 'Lore' class."""

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
    if not self.header:
      return ''
    for line in self.lines:
      line.color = self.color
      line.italic = self.italic
      line.bold = self.bold
      line.underlined = self.underlined
      line.strikethrough = self.strikethrough
      line.obfuscated = self.obfuscated
    loreLines = [self.header, *self.lines]
    loreCodes = ["""'%s'""" % str(line) for line in loreLines]
    return """[%s]""" % ', '.join(loreCodes)

  def __bool__(self) -> bool:
    """Boolean representation"""
    return True if self.header or self.lines else False

  @overload(Text)
  def append(self, line: Text) -> None:
    """Append a line to the lore."""
    self.lines.append(line)

  @overload(str)
  def append(self, line: str) -> None:
    """Append a line to the lore."""
    self.lines.append(Text(line))
