from numberReco.numberReco import number_ocr

import pytest
from pathlib import Path

_BASE = Path(__file__).parent.resolve()

testdata = [
  (str(_BASE) + "/numberTest/1.png", "15461"),
  (str(_BASE) + "/numberTest/2.png", "2"),
  (str(_BASE) + "/numberTest/3.png", "3"),
  (str(_BASE) + "/numberTest/4.png", "1488"),
  (str(_BASE) + "/numberTest/5.png", "11"),
  (str(_BASE) + "/numberTest/6.png", "5")
]

@pytest.mark.parametrize("img_path,expected", testdata)
def test_number_recognition(img_path, expected):
  assert number_ocr(img_path) == expected