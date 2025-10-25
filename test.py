import cv2

from recette import *
from numberReco import extraire_code_x_easyocr

DEFAULT_TEMPLATE_MATCHING_THRESHOLD = 0.95

class Template:
  """
  Une classe définissant un template.
  """
  def __init__(self, image_path, label, color):
    """
    Args:
      image_path (str): chemin de l'image template
      label (str): le label associé au template
      color (List[int]): la couleur associée au label (pour le tracé)
      matching_threshold (float): score minimal pour considérer la détection par template matching
    """
    self.image_path = image_path
    self.label = label
    self.color = color
    self.template = cv2.imread(image_path)
    self.template_height, self.template_width = self.template.shape[:2]

def item_extractor(image, template):
  imageForm = cv2.imread(image)
  template = Template(image_path=template, label="1", color=(0, 0, 255))
  template_matching = cv2.matchTemplate(template.template, imageForm, cv2.TM_CCOEFF_NORMED)
  _, max_val, _, max_loc = cv2.minMaxLoc(template_matching)
  if max_val >= DEFAULT_TEMPLATE_MATCHING_THRESHOLD:
    x, y = max_loc
    detection = {
      "TOP_LEFT_X": x,
      "TOP_LEFT_Y": y - 40,
      "BOTTOM_RIGHT_X": x + template.template_width,
      "BOTTOM_RIGHT_Y": y + template.template_height,
      "MATCH_VALUE": max_val,
      "LABEL": template.label,
      "COLOR": template.color
    }
    x1, y1 = detection["TOP_LEFT_X"], detection["TOP_LEFT_Y"]
    x2, y2 = detection["BOTTOM_RIGHT_X"], detection["BOTTOM_RIGHT_Y"]
    roi = imageForm[y1:y2, x1:x2]
    return roi
  return None

def number_extractor(image, template):
  template = Template(image_path=template, label="1", color=(0, 0, 255))
  template_matching = cv2.matchTemplate(template.template, image, cv2.TM_CCOEFF_NORMED)
  _, max_val, _, max_loc = cv2.minMaxLoc(template_matching)
  if max_val >= 0.7:
    x, y = max_loc
    detection = {
      "TOP_LEFT_X": x,
      "TOP_LEFT_Y": y,
      "BOTTOM_RIGHT_X": x + template.template_width + 40,
      "BOTTOM_RIGHT_Y": y + template.template_height - 5,
      "MATCH_VALUE": max_val,
      "LABEL": template.label,
      "COLOR": template.color
    }
    x1, y1 = detection["TOP_LEFT_X"], detection["TOP_LEFT_Y"]
    x2, y2 = detection["BOTTOM_RIGHT_X"], detection["BOTTOM_RIGHT_Y"]
    roi = image[y1:y2, x1:x2]
    return roi
  return None


for i in (item + equipement):
  v = item_extractor("coffre/21_10_25/3.jpg", i.img_path)
  if v is None:
    continue
  # cv2.imshow("Original", v)
  # cv2.waitKey(0)
  t = number_extractor(v, "img.jpg")
  if t is not None:
    d = extraire_code_x_easyocr(t)
    if d is None:
      cv2.imshow("Extraction test", t)
      cv2.waitKey(0)
    else:
      print(d)

