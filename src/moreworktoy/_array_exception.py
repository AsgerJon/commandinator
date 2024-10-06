"""FullArrayException class should be raised when trying to add an element
to a full instance of FixedArray. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.text import typeMsg, monoSpace


class FullArrayException(IndexError):
  """FullArrayException class should be raised when trying to add an element
  to a full instance of FixedArray. """

  def __init__(self, ) -> None:
    """Initializes a FullArrayException with the given index. """
    clsName = self.__class__.__name__
    e = """%s: Cannot add an item to a full array!""" % clsName
    IndexError.__init__(self, monoSpace(e))


class EmptyArrayException(IndexError):
  """EmptyArrayException class should be raised when trying to remove an
  element from an empty instance of FixedArray. """

  def __init__(self, ) -> None:
    """Initializes an EmptyArrayException with the given index. """
    clsName = self.__class__.__name__
    e = """%s: Cannot remove an item from an empty array!""" % clsName
    IndexError.__init__(self, monoSpace(e))


class ItemNotFoundException(KeyError):
  """ItemNotFoundException class should be raised when trying to access an
  item that is not in a FixedArray. """

  __bad_key__ = None

  def __init__(self, item: object = None) -> None:
    """Initializes an ItemNotFoundException with the given item. """
    clsName = self.__class__.__name__
    if item is not None:
      self.__bad_key__ = item
    KeyError.__init__(self)
    if item is None:
      e = """%s: Item not found in array!""" % clsName
    else:
      e = """%s: Item: '%s' not found in array!""" % (clsName, item)
    KeyError.__init__(self, monoSpace(e))

  def __str__(self) -> str:
    clsName = self.__class__.__name__
    item = str(self.__bad_key__)
    if self.__bad_key__ is None:
      return """%s: Item not found in array!""" % clsName
    return """%s: Item: '%s' not found in array!""" % (clsName, item)


class TypeMismatchException(TypeError):
  """TypeMismatchException class should be raised when trying to add an item
  to a FixedArray that does not match the array's type. """

  def __init__(self, *args) -> None:
    clsName = self.__class__.__name__
    if len(args) == 1:
      e = """%s: %s""" % (clsName, args[0])
    elif len(args) == 3:
      e = """%s: %s""" % (clsName, typeMsg(*args))
    else:
      e = """%s: Type mismatch!""" % clsName
    TypeError.__init__(self, monoSpace(e))


class OutOfBoundsException(IndexError):
  """OutOfBoundsException class should be raised when trying to access an
  index that is out of bounds for a FixedArray. """

  def __init__(self, *args) -> None:
    clsName = self.__class__.__name__
    intArgs = [arg for arg in args if isinstance(arg, int)]
    if not intArgs:
      e = """%s: Index out of bounds!""" % clsName
    elif len(intArgs) == 1:
      e = """%s: Index: '%d' is out of bounds!""" % (clsName, intArgs[0])
    else:
      _e = """%s: Index: '%d' is out of bounds for array of length: '%d'!"""
      e = _e % (clsName, *intArgs)
    IndexError.__init__(self, monoSpace(e))
