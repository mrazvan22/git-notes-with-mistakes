from diffusion_model import energy
import matplotlib.pyplot as plt
import random as rnd
import math

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

def monte_carlo(density, temp):

  iterations = 500
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

    plt.plot(density)


monte_carlo([2,4,6,5,1,5], 10.0)


