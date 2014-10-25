from diffusion_model import energy
import matplotlib.pyplot as plt
import random as rnd
import math
import numpy
from mpl_toolkits.mplot3d import Axes3D

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

def print_density_3d(densities):
  iterations, n = numpy.shape(densities)
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  colours = ['r', 'g', 'b', 'y'] * iterations
  for z in range(iterations):
    c = colours[z]
    xs = numpy.arange(n)
    ys = densities[z]

    # define the colours
    cs = [c] * len(xs)

    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.6)

  ax.set_xlabel('particle array')
  ax.set_ylabel('iteration')
  ax.set_zlabel('# particles')

  plt.show()

def monte_carlo(density, temp, iterations):

  n = len(density)
  densities = numpy.zeros(shape=(iterations+1,n), dtype=numpy.int8)
  densities[0] = density
  for i in range(iterations):
    energy_0 = energy(density)

    density_1 = move_particle(density)
    energy_1 = energy(density_1)

    print [energy_0, energy_1]
    print density
    if (energy_1 < energy_0):
      density = density_1
    else:
      p0 = math.exp(- (energy_1 - energy_0)/temp)
      p1 = rnd.random()
      if (p0 > p1):
        density = density_1

    densities[i + 1] = density

  return densities


def main():
  densities = monte_carlo([2,4,6,5,1,5], 10.0, 5)
  #print densities

  print_density_3d(densities)


if __name__ == "__main__":
    main()
