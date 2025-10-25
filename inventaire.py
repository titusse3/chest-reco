import json

#### lingo_or, coeur_lune

class Inventaire:
  def __init__(self, list_of_tuples = []):
    self.stock = {}
    for (nom, quantite) in list_of_tuples:
      self.stock[nom] = quantite

  def to_list(self) -> list:
    """
    Retourne l'inventaire sous forme de liste de couples (nom, quantité).
    """
    return list(self.stock.items())

  def afficher(self):
    """
    Affiche l'inventaire en couleur avec des caractères Unicode, sans boîte.
    """
    if self.stock == {}:
      print("\033[1;31mInventaire vide.\033[0m")
      return

    print("\033[1;34m=== Inventaire ===\033[0m")
    
    for nom, quantite in self.stock.items():
      print(f"• {nom}: \033[1;32m{quantite}\033[0m")
    print()

  def craft(self, recette, n):
    """
    Essaie de réaliser la recette n fois.
    La recette doit fournir deux attributs : 'inputs' et 'outputs', 
    lesquels sont des listes de tuples (item, quantité).
    Retourne une nouvelle instance d'Inventaire avec le stock modifié 
    (les ingrédients retirés et les produits ajoutés), sans modifier l'inventaire courant.
    Si un ingrédient est insuffisant, affiche un message et retourne None.
    """
    new_inv = Inventaire()
    new_inv.stock = self.stock.copy()

    for (item, quantite) in recette.ingredients:
      return None

    for item, quantite in recette.ingredients:
      if new_inv.stock.get(item.name, 0) < quantite * n:
        print(f"Recette impossible: {item.name} en quantité insuffisante.")
        return None
      new_inv.stock[item.name] -= quantite * n

    res = recette.result_item
    new_inv.stock[res.name] = new_inv.stock.get(res.name, 0) + n

    return new_inv

  def difference(self, other : "Inventaire"):
    added = {}
    removed = {}
    all_items = set(self.stock.keys()).union(other.stock.keys())
    for item in all_items:
      self_qty = self.stock.get(item, 0)
      other_qty = other.stock.get(item, 0)
      if other_qty > self_qty:
        added[item] = other_qty - self_qty
      elif other_qty < self_qty:
        removed[item] = self_qty - other_qty
    return added, removed

def show_diffrence(added, removed, inv):
  print("\033[1;34mAjouts:\033[0m")
  if added:
    for nom, quantite in added.items():
      print(f"• {nom}: \033[1;32m+{quantite}\033[0m ({inv.stock.get(nom, 0)})")
  else:
    print("\033[1;33mAucun ajout.\033[0m")

  print("\033[1;34mRetraits:\033[0m")
  if removed:
    for nom, quantite in removed.items():
      print(f"• {nom}: \033[1;31m-{quantite}\033[0m ({inv.stock.get(nom, 0)})")
  else:
    print("\033[1;33mAucun retrait.\033[0m")

def save_inventory(inventory, filepath : str):
  """
  Sauvegarde l'inventaire dans un fichier au format JSON.
  L'inventaire est enregistré sous forme de liste de couples (nom, quantité).
  """
  with open(filepath, "w", encoding="utf-8") as f:
    json.dump(inventory.to_list(), f, ensure_ascii=False, indent=4)
  print(f"Inventaire sauvegardé dans {filepath}.")

def load_inventory(filepath : str):
  """
  Crée une instance d'Inventaire à partir d'un fichier sauvegardé au format JSON.
  Retourne une instance d'Inventaire.
  """
  with open(filepath, "r", encoding="utf-8") as f:
    data = json.load(f)
  inv = Inventaire(data)
  print(f"Inventaire chargé depuis {filepath}.")
  return inv

# = Test =======================================================================

def test_to_list_empty():
  i = Inventaire()
  l = i.to_list()
  assert l == [], "L'inventaire devrait être vide"

def test_to_list_nempty():
  l = [("pomme", 4), ("carrote", 2)]
  i = Inventaire(l)
  assert i.to_list() == l, "Le contenue doit être le même que l'inventaire"

