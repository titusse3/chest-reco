from imgExtraction.imgExtraction import item_extractor

import pytest
from pathlib import Path

_BASE = Path(__file__).parent.resolve()

testdata = [
  (_BASE + "test_images/1.jpg", _BASE + "test_images/1/find.png", True),
  (_BASE + "test_images/1.jpg", _BASE + "test_images/2/find.png", True),
  (_BASE + "test_images/1.jpg", _BASE + "test_images/3/find.png", True),
  (_BASE + "test_images/1.jpg", _BASE + "test_images/4/find.png", True),
  (_BASE + "test_images/1.jpg", _BASE + "test_images/5/find.png", False),
]

@pytest.mark.parametrize("img,template,expected", testdata)
def test_item_extractor(img, template, expected):
  result = item_extractor(img, template)
  assert (result is not None) == expected