"""  Terribly good code for performance purposes! by Razvan Valentin Marinescu
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import time

is_animated = False

ATTENUATION_MIDDLE = 0.01
SPEED_CONSTANT = 0.125
NR_BOIDS = 50
AWAY_LIMIT = 100
MATCH_SPEED_LIMIT = 10000

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))

def fly_middle(xvs, yvs, xs,ys):
  NR_BOIDS = len(xs)
  for i in range(NR_BOIDS):
    for j in range(NR_BOIDS):
      xvs[i]=xvs[i]+(xs[j]-xs[i])*ATTENUATION_MIDDLE/NR_BOIDS
  for i in range(NR_BOIDS):
    for j in range(NR_BOIDS):
      yvs[i]=yvs[i]+(ys[j]-ys[i])*ATTENUATION_MIDDLE/NR_BOIDS

  return (xvs, yvs)

def fly_middle_opt(xvs, yvs, xs,ys):
  NR_BOIDS = len(xs)
  for i in range(NR_BOIDS):
      xvs[i] += sum(xs-xs[i])*ATTENUATION_MIDDLE/NR_BOIDS
      yvs[i] += sum(ys-ys[i])*ATTENUATION_MIDDLE/NR_BOIDS


def fly_away(xvs, yvs, xs,ys):
  for i in range(len(xs)):
    for j in range(len(xs)):
      if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < AWAY_LIMIT:
        xvs[i]=xvs[i]+(xs[i]-xs[j])
        yvs[i]=yvs[i]+(ys[i]-ys[j])

  return (xvs, yvs)


def fly_away_opt(xvs, yvs, xs,ys):
  for i in range(len(xs)):
    close_points = (xs - xs[i])**2 + (ys - ys[i])**2 < AWAY_LIMIT      
    xvs[i] += sum(xs[i]-xs[close_points])
    yvs[i] += sum(ys[i]-ys[close_points])


def match_speed(xvs,yvs,xs,ys):
  for i in range(len(xs)):
    for j in range(len(xs)):
      if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < MATCH_SPEED_LIMIT:
        xvs[i]=xvs[i]+(xvs[j]-xvs[i])*SPEED_CONSTANT/len(xs)
        yvs[i]=yvs[i]+(yvs[j]-yvs[i])*SPEED_CONSTANT/len(xs)

  return (xvs, yvs)


# note that this implementation is not exactly the same as the one before, because the original implementation updates xvs at each j iteration, which is quite bad and undesirable. That resulted in 'quick update' bias for the first eagles in the list.
def match_speed_opt(xvs,yvs,xs,ys):
  NR_BOIDS = len(xs)
  for i in range(NR_BOIDS):
    close_points = ((xs - xs[i])**2 + (ys - ys[i])**2) < MATCH_SPEED_LIMIT
    xvs[i] += sum(xvs[close_points]-xvs[i])*SPEED_CONSTANT/NR_BOIDS
    yvs[i] += sum(yvs[close_points]-yvs[i])*SPEED_CONSTANT/NR_BOIDS


def update_boids(boids):
  xs,ys,xvs,yvs=boids

  # Fly towards the middle
  fly_middle_opt(xvs, yvs, xs,ys)
  #xvs, yvs = fly_middle(xvs, yvs, xs,ys)

  # Fly away from nearby boids
  fly_away_opt(xvs, yvs, xs,ys)
  #xvs, yvs = fly_away(xvs, yvs, xs,ys)

 # Try to match speed with nearby boids
  match_speed_opt(xvs, yvs, xs,ys)
  #xvs, yvs = match_speed(xvs, yvs, xs,ys)

  # Move according to velocities
  xs += xvs
  ys += yvs


if __name__ == "__main__":
  start_time = time.time()

  boids_x=np.array([random.uniform(-450,50.0) for x in range(NR_BOIDS)])
  boids_y=np.array([random.uniform(300.0,600.0) for x in range(NR_BOIDS)])
  boid_x_velocities=np.array([random.uniform(0,10.0) for x in range(NR_BOIDS)])
  boid_y_velocities=np.array([random.uniform(-20.0,20.0) for x in range(NR_BOIDS)])
  boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)


  if(is_animated):
    figure=plt.figure()
    axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
    scatter=axes.scatter(boids[0],boids[1])
    anim = animation.FuncAnimation(figure, animate,
                                   frames=50, interval=50, repeat=False)
    plt.show()
  else:
    print 'Timing the script'
    nr_iterations = 500
    for i in range(nr_iterations):
      update_boids(boids)

    print start_time
    print (time.time() - start_time) * 1000, " ms"


