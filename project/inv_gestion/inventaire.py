import json

class Inventaire:
  def __init__(self, list_of_tuples = []):
    self.stock = {}
    for (nom, quantite) in list_of_tuples:
      if nom in self.stock:
        raise ValueError(f"Article dupliqué dans l'inventaire: {nom}")
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

  def difference(self, other : "Inventaire") -> tuple[dict, dict]:
    """
    Compare l'inventaire actuel avec un autre inventaire.
    Retourne deux dictionnaires:
    - Le premier dictionnaire contient les articles ajoutés.
    - Le deuxième dictionnaire contient les articles retirés.
    """

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

  def show_difference(self, other : "Inventaire"):
    added, removed = self.difference(other)
    print("\033[1;34mAjouts:\033[0m")
    if added:
      for nom, quantite in added.items():
        print(f"• {nom}: \033[1;32m+{quantite}\033[0m ({self.stock.get(nom, 0)})")
    else:
      print("\033[1;33mAucun ajout.\033[0m")

    print("\033[1;34mRetraits:\033[0m")
    if removed:
      for nom, quantite in removed.items():
        print(f"• {nom}: \033[1;31m-{quantite}\033[0m ({self.stock.get(nom, 0)})")
    else:
      print("\033[1;33mAucun retrait.\033[0m")

  def __str__(self):
    s = ""
    for nom, quantite in self.stock.items():
      s += f"{nom}\t{quantite}\n"
    return s

  @staticmethod
  def load_inventory(filepath : str) -> "Inventaire":
    """
    Crée une instance d'Inventaire à partir d'un fichier sauvegardé au format 
    JSON. Retourne une instance d'Inventaire.
    """
    with open(filepath, "r", encoding="utf-8") as f:
      data = json.load(f)
    inv = Inventaire(data)
    return inv

  def save_inventory(self, filepath : str):
    """
    Sauvegarde l'inventaire dans un fichier au format JSON.
    L'inventaire est enregistré sous forme de liste de couples (nom, quantité).
    """
    with open(filepath, "w", encoding="utf-8") as f:
      json.dump(self.to_list(), f, ensure_ascii=False, indent=4)
