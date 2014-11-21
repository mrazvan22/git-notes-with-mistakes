from nose.tools import assert_equal, assert_raises, assert_almost_equal
from units import *

def test_building():

  two_cm = Unit('centimeters', 2)
  assert_equal(two_cm.value, 2)
  assert_equal(two_cm.unit, 'centimeters')
  
  three_ms = Unit('milliseconds', 3)
  assert_equal(three_ms.value, 3)
  assert_equal(three_ms.unit, 'milliseconds')

  with assert_raises(Exception) as e: 
    Unit('pint_of_ale',1)
 

def test_conversion():
  two_cm = Unit('centimeters', 2)
  two_cm_in_dm = two_cm.to('decimeters')
  assert_almost_equal(two_cm_in_dm.value, 0.2)
  assert_equal(two_cm_in_dm.unit, 'decimeters')
  
       
