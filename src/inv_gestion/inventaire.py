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
