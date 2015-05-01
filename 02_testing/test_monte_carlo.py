from diffusion_model import energy
from nose.tools import assert_equal, assert_raises, assert_almost_equal
import numpy as np
from monte_carlo import *

def test_move_particle_empty():
  initial_array = [0,0,0]

  with assert_raises(ValueError) as exception:    
    MonteCarlo().move_particle(initial_array)


def test_move_particle_sum():
  initial_array = [2,4,7]
  sum_initial = sum(initial_array)
  final_array = MonteCarlo().move_particle(initial_array)

  assert_equal(sum(initial_array),sum(final_array))

def test_move_particle_edge():
  initial_array = [0,0,7]
  sim = MonteCarlo()
  final_array = sim.move_particle(initial_array)

  print final_array
  assert_equal(any(final_array - [0,1,6]), False)

def test_monte_carlo_zero_particles():
  density = [0,0,0,0]
  T = 2.0
  iterations = 20
  sim = MonteCarlo(T, iterations)

  with assert_raises(ValueError) as exception:    
    sim(density, energy)

def test_monte_carlo_one_particle():
  density = [0,0,1,0]
  T = 2.0
  iterations = 20
  sim = MonteCarlo(T, iterations)
  densities = sim(density, energy)
  constant_energy = energy(density)
  print constant_energy

  for i in range(len(density)):
    print "energies:", [energy(densities[i]), constant_energy]
    assert_equal(energy(densities[i]), constant_energy)


