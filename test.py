from api import get_city_from_ident
from api import get_city_from_name
from api import get_weather

def test_ident1():
    assert get_city_from_ident("00AK") == "Anchor Point"

def test_ident2():
    assert get_city_from_ident("PABV") == "Birchwood"

def test_ident3():
    assert get_city_from_ident("PAVD") == "Valdez"

def test_invalid_ident():
    assert get_city_from_ident("HEYY") == ""

def test_name1():
    assert get_city_from_name("Talkeetna Airport") == "Talkeetna"

def test_name2():
    assert get_city_from_name("Gulkana Airport") == "Gulkana"

def test_name3():
    assert get_city_from_name("Merrill Field") == "Anchorage"

def test_invalid_name():
    assert get_city_from_name("heyyy") == ""

def test_invalid1():
    assert get_weather("234") == 0

def test_invalid2():
    assert get_weather("") == 0
