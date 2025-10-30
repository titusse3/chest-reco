from imgExtraction.imgExtraction import item_extractor, number_extractor
from numberReco.numberReco import number_ocr
from util.util import img_resize
from inv_gestion.recette import *
import math

from pathlib import Path
import pytest

import cv2

_BASE = str(Path(__file__).parent.resolve())

X_IMG = _BASE + "/ressource/x.jpg"

testdata = [
  (parchemin_basique, 1588),
  (parchemin_rare, 1558),
  (collier_t4, 7),
  (bottes_t4, 2),
  (ficelle, 1803),
  (pomme, 1304),
  (pavot, 62),
  (lingo_obsidienne, 21)
]

@pytest.mark.parametrize("template, number", testdata)
def test_extraction_info_image_work(template, number):
  img = _BASE + "/ressource/coffre.jpg"

  extraction = item_extractor(img, template.img_path)
  assert extraction is not None, f"L'extraction de {template.name} de l'objet a échoué."
  
  number_img = number_extractor(extraction, X_IMG)
  assert number_img is not None, f"Le nombre n'a pas pu être extrait."

  n = number_ocr(number_img)
  assert n is not None, f"Aucun nombre trouver."
  assert n.isdigit(), f"Le nombre extrait n'est pas un entier valide."
  assert int(n) == number, f"Le nombre extrait est incorrect."