"""Text provides a class representation of the texts in Minecraft. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.desc import AttriBox
from worktoy.base import overload, BaseObject
from worktoy.text import monoSpace

from commandinator.data import Color

if TYPE_CHECKING:
  pass

FALSE = """false"""
TRUE = """true"""
BOOL = lambda x: '%s' % (TRUE if x else FALSE,)


class Text(BaseObject):
  """CANCER SYNTAX"""

  text = AttriBox[str]('')  # FUCK YOU
  color = AttriBox[Color](255, 0, 144)  # KILL YOURSELF
  italic = AttriBox[bool](False)
  bold = AttriBox[bool](False)
  underlined = AttriBox[bool](False)
  strikethrough = AttriBox[bool](False)
  obfuscated = AttriBox[bool](False)

  def __str__(self) -> str:
    """Returns the syntax for when the item is inside a container,
    which is fucking different from normal. FUCK YOU!!"""
    fmtSpec = monoSpace("""{"text": "%s", "color": "%s", 
    "italic": %s, "bold": %s, "underlined": %s,
    "strikethrough": %s, "obfuscated": %s
    }""")
    values = [self.text, str(self.color), BOOL(self.italic),
              BOOL(self.bold), BOOL(self.underlined),
              BOOL(self.strikethrough), BOOL(self.obfuscated)]
    return fmtSpec % (*values,)

  @overload(str, int, int, int)
  def __init__(self, text: str, r: int, g: int, b: int) -> None:
    self.color = Color(r, g, b)
    self.text = text

  @overload(str)
  def __init__(self, text: str) -> None:
    self.__init__(text, 255, 0, 144)

  @overload()
  def __init__(self) -> None:
    self.__init__('', 255, 0, 144)

  def __bool__(self) -> bool:
    return True if self.text else False
