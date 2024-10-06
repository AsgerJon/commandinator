"""The 'moreworktoy' package provides functionality missing from
'worktoy', but implemented here ad hoc. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ._dict_to_str import dict2str
from ._array_exception import FullArrayException, EmptyArrayException
from ._array_exception import ItemNotFoundException, TypeMismatchException
from ._array_exception import OutOfBoundsException
from ._fixed_array import FixedArray
