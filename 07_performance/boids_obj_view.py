from boids_object_oriented import *
from matplotlib import pyplot as plt
from matplotlib import animation
import time

def color(boid):
	if boid.species=="Eagle":
		return (1,0,0)
	return (0,0,1)

def animate(frame):
    boids.update()
    scatter.set_offsets([b.position for b in boids.boids])
    scatter.set_color([color(b) for b in boids.boids])

NR_BOIDS = 2000
NR_ITERATIONS = 1
start_time = time.time()

builder = ModelBuilder()
builder.start_model()
builder.set_flock_attraction(0.01/NR_BOIDS)
builder.set_avoidance_radius(10)
builder.set_formation_flying_radius(100)
builder.set_speed_matching_strength(0.125/NR_BOIDS)
builder.initialise_random(NR_BOIDS)
builder.add_eagle(0,0,0,50)

boids = builder.finish()


print 'Timing the script'
for i in range(NR_ITERATIONS):
  boids.update()

print (time.time() - start_time) * 1000, " ms"


#figure=plt.figure()
#axes=plt.axes(xlim=(-2000,1500), ylim=(-500,4000))
#scatter=axes.scatter([b.position[0] for b in boids.boids],[b.position[1] for b in boids.boids])

#anim = animation.FuncAnimation(figure, animate,
#        frames=50, interval=50)

#if __name__ == "__main__":
#    plt.show()
