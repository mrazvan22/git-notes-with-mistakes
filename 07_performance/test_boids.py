from boids import *
from nose.tools import assert_equals, assert_almost_equal
from numpy.testing import assert_array_equal, assert_array_almost_equal
import os
import yaml
import numpy as np

NR_BOIDS = 3

def test_fly_middle():
  xvs = [1,1,1]
  yvs = [1,1,1]
  xs = [1,2,3]
  ys = [1,2,3]

  xvs,yvs = fly_middle(xvs, yvs, xs,ys)

  assert_equals(xvs, [1.01, 1.0, 0.99])
  assert_equals(yvs, [1.01, 1.0, 0.99])

def test_fly_away():
  xvs = [1,1,1]
  yvs = [1,1,1]
  xs = [1,2,3]
  ys = [1,2,3]

  xvs,yvs = fly_away(xvs, yvs, xs,ys)

  assert_equals(xvs, [-2, 1, 4])
  assert_equals(yvs, [-2, 1, 4])


def test_match_speed():
  xvs = [1,1,1]
  yvs = [1,1,1]
  xs = [1,2,3]
  ys = [1,2,3]

  xvs,yvs = match_speed(xvs, yvs, xs,ys)

  assert_equals(xvs, [1, 1, 1])
  assert_equals(yvs, [1, 1, 1])


def test_opt():
  np.set_printoptions(precision=10)
  for i in range(10):

    print NR_BOIDS
    xs=np.array([random.uniform(-450,50.0) for x in range(NR_BOIDS)],dtype=np.float64)
    ys=np.array([random.uniform(300.0,600.0) for x in range(NR_BOIDS)],dtype=np.float64)
    xvs=np.array([random.uniform(0,10.0) for x in range(NR_BOIDS)],dtype=np.float64)
    yvs=np.array([random.uniform(-20.0,20.0) for x in range(NR_BOIDS)],dtype=np.float64)

    xs_o = np.copy(xs)
    ys_o = np.copy(ys)
    xvs_o = np.copy(xvs)
    yvs_o = np.copy(yvs)
  
    #print xvs, yvs
    #print xvs_o, yvs_o
    # compute new xvs yvs with slow and fast fly_middle
    xvs,yvs = fly_middle(xvs, yvs, xs,ys)
    fly_middle_opt(xvs_o, yvs_o, xs_o,ys_o)
    assert_array_almost_equal(xvs, xvs_o, verbose=True)
    assert_array_almost_equal(yvs, yvs_o)
  
    # same for fly_away
    xvs,yvs = fly_away(xvs, yvs, xs,ys)  
    #xvs_o,yvs_o = fly_away_opt(xvs_o, yvs_o, xs_o,ys_o)  
    fly_away_opt(xvs_o, yvs_o, xs_o,ys_o)  
    assert_array_almost_equal(xvs, xvs_o)
    assert_array_almost_equal(yvs, yvs_o)
    

    xvs,yvs = match_speed(xvs, yvs, xs,ys)
    #xvs_o,yvs_o = match_speed_opt(xvs_o, yvs_o, xs_o,ys_o)
    match_speed_opt(xvs_o, yvs_o, xs_o,ys_o)
    # will not be exactly the same, therefore decimal=1
    assert_array_almost_equal(xvs, xvs_o, decimal=1)
    assert_array_almost_equal(yvs, yvs_o, decimal=1)

      
def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    boid_data = (np.array(boid_data[0]),np.array(boid_data[1]),np.array(boid_data[2]),np.array(boid_data[3]), )
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.06)


test_opt()
