import pytest
from calculator import square
def test_positive():
  assert square(2)==4
  assert square(3)==9

def test_negative():
  assert square(-4)==16

def test_str():
  with pytest.raises(TypeError):
    square("cat")


