from src.strength import avaliar_forca

def test_fraca():
    assert avaliar_forca("abc") == "fraca"

def test_fraca_2():
    assert avaliar_forca("abcdefg") == "fraca"

def test_media():
    assert avaliar_forca("Senha123") == "media"

def test_media_2():
    assert avaliar_forca("Senha!!!") == "media"

def test_forte():
    assert avaliar_forca("Senha123!") == "forte"