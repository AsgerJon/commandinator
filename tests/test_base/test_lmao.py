"""Tests that unittests are correctly tested. Deep."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from unittest import TestCase


class TestLMAO(TestCase):
  """Tests that unittests are correctly tested. Deep."""

  def test_lmao(self) -> None:
    """Tests that unittests are correctly tested. Deep."""
    self.assertTrue((3.14159265358979 ** 3 - 31) ** 2 < 1e-03)
