from inv_gestion.item import Item

import pytest
from pathlib import Path

_BASE = str(Path(__file__).parent.resolve())

def test_excepetion_when_image_doesnt_exists():
  with pytest.raises(FileNotFoundError):
    Item("pomme", "path/that/does/not/exist.jpg")

def test_exception_when_image_exists():
  Item("name", f"{_BASE}/test_images/1.jpg")