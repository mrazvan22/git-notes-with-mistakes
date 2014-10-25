from diffusion_model import energy
import matplotlib.pyplot as plt
import random as rnd
import math
import numpy
from mpl_toolkits.mplot3d import Axes3D

def move_particle(particle_array):

  n = len(particle_array)

  selected_particle = int(rnd.uniform(0, n))

  displacement = 0
  if rnd.random() < 0.5:
    displacement = 1

  while (selected_particle + displacement < 0 or selected_particle + displacement >= n or particle_array[selected_particle] == 0):
    selected_particle = int(rnd.uniform(0, n))

    displacement = 0
    if rnd.random() < 0.5:
      displacement = 1

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

def monte_carlo(density, temp):

  n = len(density)
  iterations = 30
  densities = numpy.zeros(shape=(iterations+1,n))
  densities[0] = density
  for i in range(iterations):
    energy_0 = energy(density)

    density_1 = move_particle(density)
    energy_1 = energy(density)

    if (energy_0 < energy_1):
      density = density_1
    else:
      p0 = math.exp(- (energy_1 - energy_0)/temp)
      p1 = rnd.random()
      if (p0 > p1):
        density = density_1

    densities[i + 1] = density

  return densities


densities = monte_carlo([2,4,6,5,1,5], 10.0)
print densities

print_density_3d(densities)

