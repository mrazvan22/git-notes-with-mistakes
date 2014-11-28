"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random
from numpy import array

# Will now add an Eagle to Boids

class Boid(object):
    def __init__(self,x,y,xv,yv,owner,species="Starling"):
        self.position=array([x,y])
        self.velocity=array([xv,yv])
        self.owner=owner
        self.species=species

    def interaction(self,other):
        delta_v=array([0.0,0.0])
        separation=other.position-self.position
        separation_sq=separation.dot(separation)

        if other.species=="Eagle":
            # Flee the Eagle
            if separation_sq < self.owner.eagle_avoidance_radius**2:
                delta_v-=(separation*self.owner.eagle_fear)/separation.dot(separation)
                return delta_v

        # Fly towards the middle
        delta_v+=separation*self.owner.flock_attraction

        # Fly away from nearby boids
        if separation_sq < self.owner.avoidance_radius**2:
            delta_v-=separation

        # Try to match speed with nearby boids
        if separation_sq < self.owner.formation_flying_radius**2:
            delta_v+=(other.velocity-self.velocity)*self.owner.speed_matching_strength

        return delta_v

class Eagle(Boid):

   def interaction(self,other):
        delta_v=array([0.0,0.0])
        separation=other.position-self.position
        separation_sq=separation.dot(separation)

        # Hunt the boids
        delta_v+=separation*self.owner.eagle_hunt_strength
        return delta_v


class ModelBuilder():
  def start_model(self):
    self.model = Boids(0,0,0,0)

  def set_flock_attraction(self, attraction):
    self.model.flock_attraction = attraction

  def set_avoidance_radius(self, avoidance):
    self.model.avoidance_radius = avoidance

  def set_formation_flying_radius(self, radius):
    self.model.formation_flying_radius = radius

  def set_speed_matching_strength(self, strength):
    self.model.speed_matching_strength = strength

  def initialise_random(self, count):
    self.model.initialise_random(count)

  def add_eagle(self, x,y,xv,yv):
    self.model.add_eagle(x,y,xv,yv)

  def finish(self):
    # make sure object is fully constructed before returning it
    assert(self.model.flock_attraction != 0)
    assert(self.model.avoidance_radius != 0)
    assert(self.model.formation_flying_radius != 0)
    assert(self.model.speed_matching_strength != 0)
    assert(self.model.boids != None)

    return self.model

# Deliberately terrible code for teaching purposes
class Boids(object):
    def __init__(self,
           flock_attraction,avoidance_radius,
            formation_flying_radius,speed_matching_strength,
            eagle_avoidance_radius=100, eagle_fear=5000, eagle_hunt_strength=0.00005):
        self.flock_attraction=flock_attraction
        self.avoidance_radius=avoidance_radius
        self.formation_flying_radius=formation_flying_radius
        self.speed_matching_strength=speed_matching_strength
        self.eagle_avoidance_radius=eagle_avoidance_radius
        self.eagle_fear=eagle_fear
        self.eagle_hunt_strength=eagle_hunt_strength


    def initialise_random(self,count):
        self.boids=[Boid(random.uniform(-450,50.0),
                random.uniform(300.0,600.0),
                random.uniform(0,10.0),
                random.uniform(-20.0,20.0),self) for i in range(count)]

    def add_eagle(self,x,y,xv,yv):
        self.boids.append(Eagle(x,y,xv,yv,self,species="Eagle"))

    def initialise_from_data(self,data):
        self.boids=[Boid(x,y,xv,yv,self) for x,y,xv,yv in zip(*data)]

    def update(self):
        for me in self.boids:
            delta_v=array([0.0,0.0])
            for him in self.boids:
                delta_v+=me.interaction(him)
            # Accelerate as stated
            me.velocity+=delta_v
            # Move according to velocities
            me.position+=me.velocity


