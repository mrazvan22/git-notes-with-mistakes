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

def test_add():
  two_cm = Unit('centimeters', 2)
  three_cm = Unit('centimeters', 3)
  five_cm = two_cm + three_cm
  assert_equal(five_cm.value, 5)
  assert_equal(five_cm.unit, 'centimeters')

  four_dm = Unit('decimeters', 4)
  sum_m = two_cm + four_dm
  assert_almost_equal(sum_m.value, 0.42)
  assert_equal(sum_m.unit, 'meters')


def test_mult():
  two_cm = Unit('centimeters', 2)
  three_cm = Unit('centimeters', 3)
  six_cm = two_cm * three_cm
  assert_equal(six_cm.value, 6)
  assert_equal(six_cm.unit, 'centimeters')

  four_dm = Unit('decimeters', 4)
  mult_m = two_cm * four_dm
  print mult_m.unit, mult_m.value
  assert_almost_equal(mult_m.value, 0.008)
  assert_equal(mult_m.unit, 'meters')

def test_eq():
  two_cm = Unit('centimeters', 2)
  two_cm_in_dm = Unit('decimeters', 0.2)
  assert(two_cm == two_cm_in_dm)

  two_grams = Unit('grams',2)

  with assert_raises(IncompatibleUnitsError):
    two_grams == two_cm

def given_tests():
  meters = Unit('meters',1)
  kilometers = Unit('kilometers',1)
  seconds = Unit('seconds',1)
  minutes = Unit('minutes', 1)

  assert(5*meters == 0.005*kilometers)
  assert((60*seconds).to('minutes').value==1)
  assert((60*seconds).to('minutes').unit=='minutes')
  with assert_raises(IncompatibleUnitsError):
    5*meters+2*seconds
