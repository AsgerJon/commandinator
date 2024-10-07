"""TrimPattern enumerates the available armor trim patterns available for
decorating armor pieces in Minecraft. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import KeeNum, auto


class TrimPattern(KeeNum):
  """TrimPattern enumerates the available armor trim patterns available for
  decorating armor pieces in Minecraft. """

  NULL = auto()
  SENTRY = auto()
  VEX = auto()
  WILD = auto()
  COAST = auto()
  DUNE = auto()
  WAYFINDER = auto()
  RAISER = auto()
  SHAPER = auto()
  HOST = auto()
  WARD = auto()
  SILENCE = auto()
  TIDE = auto()
  SNOUT = auto()
  RIB = auto()
  EYE = auto()
  SPIRE = auto()
  FLOW = auto()
  BOLT = auto()
