import pytest
import main_test as m

# define tests for normalize_lons

def test_normalize_lons_empty():
    assert m.normalize_lons([]) == []

def test_normalize_lons_ok():
    lon1 = [-179., -90., 0., 90., 180.]
    assert m.normalize_lons(lon1) == lon1

def test_normalize_lons_convert():
    lon2 = [0., 90., 180., 270., 360.]
    lon2_result = [0., 90., 180., -90., 0.]
    assert m.normalize_lons(lon2) == lon2_result

def test_normalize_lons_type_None():
    with pytest.raises(TypeError):
        _ = m.normalize_lons()

def test_normalize_lons_type_Int():
    with pytest.raises(TypeError):
        _ = m.normalize_lons(5)

def test_normalize_lons_type_String():
    with pytest.raises(TypeError):
        _ = m.normalize_lons('blabla')
    