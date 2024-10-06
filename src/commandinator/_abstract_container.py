"""AbstractContainer subclasses AbstractItem adding support for containing
other item stacks."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import json

from worktoy.base import BaseObject, overload
from worktoy.desc import AttriBox

from commandinator import AbstractItem
from moreworktoy import FixedArray


class AbstractContainer(AbstractItem):
  """AbstractContainer subclasses AbstractItem adding support for containing
  other item stacks."""

  contents = AttriBox[FixedArray](AbstractItem, 27)

  @classmethod
  def dict2str(cls, data: dict) -> str:
    """Converts a dictionary to a string"""
    out = []
    for (key, val) in data.items():
      if isinstance(val, dict):
        out.append("""%s: {%s}""" % (key, cls.dict2str(val)))
      else:
        out.append("""%s: %s""" % (key, val))
    return ', '.join(out)

  def _getInner(self, ) -> str:
    """Returns the inner part of the item string"""
    self.count = -1
    base = AbstractItem._getInner(self)
    if not self.contents:
      return base
    out = []
    for (i, slot) in enumerate(self.contents):
      if slot is not None:
        entry = {'slot': i, 'item': {
            'id'   : slot.itemId,
            'count': slot.count,
        }}
        if slot.components:
          entry['item']['components'] = json.loads(slot.components)
        out.append(self.dict2str(entry))
    container = """container=[%s]""" % ', '.join(out)
    if base:
      return ', '.join([base, container])
    return container

  @overload(AbstractItem, int)
  def append(self, item: AbstractItem, count: int) -> None:
    """Adds an item to the container"""
    item.count = count
    self.contents.append(item)

  @overload(AbstractItem)
  def append(self, item: AbstractItem) -> None:
    """Adds an item to the container"""
    self.append(item, 1)

  def __setitem__(self, index: int, item: AbstractItem) -> None:
    """Sets an item in the container"""
    self.contents[index] = item
