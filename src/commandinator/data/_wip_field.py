"""WIPField class provides a placeholder for names yet to be implemented. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Never

from worktoy.base import BaseObject


class FieldNotYetImplemented(NotImplementedError):
  """An exception for fields that are not yet implemented. """
  pass


class WIPField(BaseObject):
  """A placeholder for names yet to be implemented. """

  __field_name__ = None
  __field_owner__ = None

  def __set_name__(self, owner: type, name: str) -> None:
    self.__field_owner__ = owner
    self.__field_name__ = name

  def __get__(self, *_) -> Never:
    raise FieldNotYetImplemented(self.__field_name__)

  def __set__(self, *_) -> Never:
    raise FieldNotYetImplemented(self.__field_name__)
