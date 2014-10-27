import random as rnd
import math
import numpy

def move_particle(particle_array):

  particle_array = numpy.array(particle_array)

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

