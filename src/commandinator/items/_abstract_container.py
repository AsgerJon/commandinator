"""AbstractContainer subclasses AbstractItem adding support for containing
other item stacks."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import overload
from worktoy.desc import AttriBox

from commandinator.items import AbstractItem
from moreworktoy import FixedArray


class AbstractContainer(AbstractItem):
  """AbstractContainer subclasses AbstractItem adding support for containing
  other item stacks."""

  contents = AttriBox[FixedArray](AbstractItem, 27)

  def _getContainer(self) -> str:
    """Getter-function for the code describing this item containing other
    items. """
    if not self.contents:
      return ''
    out = []
    for (i, x) in enumerate(self.contents):
      if x is not None:
        out.append("""{slot:%d, item:{%s}}""" % (i, str(x)))
    if out:
      return ', '.join(out)
    return ''

  def __str__(self, ) -> str:
    """This assumes the container is not in another container."""
    out = []
    if self.customName:
      out.append("""custom_name='%s'""" % str(self.customName))
    if self.lore:
      out.append("""lore=%s""" % str(self.lore))
    if self.contents:
      out.append("""container=[%s]""" % self._getContainer())
    return """%s[%s]""" % (self.itemId, ', '.join(out))

  @overload(AbstractItem, int)
  def append(self, item: AbstractItem, count: int) -> None:
    item.count = count
    self.contents.append(item)

  @overload(AbstractItem)
  def append(self, item: AbstractItem) -> None:
    if item.count > 0:
      return self.append(item, item.count)
    return self.append(item, 1)
