from inventaire import Inventaire, load_inventory, save_inventory, show_diffrence
from imgExtraction import img_extractor
from numberReco import extraire_code_x_easyocr
import cv2
from recette import *

def get_values(date):
  for img in ["1.jpg"]:
    l = []
    for i in (item + equipement):
      result = img_extractor(f"coffre/{date}/" + img, i.img_path)
      if result is not None:
        number = extraire_code_x_easyocr(result)
        if number is None:
          cv2.imshow("debug", result)
          cv2.waitKey(0)
          user_input = input(f"Entrez la quantité pour {i.name}: ")
          l.append((i.name, int(user_input)))
          cv2.destroyAllWindows()
        else:
          l.append( (i.name, int(number)) )
  return l

# print(get_values("20_10_25"))

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

if __name__ == "__main__":
  inv_old = load_inventory("logs/20_10_25.json")
  date = "21_10_25"

  l = []
  for img in ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]:
    l_ = []
    for i in (item + equipement):
      result = img_extractor(f"coffre/{date}/" + img, i.img_path)
      if result is not None:
        number = extraire_code_x_easyocr(result)
        if number is None:
          print("number none")
          # cv2.imshow("debug", result)
          # cv2.waitKey(0)
          # user_input = input(f"Entrez la quantité pour {i.name}: ")
          # l_.append((i.name, int(user_input)))
          # cv2.destroyAllWindows()
        else:
          l_.append( (i.name, int(number)) )
    l = compare(l, l_)
  
  inv_new = Inventaire(l)

  a, b = inv_old.difference(inv_new)

  show_diffrence(a, b, inv_new)
  
  save_inventory(inv_new, date)
