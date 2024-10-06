"""Advanced instantiation of the 'AttriBox' class."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.desc import AttriBox, THIS
from worktoy.meta import BaseObject


class Test(BaseObject):
  """Test class for the 'AttriBox' class."""

  def __init__(self, **kwargs):
    """Initialize the 'Test' class."""
