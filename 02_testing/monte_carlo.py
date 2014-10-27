from diffusion_model import *
import matplotlib.pyplot as plt
import random as rnd
import math
import numpy
from mpl_toolkits.mplot3d import Axes3D
from move_particle import *
from print_density import *

def monte_carlo(density, temp, iterations, energy_function):

  n = len(density)
  densities = numpy.zeros(shape=(iterations+1,n), dtype=numpy.int8)
  densities[0] = density
  for i in range(iterations):
    energy_0 = energy_function(density)

    density_1 = move_particle(density)
    energy_1 = energy_function(density_1)

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
  #densities = monte_carlo([2,4,6,5,1,5], 10.0, 5, energy)
  densities = monte_carlo([2,4,6,5,1,5], 10.0, 5, energy_aux)
  #print densities

  print_density_3d(densities)


if __name__ == "__main__":
    main()
