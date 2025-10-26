import os
from inv_gestion.recette import items, equipements
from imgExtraction.imgExtraction import item_extractor, number_extractor
from numberReco.numberReco import number_ocr
from inv_gestion.inventaire import Inventaire, show_diffrence, load_inventory

import cv2
import math

X_IMG = "ressources/x.jpg"

def compare(l, l_):
  ll = {n : i for (n, i) in l}
  for (name, qt) in l_:
    if name in ll:
      ll[name] = qt
      print(f"Mise à jour de {name}: {ll[name]} -> {qt}")
    else:
      ll[name] = qt
      print(f"Ajout de {name}: {qt}")
  return [(n, i) for (n, i) in ll.items()]

def get_closest_file(folder_path) -> str | None:
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

def main(coffre_path, logs_folder="ressources/logs"):
  old_path = get_closest_file(logs_folder)
  if old_path is None:
    print("Aucun fichier de log trouvé.")
    exit(1)
  old_inv = load_inventory(old_path)
  
  all_items = []
  for img in os.listdir(coffre_path):
    img_items = []
    for item in (items + equipements):
      result = item_extractor(os.path.join(coffre_path, img), item.img_path)
      if result is None:
        continue
      number_img = number_extractor(result, X_IMG)
      qt = 1
      if number_img is not None:
        n = number_ocr(number_img)
        if n is None:
          n = number_ocr(img_resize(number_img))
        if n is None:
          print(f"Échec de la reconnaissance du nombre pour l'image {img}.")
        if not n.isdigit():
          print(f"Nombre reconnu non valide '{n}' pour l'image {img}.")
        qt = int(n)
      img_items.append((item.name, qt))
      print(f"Détection de {qt} x {item.name} dans l'image {img}.")
    all_items = compare(all_items, img_items)
    print(f"File {img} treated.")

  inv = Inventaire(all_items)
  add, remove = old_inv.difference(inv)
  show_diffrence(add, remove, inv)

if __name__ == "__main__":
  main("ressources/coffre/21_10_25")