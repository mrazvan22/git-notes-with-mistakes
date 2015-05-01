import random as rnd
import math
import numpy as np
from diffusion_model import energy


class MonteCarlo(object):

  def __init__(self, temperature=100, itermax=100):
    self.temp = temperature
    """ Temperature at which to run the simulation"""
    self.iterations = itermax
    """Maximum number of iterations"""

  def __call__(self, density, energy):

    currArray = density
    allArrays = np.zeros((self.iterations, len(density)), int)
    for i in range(self.iterations):
      currEnergy = energy(currArray)
      newArray = self.move_particle(currArray)
      newEnergy = energy(newArray)
      
      p0 = np.exp(-(newEnergy - currEnergy)/self.temp)
      if newEnergy < currEnergy or p0 > np.random.rand():
        currArray = newArray
  
      allArrays[i,:] = currArray

    return allArrays


  def move_particle(self, particle_array):

    particle_array = np.array(particle_array)

    if particle_array.dtype.kind != 'i' and len(particle_array) > 0:
      raise TypeError("particle_array should be an array of *integers*.")
      # and the right values (positive or null)
    if any(particle_array < 0):
      raise ValueError("particle_array should be an array of *positive* integers.")
    if particle_array.ndim != 1:
      raise ValueError("particle_array should be an a *1-dimensional* array of positive integers.")
    if not any(particle_array):
      raise ValueError("particle array must contain at least one particle")

    n = len(particle_array)
    print "n=",n

    selected_particle = int(rnd.uniform(0, n))

    displacement = -1
    if rnd.random() < 0.5:
      displacement = 1

    while (selected_particle + displacement < 0 or selected_particle + displacement >= n or particle_array[selected_particle] == 0):
      selected_particle = int(rnd.uniform(0, n))

      displacement = -1
      if rnd.random() < 0.5:
        displacement = 1

    #print "selected_particle=", selected_particle
    #print "displacement=", displacement
    particle_array[selected_particle] -= 1
    particle_array[selected_particle + displacement] += 1

    return particle_array

