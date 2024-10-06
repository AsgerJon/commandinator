"""The 'commandinator.data' package provides functionality for creating
data objects for minecraft commands and data packs. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ._wip_field import WIPField, FieldNotYetImplemented
from ._abstract_data import AbstractData
from ._color import Color
from ._format_flags import FormatFlags
from ._text import Text
from ._lore import Lore
