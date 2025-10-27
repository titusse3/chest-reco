import cv2
import numpy as np
import os

class Item:
  def __init__(self, name, path):
    self.name = name
    if name != "lingo or" and name != "coeur de lune" and not os.path.exists(path):
      raise FileNotFoundError(f"L'image n'existe pas: {path}")
    self.img_path = path

  def display_text(self):
    width = 50
    border = "═" * width
    print(f"╔{border}╗")
    header = f"Fiche d'item: {self.name}"
    print(f"║{header:^{width}}║")
    print(f"╟{'-' * width}╢")
    line1 = f"Nom      : {self.name}"
    line2 = f"Chemin   : {self.img_path}"
    print(f"║ {line1:<{width-2}} ║")
    print(f"║ {line2:<{width-2}} ║")
    print(f"╚{border}╝")

class Recette:
  def __init__(self, result_item : Item, ingredients : list):
    self.result_item = result_item
    seen = set()
    for (item, qt) in ingredients:
      if item in seen:
        raise ValueError(f"Duplicate ingredient found: {item.name}")
      seen.add(item)
    self.ingredients = ingredients

  def display_text(self):
    border = "═" * 40
    print(f"╔{border}╗")
    print(f"║{'Recette pour : ' + self.result_item.name:^40}║")
    print(f"╟{'-' * 40}╢")
    for (item, qt) in self.ingredients:
      ingredient_display = f"{qt} x {item.name}"
      print(f"║ {ingredient_display:<38} ║")
    print(f"╚{border}╝")

  def display_image(self):
    header_height = 40
    cell_size = (200, 200)

    # Prépare les images des ingrédients
    ingredient_imgs = []
    for (ingredient, qt) in self.ingredients:
      img = cv2.imread(ingredient.img_path)
      if img is None:
        img = np.full((cell_size[1], cell_size[0], 3), 200, dtype=np.uint8)
      else:
        img = cv2.resize(img, cell_size)
      cv2.putText(img, f"{qt}x {ingredient.name}", (5, cell_size[1]-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
      ingredient_imgs.append(img)

    if ingredient_imgs:
      ingredients_collage = cv2.hconcat(ingredient_imgs)
    else:
      ingredients_collage = np.full((cell_size[1], cell_size[0], 3), 255, dtype=np.uint8)

    # Prépare l'image du produit final
    prod_img = cv2.imread(self.result_item.img_path)
    if prod_img is None:
      prod_img = np.full((cell_size[1], cell_size[0], 3), 200, dtype=np.uint8)
    else:
      prod_img = cv2.resize(prod_img, cell_size)
    cv2.putText(prod_img, self.result_item.name, (5, cell_size[1]-10),
          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Crée une image composite avec une entête pour étiqueter les sections
    collage_width = ingredients_collage.shape[1] + prod_img.shape[1]
    collage_height = cell_size[1]
    composite = np.full((header_height + collage_height, collage_width, 3), 255, dtype=np.uint8)

    # Ajoute l'entête pour les ingrédients
    ing_header = "Ingredients"
    (text_w, text_h), _ = cv2.getTextSize(ing_header, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
    ing_x = (ingredients_collage.shape[1] - text_w) // 2
    ing_y = (header_height + text_h) // 2
    cv2.putText(composite, ing_header, (ing_x, ing_y),
          cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # Ajoute l'entête pour le produit
    prod_header = "Produit"
    (text_w, text_h), _ = cv2.getTextSize(prod_header, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
    prod_x = ingredients_collage.shape[1] + (prod_img.shape[1] - text_w) // 2
    prod_y = (header_height + text_h) // 2
    cv2.putText(composite, prod_header, (prod_x, prod_y),
          cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # Place les images en dessous de l'entête
    composite[header_height:, :ingredients_collage.shape[1]] = ingredients_collage
    composite[header_height:, ingredients_collage.shape[1]:] = prod_img

    cv2.imshow("Recette", composite)
    cv2.waitKey(0)
    cv2.destroyAllWindows()