from imgExtraction.imgExtraction import item_extractor, number_extractor

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

x_img = _BASE + "/test_images/x.jpg"
test_number_extractor = [
  (_BASE + "/test_images/1/result.png"),
  (_BASE + "/test_images/2/result.png"),
  (_BASE + "/test_images/3/result.png"),
  (_BASE + "/test_images/4/result.png"),
  (_BASE + "/test_images/6/result.png"),
]

@pytest.mark.parametrize("file", test_number_extractor)
def test_number_extractor(file, x_img=x_img):
  file = cv2.imread(file)
  result = number_extractor(file, x_img)
  cv2.imshow("result", result)
  cv2.waitKey(0)
  user_verif = bool(input("Did the number extraction work? (y/n) ") == "y")
  assert (result is not None) == user_verif