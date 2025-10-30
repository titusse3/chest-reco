from numberReco.numberReco import number_ocr

import pytest
from pathlib import Path

_BASE = str(Path(__file__).parent.resolve())

testdata = [
  (_BASE + "/numberTest/1.png", "15461"),
  (_BASE + "/numberTest/2.png", "2"),
  (_BASE + "/numberTest/3.png", "3"),
  (_BASE + "/numberTest/4.png", "1488"),
  (_BASE + "/numberTest/5.png", "11"),
  (_BASE + "/numberTest/6.png", "5"),
  (_BASE + "/numberTest/7.png", "643"),
  (_BASE + "/numberTest/8.png", "15469"),
  (_BASE + "/numberTest/9.png", "5"),
  (_BASE + "/numberTest/10.png", "7"),
]

@pytest.mark.parametrize("img_path,expected", testdata)
def test_number_recognition(img_path, expected):
  assert number_ocr(img_path) == expected