import easyocr

def extraire_code_x_easyocr(image_path):
  reader = easyocr.Reader(['fr', 'en'], gpu=True)

  resultats = reader.readtext(image_path, detail=0)
  
  if len(resultats) >= 1 :
    num = resultats[0]
  else:
    return None

  corrections = {
    'l': '1', 'i': '1', 'I': '1', 'o': '0', 'O': '0', 'B': '8', 'S': '5', 's': '5', 'x' : ''
  }

  num = num.lower()

  for (old, new) in corrections.items():
    num = num.replace(old, new)
  if num.isdigit():
    return num
  return None

