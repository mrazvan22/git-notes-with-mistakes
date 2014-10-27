import matplotlib.pyplot as plt
import random as rnd
from mpl_toolkits.mplot3d import Axes3D
import numpy


def print_density_3d(densities):

  if densities.dtype.kind != 'i' and len(densities) > 0:
    raise TypeError("Densities should be an array of *integers*.")
  # and the right values (positive or null)
  if (numpy.amin(densities) < 0):
    raise ValueError("Density should be an array of *positive* integers.")
  if densities.ndim != 2:
    raise ValueError("Densities should be an a *2-dimensional* array of positive integers.")

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

