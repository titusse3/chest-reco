import os
from inv_gestion.recette import items, equipements
from imgExtraction.imgExtraction import item_extractor, number_extractor
from numberReco.numberReco import number_ocr
from inv_gestion.inventaire import Inventaire

import argparse
import cv2
import math
from multiprocessing import Pool
from functools import partial

X_IMG = "ressources/x.jpg"
LOGS_FOLDER="ressources/logs"
DESC_PROG = """
Programme de reconnaissance d'objets et de quantité dans un coffre Naruto RP 
Solve.
"""
PATH_DESC = """
Chemin vers le dossier contenant les images du coffre à analyser.
"""
DIFFERENCE_DESC = """
Option qui permet d'afficher les ajouts et retraits par rapport au dernier
inventaire sauvegardé dans le dossier des logs.
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

def get_items_from_img(coffre_path : str, img : str):
  item_qt = []
  for item in (items + equipements):
    result = item_extractor(os.path.join(coffre_path, img), item.img_path)
    if result is None:
      continue
    number = get_number_from_image(result)
    item_qt.append((item.name, number))
  
  return item_qt

def main():
  parser = argparse.ArgumentParser(description=DESC_PROG)
  parser.add_argument('filename', type=str, help=PATH_DESC)
  parser.add_argument('-d', '--diff', action='store_true', help=DIFFERENCE_DESC)
  arg = parser.parse_args()
  coffre_path = arg.filename

  old_path = get_closest_file(LOGS_FOLDER)
  if old_path is None:
    print("Aucun fichier de log trouvé.")
    exit(1)
  old_inv = Inventaire.load_inventory(old_path)
  
  files = os.listdir(coffre_path)
  files_number = len(files)

  all_items = []
  with Pool(files_number) as p:
    results = p.map(partial(get_items_from_img, coffre_path), files)

    item_qt = [pair for sub in results for pair in (sub or [])]
    for (item, qt) in item_qt:
      if (item, qt) not in all_items:
        all_items.append((item, qt))
      else:
        print(f"Doublon détecté pour l'item {item} dans l'image.")

  inv = Inventaire(all_items)
  print(inv, end="\n")
  if arg.diff:
    inv.show_difference(old_inv)

if __name__ == "__main__":
  main()