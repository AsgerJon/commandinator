"""FormatFlags provides a class with boolean valued attributes for each of
the formatting flags in Minecraft:

- bold
- italic
- underlined
- strikethrough
- obfuscated

"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import json

from worktoy.base import FastObject
from worktoy.desc import AttriBox
from worktoy.ezdata import EZData

from commandinator.data import AbstractData


class FormatFlags(AbstractData):
  """FormatFlags provides a class with boolean valued attributes for each of
  the formatting flags in Minecraft:

  - bold
  - italic
  - underlined
  - strikethrough
  - obfuscated
  """

  bold = AttriBox[bool](False)
  italic = AttriBox[bool](False)
  underlined = AttriBox[bool](False)
  strikethrough = AttriBox[bool](False)
  obfuscated = AttriBox[bool](False)

  def getData(self) -> dict[str, str]:
    return dict(
        bold='true' if self.bold else 'false',
        italic='true' if self.italic else 'false',
        underlined='true' if self.underlined else 'false',
        strikethrough='true' if self.strikethrough else 'false',
        obfuscated='true' if self.obfuscated else 'false',
    )

  def __str__(self, ) -> str:
    entries = []
    for (key, val) in self.getData().items():
      entries.append("""%s: %s""" % (key, val))
    return """%s""" % ', '.join(entries)

  def __repr__(self, ) -> str:
    fmtSpec = """ "%s": "%s" """
    items = [fmtSpec % (key, val) for key, val in self.getData().items()]
    return """FormatFlags({%s})""" % ', '.join(items)

  def getValue(self) -> str:
    """Returns the string representation of the format flags"""
    return json.dumps(self.getData())
