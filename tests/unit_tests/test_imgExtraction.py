from imgExtraction.imgExtraction import item_extractor

import pytest
from pathlib import Path
import cv2

_BASE = str(Path(__file__).parent.resolve())

testdata = [
  (_BASE + "/test_images/1.jpg", _BASE + "/test_images/1/find.png", True),
  (_BASE + "/test_images/1.jpg", _BASE + "/test_images/2/find.png", True),
  (_BASE + "/test_images/1.jpg", _BASE + "/test_images/3/find.png", True),
  (_BASE + "/test_images/1.jpg", _BASE + "/test_images/4/find.png", True),
  (_BASE + "/test_images/1.jpg", _BASE + "/test_images/5/find.png", False),
  (_BASE + "/test_images/1.jpg", _BASE + "/test_images/5/find.png", False),
]

@pytest.mark.parametrize("img,template,expected", testdata)
def test_item_extractor(img, template, expected):
  result = item_extractor(img, template)
  if not expected and result is not None:
    cv2.imshow("result", result)
    cv2.waitKey(0)
  assert (result is not None) == expected