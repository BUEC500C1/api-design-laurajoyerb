from api import get_weather

def test1():
    assert get_weather("Boston") == 0

def test2():
    assert get_weather("London") == 0

def test3():
    assert get_weather("Blah Blah") == -1