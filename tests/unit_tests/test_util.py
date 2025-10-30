from util.util import get_closest_file, flatten, preprocess_image

def test_flatten_empty_is_empty():
  assert flatten([]) == []

def test_flatten_single_list_is_same_list():
  assert flatten([[1, 2, 3]]) == [1, 2, 3]

def test_flatten_multiple_lists_concatenated():
  assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]