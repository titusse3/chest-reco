import os
from inv_gestion.recette import items, equipements
from imgExtraction.imgExtraction import img_extractor, number_extractor
from numberReco.numberReco import number_ocr

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

def main(coffre_path, logs_folder="logs"):
  old_path = get_closest_file(logs_folder)
  if old_path is None:
    print("Aucun fichier de log trouvé.")
    exit(1)
  
  all_items = []
  for img in os.listdir(coffre_path):
    img_items = []
    for item in (items + equipements):
      result = img_extractor(os.path.join(coffre_path, img), item.img_path)
      if result is not None:
        number_img = number_extractor(result, "")
        if number_img is not None:
          n = number_ocr(number_img)
          if n is not None and n.isdigit():
            qt = int(n)
          img_items.append((item.name, qt))
          print(f"Détection de {qt} x {item.name} dans l'image {img}.")
        else:
          img_items.append((item.name, 1))
          print(f"Détection de 1 x {item.name} dans l'image {img}.")

if __name__ == "__main__":
  main()