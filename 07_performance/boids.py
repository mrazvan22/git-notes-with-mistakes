"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import time

# Deliberately terrible code for teaching purposes

start_time = time.time()

is_animated = True

ATTENUATION_MIDDLE = 0.01
SPEED_CONSTANT = 0.125
NR_BOIDS = 50
AWAY_LIMIT = 100

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))

def fly_middle(xvs, yvs, xs,ys):
  for i in range(len(xs)):
    for j in range(len(xs)):
      xvs[i]=xvs[i]+(xs[j]-xs[i])*ATTENUATION_MIDDLE/len(xs)
  for i in range(len(xs)):
    for j in range(len(xs)):
      yvs[i]=yvs[i]+(ys[j]-ys[i])*ATTENUATION_MIDDLE/len(xs)

  return (xvs, yvs)

def fly_away(xvs, yvs, xs,ys):
  for i in range(len(xs)):
    for j in range(len(xs)):
      if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < AWAY_LIMIT:
        xvs[i]=xvs[i]+(xs[i]-xs[j])
        yvs[i]=yvs[i]+(ys[i]-ys[j])

  return (xvs, yvs)

def match_speed(xvs,yvs,xs,ys):
  for i in range(len(xs)):
    for j in range(len(xs)):
      if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
        xvs[i]=xvs[i]+(xvs[j]-xvs[i])*SPEED_CONSTANT/len(xs)
        yvs[i]=yvs[i]+(yvs[j]-yvs[i])*SPEED_CONSTANT/len(xs)

  return (xvs, yvs)

def update_boids(boids):
  xs,ys,xvs,yvs=boids
  # Fly towards the middle
  xvs, yvs = fly_middle(xvs, yvs, xs,ys)
  # Fly away from nearby boids
  xvs, yvs = fly_away(xvs, yvs, xs,ys)
 # Try to match speed with nearby boids
  xvs, yvs = match_speed(xvs, yvs, xs,ys)

  # Move according to velocities
  for i in range(len(xs)):
    xs[i]=xs[i]+xvs[i]
    ys[i]=ys[i]+yvs[i]


boids_x=[random.uniform(-450,50.0) for x in range(NR_BOIDS)]
boids_y=[random.uniform(300.0,600.0) for x in range(NR_BOIDS)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(NR_BOIDS)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(NR_BOIDS)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)


if(is_animated):
  figure=plt.figure()
  axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
  scatter=axes.scatter(boids[0],boids[1])
  anim = animation.FuncAnimation(figure, animate,
                                 frames=50, interval=50, repeat=False)
else:
  nr_iterations = 500
  for i in range(nr_iterations):
    update_boids(boids)

  print start_time
  print (time.time() - start_time) * 1000, " ms"

if __name__ == "__main__":
    plt.show()
