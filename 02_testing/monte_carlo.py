from diffusion_model import energy
import matplotlib.pyplot as plt
import random as rnd

def move_particle(particle_array):
  
  n = len(particle_array)
  selected_particle = round(rnd.uniform(0, n))

  displacement = 0
  if rnd.random() < 0.5:
    displacement = 1
    
  particle_array[selected_particle] -= 1
  particle_array[selected_particle + displacement] += 1

def monte_carlo(density, temp):

  iterations = 5
  energy_0 = energy(density)

  density_1 = move_particle(density)
  energy_1 = energy(density)

  for i in range(iterations):
    if (energy_0 < energy_1):
      density = density_1
    else:
      p0 = exp(- (energy_1 - energy_0)/temp)
      p1 = random()
      if (p0 > p1):
        density = density_1

    plt.plot(density)


monte_carlo([2,4,6,5,1,5], 10.0)


