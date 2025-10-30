import os
import cv2

def get_closest_file(folder_path : str) -> str | None:
  files = os.listdir(folder_path)
  files.sort()
  if len(files) == 0:
    return None
  return os.path.join(folder_path, files[-1])

def preprocess_image(folder_path : str) -> list[str]:
  files = os.listdir(folder_path)
  l = []
  for f in files:
    path = os.path.join(folder_path, f)

    if not f.endswith('.jpg'):
      print(f"Le fichier {f} n'est pas une image JPG.")
      continue
    
    image = cv2.imread(path)
    h, w = image.shape[:2]

    target_w, target_h = 1920, 1080
    scale_w = target_w / w
    scale_h = target_h / h
    if not (w == 1920 and h == 1080):
      print(f"Redimensionnement de l'image {f}...")
      image = img_resize(image, min(scale_w, scale_h))
      cv2.imwrite(path, image)

    l.append(f)
  return l

def img_resize(image, scale_factor: float):
  h, w = image.shape[:2]
  new_w = max(1, int(round(w * scale_factor)))
  new_h = max(1, int(round(h * scale_factor)))
  image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
  print(f"Pixels: {w*h} -> {new_w*new_h} ({scale_factor:.3f}x linear)")
  return image

def flatten(xss : list[list]) -> list:
  """
  Flattens une liste de liste en une liste simple.
  """
  return [x for xs in xss for x in xs]
