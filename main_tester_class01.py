"""Using __slots__ during inheritance. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import FastObject
from worktoy.desc import AttriBox
from worktoy.text import monoSpace


class Parent(FastObject):
  """Parent class. As a subclass of FastObject, instances of AttriBox are
  automatically replaced with appropriate entries in the __slots__
  attribute."""

  x = AttriBox[int]()
  y = AttriBox[int]()

  def __str__(self) -> str:
    """String representation"""
    clsName = self.__class__.__name__
    keys = getattr(self, '__slots__', None)
    vals = [getattr(self, k) for k in keys]
    keysVals = ', '.join(['%s: %s' % (k, v) for (k, v) in zip(keys, vals)])
    if keys is None:
      e = """lol, can't find __slots__ on %s""" % clsName
      raise RuntimeError(e)
    out = """Instance of %s with slots: %s""" % (clsName, keysVals)
    return monoSpace(out)


class Child(Parent):
  """Child class. As a subclass of Parent, instances of AttriBox are
  automatically replaced with appropriate entries in the __slots__
  attribute."""

  z = AttriBox[int]()
