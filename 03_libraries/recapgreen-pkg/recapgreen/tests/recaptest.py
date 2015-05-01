from nose.tools import assert_equals,assert_raises
import numpy as np
from ..recapgreen import *

def test_is_green():
  with assert_raises(ValueError):
    is_green(-1, 4, 5)


  with assert_raises(TypeError):
    is_green("abd", 4,6)

def test_map_at():
  with assert_raises(TypeError):
    map_at("a", 23)
