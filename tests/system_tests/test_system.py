from main import main
import sys

def test_main_function(capsys):
  with open("tests/system_tests/test_files/response.txt", "r", encoding="utf-8") as rfile:
    expected_output = rfile.read()
    sys.argv = ["tests/system_tests/test_files/coffre"]
    main()
    captured = capsys.readouterr()
    assert captured.out == expected_output
