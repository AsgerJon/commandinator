"""AbstractCore provides a metaclass for abstract baseclasses. This class
is essentially a second order of abstraction as it defines what an
abstract baseclass should define. In this context, abstract baseclass
refers not to a particular family of classes related by subject,
but instead a particular pattern of class design. AbstractCore itself or a
subclass hereof defines what questions the abstract baseclass should
answer. Thus, instances of AbstractCore or its subclasses define
particular patterns. These patterns may then be instantiated to provide
subject specific abstract baseclasses."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
