"""AbstractField provides an abstract baseclass for field classes. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Never

from worktoy.base import FastObject
from worktoy.desc import AttriBox
from worktoy.text import monoSpace


class AbstractField(FastObject):
  """AbstractField provides an abstract baseclass for field classes. """

  __field_name__ = AttriBox[str]()
  __field_owner__ = AttriBox[type]()
  __pvt_name__ = AttriBox[str]()

  def __init__(self, pvtName: str) -> None:
    self.__pvt_name__ = pvtName

  def __set_name__(self, owner: type, name: str) -> None:
    """Automatically invoked upon creation of owning class. """
    self.__field_name__ = name
    self.__field_owner__ = owner

  def __get__(self, instance: object, owner: type) -> Any:
    """Automatically invoked upon attribute access. """
    if instance is None:
      return self
    return getattr(instance, self.__pvt_name__)

  def __set__(self, instance: object, value: Any) -> None:
    """Setter-method for the field. """
    setattr(instance, self.__pvt_name__, value)

  def __delete__(self, *_) -> Never:
    """Deleter-method is disabled"""
    e = """Instances of '%s', a subclass of AbstractField, does not support
    deletion of attributes.""" % self.__class__.__name__
    raise TypeError(monoSpace(e))
