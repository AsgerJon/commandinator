"""AbstractData provides a base class for data entries in the JSON format
used in Minecraft command syntax."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import json
from abc import abstractmethod

from worktoy.base import BaseObject
from worktoy.desc import AttriBox
from worktoy.text import typeMsg


class AbstractData(BaseObject):
  """AbstractData provides a base class for data entries in the JSON format
  used in Minecraft command syntax."""
