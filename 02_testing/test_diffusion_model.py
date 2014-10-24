from diffusion_model import energy
from nose.tools import assert_raises, assert_almost_equal
def test_energy():
  """ Optional description for nose reporting """
  # Test something

def test_zero_energy_cases():
  density = [0,0,0]
  coeff = 1.0
  assert_almost_equal(energy(density, coeff), 0)

  density = [1,1,1]
  coeff = 0.0
  assert_almost_equal(energy(density, coeff), 0)

  
