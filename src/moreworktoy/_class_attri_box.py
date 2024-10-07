"""ClassAttriBox provides a subclass for AttriBox allowing classes to
define a class specific attribute shared between every instance of the
class. An abstract baseclass would own instances of ClassAttriBox allowing
or requiring subclasses to provide a specific value for the attribute."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import BaseObject


class ClassAttriBox(BaseObject):
  """ClassAttriBox provides a subclass for AttriBox allowing classes to
  define a class specific attribute shared between every instance of the
  class. An abstract baseclass would own instances of ClassAttriBox allowing
  or requiring subclasses to provide a specific value for the attribute."""

  __abstract_base_class__ = None
  __class_field_name__ = None

  def __set_name__(self, owner: type, name: str) -> None:
    self.__class_field_name__ = name
    self.__abstract_base_class__ = owner
 