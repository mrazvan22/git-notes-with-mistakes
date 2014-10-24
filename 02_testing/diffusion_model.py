from numpy import array, any, sum

def energy(density, coeff=1.0):
  """ Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient.
  """
  # implementation goes here

  density = array(density)

  #for i in range(len(density) - 1 ):
  #  energy += density[i] * (density[i]- 1)


  if density.dtype.kind != 'i' and len(density) > 0:
    raise TypeError("Expected Array of integers");
  if any(density) < 0:
    raise ValueError("Expected array of *positive* integers")


  return sum(density * (density - 1)) * coeff * 0.5
