"""Color provides a class representation of the colors in Minecraft."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.base import FastObject
from worktoy.desc import AttriBox


class Color(FastObject):
  """Color provides a class representation of the colors in Minecraft."""
  red = AttriBox[int](255)
  green = AttriBox[int](255)
  blue = AttriBox[int](255)

  @staticmethod
  def parseColor(colorSpec: str) -> tuple[int, int, int]:
    """The received string argument should be a hex representation of the
    color or the name of a common color. """
    if colorSpec[0] == '#':
      colorSpec = colorSpec[1:]
    if len(colorSpec) == 6:
      r = int(colorSpec[:2], 16)
      g = int(colorSpec[2:4], 16)
      b = int(colorSpec[4:], 16)
      return r, g, b
    raise NotImplementedError  # Common colors not yet implemented

  def __init__(self, red: int, green: int, blue: int) -> None:
    self.red = red
    self.green = green
    self.blue = blue

  def _getHex(self) -> str:
    """Getter-function for hex representation in %s style"""
    r, g, b = hex(self.red)[2:], hex(self.green)[2:], hex(self.blue)[2:]
    return ("""#%2s%2s%2s""" % (r, g, b)).upper().replace(' ', '0')

  def getData(self) -> str | dict[str, str]:
    """Return a dictionary representation of the color"""
    return self._getHex()

  def __repr__(self, ) -> str:
    """Code representation of the color"""
    return """Color(%02d, %02d, %02d)""" % (self.red, self.green, self.blue)

  def __str__(self, ) -> str:
    """String representation of the color"""
    return self._getHex()

  if TYPE_CHECKING:
    __init__.__annotations__ = {'red': int, 'green': int, 'blue': int}
    __init__.__annotations__ = {'otherColor': FastObject}
