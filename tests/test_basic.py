from pathlib import Path

def test_test_txt_contents():
    path = Path(__file__).resolve().parents[1] / "test.txt"
    assert path.read_text().strip() == "first test"
