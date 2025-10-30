import os
from inv_gestion.recette import items, equipements
from imgExtraction.imgExtraction import item_extractor, number_extractor
from numberReco.numberReco import number_ocr
from inv_gestion.inventaire import Inventaire
from util.util import get_closest_file, flatten, preprocess_image

import argparse
from multiprocessing import Pool
from functools import partial

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
DIFFERENCE_DESC = """
Option qui permet d'afficher les ajouts et retraits par rapport au dernier
inventaire sauvegardé dans le dossier des logs.
"""

def get_number_from_image(image) -> int | None:
  number_img = number_extractor(image, X_IMG)
  if number_img is None:
    return 1
  n = number_ocr(number_img)
  if n is None:
    print(f"Échec de la reconnaissance du nombre pour l'image {image}.")
    return None
  if not n.isdigit():
    print(f"Nombre reconnu non valide '{n}' pour l'image {image}.")
    return None
  return int(n)

def get_items_from_img(coffre_path : str, img : str):
  path = os.path.join(coffre_path, img)
  item_qt = []
  for item in (items + equipements):
    result = item_extractor(path, item.img_path)
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
  
  files = preprocess_image(coffre_path)

  all_items = []
  with Pool(len(files)) as p:
    results = p.map(partial(get_items_from_img, coffre_path), files)

    item_qt = flatten(results)
    all_items = list(set(item_qt))

  inv = Inventaire(all_items)
  print(inv, end="\n")
  if arg.diff:
    inv.show_difference(old_inv)

if __name__ == "__main__":
  main()