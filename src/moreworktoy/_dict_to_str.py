"""The 'dict2str' function converse a dictionary to a string. Unlike the
'json.dumps' function, no quotes are applied to the keys."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


def dict2str(data: dict) -> str:
  """Converse a dictionary to a string. Unlike the 'json.dumps' function,
  no quotes are applied to the keys."""
  out = []
  for key, value in data.items():
    if isinstance(value, dict):
      out.append("""%s: {%s}""" % (key, dict2str(value)))
    else:
      out.append("""%s: %s""" % (key, str(value)))
  return ', '.join(out)
