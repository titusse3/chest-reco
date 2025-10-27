from inv_gestion.inventaire import Inventaire

def test_to_list_empty():
  i = Inventaire()
  l = i.to_list()
  assert l == [], "L'inventaire devrait être vide"

def test_to_list_nempty():
  l = [("pomme", 4), ("carrote", 2)]
  i = Inventaire(l)
  assert i.to_list() == l, "Le contenue doit être le même que l'inventaire"

def test_display_empty_inv(capsys):
  i = Inventaire()
  i.afficher()
  captured = capsys.readouterr()
  assert "Inventaire vide" in captured.out

def test_display_nempty_inv(capsys):
  l = [("pomme", 4), ("carrote", 2)]
  i = Inventaire(l)
  i.afficher()
  captured = capsys.readouterr()
  assert "pomme" in captured.out
  assert "4" in captured.out
  assert "carrote" in captured.out
  assert "2" in captured.out  