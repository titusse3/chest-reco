import os
from inv_gestion.recette import items, equipements
from imgExtraction.imgExtraction import item_extractor, number_extractor
from numberReco.numberReco import number_ocr
from inv_gestion.inventaire import Inventaire, show_diffrence, load_inventory

import argparse
import cv2
import math

X_IMG = "ressources/x.jpg"
LOGS_FOLDER="ressources/logs"
DESC_PROG = """
Programme de reconnaissance d'objets et de quantité dans un coffre Naruto RP 
Solve.
"""
PATH_DESC = """
Chemin vers le dossier contenant les images du coffre à analyser.
"""

def get_closest_file(folder_path : str) -> str | None:
  files = os.listdir(folder_path)
  files.sort()
  if len(files) == 0:
    return None
  return os.path.join(folder_path, files[-1])

def img_resize(image):
  h, w = image.shape[:2]
  scale = math.sqrt(2)  # ~1.414 to double total number of pixels
  new_w = max(1, int(round(w * scale)))
  new_h = max(1, int(round(h * scale)))
  image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
  print(f"Pixels: {w*h} -> {new_w*new_h} ({scale:.3f}x linear)")
  return image

def get_number_from_image(image):
  number_img = number_extractor(image, X_IMG)
  if number_img is not None:
    n = number_ocr(number_img)
    if n is None:
      n = number_ocr(img_resize(number_img))
    if n is None:
      print(f"Échec de la reconnaissance du nombre pour l'image {image}.")
      return None
    if not n.isdigit():
      print(f"Nombre reconnu non valide '{n}' pour l'image {image}.")
      return None
    return int(n)
  return 1

def main():
  parser = argparse.ArgumentParser(description=DESC_PROG)
  parser.add_argument('filename', type=str, help=PATH_DESC)
  coffre_path = parser.parse_args().filename

  old_path = get_closest_file(LOGS_FOLDER)
  if old_path is None:
    print("Aucun fichier de log trouvé.")
    exit(1)
  old_inv = load_inventory(old_path)
  
  all_items = []
  for item in (items + equipements):
    item_qt = []
    for img in os.listdir(coffre_path):
      result = item_extractor(os.path.join(coffre_path, img), item.img_path)
      if result is None:
        continue
      number = get_number_from_image(result)
      item_qt.append((item.name, number))
      print(f"Détection de {number} x {item.name} dans l'image {img}.")

    if not all(q == item_qt[0] for q in item_qt):
      print(f"Paramètres différents détectés pour {item.name}.")

    if item_qt == []:
      continue
    
    all_items.append((item.name, max(qt for (_, qt) in item_qt)))
    print(f"Item {item.name} treated.")

  inv = Inventaire(all_items)
  add, remove = old_inv.difference(inv)
  show_diffrence(add, remove, inv)

if __name__ == "__main__":
  main()