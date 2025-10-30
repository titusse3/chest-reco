from util.util import img_resize

import easyocr
import math

def correct_ocr_errors(text):
  corrections = {
    'l': '1', 'i': '1', 'I': '1', 'o': '0', 'O': '0', 'B': '8', 'S': '5', 
    's': '5', 'x' : '', 'k' : '', ' ' : ''
  }

  text = text.lower()

  for (old, new) in corrections.items():
    text = text.replace(old, new)
  return text

def number_ocr(image_path):
  reader = easyocr.Reader(['fr', 'en'], gpu=True)

  resultats = reader.readtext(image_path, detail=0)

  if len(resultats) >= 1 :
    num = resultats[0]
  else:
    image_resize = img_resize(image_path, math.sqrt(2))
    resultats = reader.readtext(image_resize, detail=0)
    num = resultats[0] if len(resultats) >= 1 else None

  if num is None:
    return None
  return correct_ocr_errors(num)