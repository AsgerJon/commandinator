"""Text provides a class representation of the texts in Minecraft. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import json
from typing import TYPE_CHECKING

from worktoy.desc import AttriBox, Field
from worktoy.base import overload
from worktoy.parse import maybe

from commandinator.data import AbstractData, Color, FormatFlags, WIPField
from moreworktoy import dict2str

if TYPE_CHECKING:
  from commandinator import AbstractItem


class Text(AbstractData):
  """Text provides a class representation of the texts in Minecraft. """

  text = AttriBox[str]()
  color = AttriBox[Color]()
  italic = AttriBox[bool](False)
  bold = AttriBox[bool](False)
  underlined = AttriBox[bool](False)
  strikethrough = AttriBox[bool](False)
  obfuscated = AttriBox[bool](False)

  #  Not yet implemented
  insertion = WIPField()
  clickEvent = WIPField()
  hoverEvent = WIPField()

  def __init__(self, text: str = None) -> None:
    self.text = maybe(text, '')

  def __str__(self, ) -> str:
    """String representation"""
    out = {'text': self.text}
    if self.color:
      out['color'] = str(self.color)
    if not self.italic:
      out['italic'] = 'false'
    if self.bold:
      out['bold'] = 'true'
    if self.underlined:
      out['underlined'] = 'true'
    if self.strikethrough:
      out['strikethrough'] = 'true'
    if self.obfuscated:
      out['obfuscated'] = 'true'
    return dict2str(out)

  def __bool__(self, ) -> bool:
    """Boolean representation"""
    return True if self.text else False
