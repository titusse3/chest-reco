from inv_gestion.inventaire import Inventaire

import json
import pytest

def test_to_list_empty():
  i = Inventaire()
  l = i.to_list()
  assert l == [], "L'inventaire devrait être vide"

def test_to_list_nempty():
  l = [("pomme", 4), ("carrote", 2)]
  i = Inventaire(l)
  assert i.to_list() == l, "Le contenue doit être le même que l'inventaire"

def test_create_inv_with_duplicates():
  l = [("pomme", 4), ("carrote", 2), ("pomme", 3)]
  with pytest.raises(ValueError):
    i = Inventaire(l)

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

def test_save_inventory(tmp_path):
  l = [("pomme", 4), ("carrote", 2)]
  i = Inventaire(l)
  filepath = tmp_path / "test_inv.json"
  i.save_inventory(str(filepath))
  assert filepath.exists()
  content = filepath.read_text(encoding="utf-8")
  assert '"pomme"' in content
  assert '"carrote"' in content
  assert json.loads(content), "Le contenu du fichier JSON est incorrect"

def test_to_str():
  l = [("pomme", 4), ("carrote", 2)]
  i = Inventaire(l)
  s = str(i)
  assert s == "pomme\t4\ncarrote\t2\n", "Représentation en chaîne incorrecte"