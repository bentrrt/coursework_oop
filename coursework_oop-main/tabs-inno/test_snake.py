#test_snake
import pytest
import library_item as lib

def test_list_all():
    result = lib.list_all()
    assert "01 Tom and Jerry" in result
    assert "02 Breakfast at Tiffany's" in result
    assert len(result.splitlines()) == 5  #list all 5 items

def test_get_name():
    assert lib.get_name("01") == "Tom and Jerry"
    assert lib.get_name("69") is None  # Invalid key should return None

def test_get_director():
    assert lib.get_director("02") == "Blake Edwards"
    assert lib.get_director("69") is None

def test_get_rating():
    assert lib.get_rating("03") == 2
    assert lib.get_rating("69") == -1  # Invalid key should return -1

def test_set_rating():
    lib.set_rating("03", 5)
    assert lib.get_rating("03") == 5


def test_increment_play_count():
    initial_play_count = lib.get_play_count("04")
    lib.increment_play_count("04")
    assert lib.get_play_count("04") == initial_play_count + 1

def test_get_url():
    assert lib.get_url("05") == "https://www.youtube.com/watch?v=0X94oZgJis4"
    assert lib.get_url("69") is None
