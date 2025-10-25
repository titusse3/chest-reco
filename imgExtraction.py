import cv2
import numpy as np

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

def img_extractor(image, template):
  image = cv2.imread(image)
  template = Template(image_path=template, label="1", color=(0, 0, 255))
  template_matching = cv2.matchTemplate(template.template, image, cv2.TM_CCOEFF_NORMED)
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
    roi = image[y1:y2, x1:x2]
    return roi
  return None
    # cv2.imwrite("extracted_rectangle.jpg", roi)
  
if __name__ == "__main__":
  folder = "ressource"
  r = img_extractor("coffre/4.jpg", "ressource/commun/laine.png")
  if r is not None:
    original = cv2.imread("coffre1.jpg")
    if original is None:
      print("Erreur en lisant coffre1.jpg")
    else:
      # Redimensionner l'image originale pour qu'elle soit bien plus petite (par exemple à 30% de sa taille)
      scale_factor = 0.3
      small_original = cv2.resize(original, (int(original.shape[1] * scale_factor), int(original.shape[0] * scale_factor)))
      
      # Ajuster la taille de r pour qu'elle corresponde à la hauteur de l'image réduite
      if r.shape[0] != small_original.shape[0]:
        ratio = small_original.shape[0] / r.shape[0]
        new_width = int(r.shape[1] * ratio)
        r = cv2.resize(r, (new_width, small_original.shape[0]))
      
      # Mettre les deux images côte à côte dans le même affichage
      combined = np.hstack((small_original, r))
      cv2.imshow("Images cote a cote", combined)
      cv2.waitKey(0)
    # cv2.imshow("Detections", r)
    cv2.waitKey(0)
  else:
    print("No detection")


# image_with_detections = image.copy()
# cv2.rectangle(
#   image_with_detections,
#   (detection["TOP_LEFT_X"], detection["TOP_LEFT_Y"]),
#   (detection["BOTTOM_RIGHT_X"], detection["BOTTOM_RIGHT_Y"]),
#   detection["COLOR"],
#   2,
# )
# cv2.putText(
#   image_with_detections,
#   f"{detection['LABEL']} - {detection['MATCH_VALUE']:.2f}",
#   (detection["TOP_LEFT_X"] + 2, detection["TOP_LEFT_Y"] + 20),
#   cv2.FONT_HERSHEY_SIMPLEX,
#   0.5,
#   detection["COLOR"],
#   1,
#   cv2.LINE_AA,
# )
# cv2.imwrite("result.jpeg", image_with_detections)
