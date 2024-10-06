"""Provides a list with fixed size and only one type (or None)"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import BaseObject, overload
from worktoy.desc import AttriBox, THIS
from worktoy.text import typeMsg

from moreworktoy import TypeMismatchException, OutOfBoundsException, \
  ItemNotFoundException, FullArrayException, EmptyArrayException


class FixedArray(BaseObject):
  """Provides a list with fixed size and only one type (or None)"""
  __iter_contents__ = None
  __content_list__ = None
  __fallback_type__ = str
  __fallback_length__ = 27

  length = AttriBox[int]()
  itemType = AttriBox[type](object)

  @overload(THIS)
  def __init__(self, other: FixedArray) -> None:
    self.__init__(other.length, other.itemType)
    for (i, item) in enumerate(other):
      self[i] = item

  @overload(int)
  def __init__(self, length: int) -> None:
    self.__init__(length, self.__fallback_type__, )

  @overload(type)
  def __init__(self, itemType: type) -> None:
    self.__init__(self.__fallback_length__, itemType)

  @overload()
  def __init__(self) -> None:
    self.__init__(self.__fallback_length__, self.__fallback_type__)

  @overload(type, int)
  def __init__(self, itemType: type, length: int) -> None:
    self.__init__(length, itemType)

  @overload(int, type)
  def __init__(self, length: int, itemType: type) -> None:
    self.itemType = itemType
    self.length = length
    self.__content_list__ = [None, ] * self.length

  def __iter__(self, ) -> FixedArray:
    """Implementation of the iterator protocol"""
    self.__iter_contents__ = [*self.__content_list__, ]
    return self

  def __next__(self, ) -> object:
    """Implementation of the iterator protocol"""
    if self.__iter_contents__:
      return self.__iter_contents__.pop(0)
    raise StopIteration

  def __str__(self, ) -> str:
    """Returns the array as a string."""
    clsName = self.itemType.__name__
    header = """FixedArray with %d of %s:""" % (self.length, clsName)
    body = '\n'.join([str(item) for item in self])
    return '\n'.join([header, body])

  def __getitem__(self, index: int) -> object:
    """Implementation of the indexable protocol"""
    if index < self.length:
      while index < 0:
        index += self.length
      return self.__content_list__[index]
    raise OutOfBoundsException

  def __setitem__(self, index: int, value: object) -> None:
    """Implementation of the indexable protocol"""
    if index < self.length:
      while index < 0:
        index += self.length
      if not isinstance(value, self.itemType):
        if value is not None:
          e = typeMsg('value', value, self.itemType)
          raise TypeMismatchException(e)
      self.__content_list__[index] = value
    else:
      raise OutOfBoundsException

  def __len__(self, ) -> int:
    """Returns the length of the array"""
    return sum([0 if item is None else 1 for item in self])

  def __contains__(self, other: object) -> bool:
    """Returns whether the item is in the array"""
    for item in self:
      if item == other:
        return True
    return False

  def __bool__(self) -> bool:
    """If every slot is None, the array is False. Otherwise, it is True"""
    for item in self:
      if item is not None:
        return True
    return False

  def append(self, other: object) -> None:
    """Appends the item to the array"""
    for (i, item) in enumerate(self):
      if item is None:
        self[i] = other
        return
    raise FullArrayException

  def extend(self, *args) -> None:
    """Appends the items to the array"""
    for arg in args:
      if not isinstance(arg, self.itemType):
        e = typeMsg('arg', arg, self.itemType)
        raise TypeMismatchException('arg', arg, self.itemType)
      self.append(arg)

  def remove(self, other: object) -> None:
    """Removes the item from the array"""
    for (i, item) in enumerate(self):
      if item == other:
        self[i] = None
        return
    raise ItemNotFoundException(other)

  def pop(self, index: int = None) -> object:
    """Pops removes the item at the index from the array. The index
    defaults to the last item different from None. """
    if self:
      if index is None:
        return self.pop(self.length - 1)
      if index < self.length:
        while index < 0:
          index += self.length
        while self[index] is None:
          index -= 1
          if not self:
            raise EmptyArrayException
        item = self[index]
        self[index] = None
        return item
      raise OutOfBoundsException(index, self.length)
    raise EmptyArrayException

  def insert(self, index: int, other: object, **kwargs) -> None:
    """Inserts the item at the index in the array"""
    if self[-1] is None:
      pass
    if index < self.length:
      while index < 0:
        index += self.length
      if self[index] is None:
        self[index] = other
        return
      if kwargs.get('_recursion', False):
        raise FullArrayException
      self.roll(1)
      return self.insert(index, other, _recursion=True)
    raise OutOfBoundsException(index, self.length)

  def roll(self, offset: int) -> None:
    """Rolls the array by the offset"""
    if offset > 0:
      _temp = [*self.__content_list__, ]
      self.__content_list__ = [_temp[-1], *(_temp[:-1]), ]
      offset -= 1
    elif offset < 0:
      _temp = [*self.__content_list__, ]
      self.__content_list__ = [*_temp[1:], _temp[0], ]
      offset += 1
    if offset:
      return self.roll(offset)

  def clear(self, ) -> list[object]:
    """Clears the array and returns the items removed."""
    out = []
    while self:
      out.append(self.pop())
    return out

  def bunchUp(self, endIndex: bool = None) -> None:
    """Bunches up the array"""
    if endIndex is None:
      return self.bunchUp(True)
    space = self.length - len(self) if endIndex else 0
    items = self.clear()  # In reverse order
    for (i, item) in enumerate(items[::-1]):
      self[i + space] = item
