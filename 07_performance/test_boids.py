from boids import *
from nose.tools import assert_equals, assert_almost_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.01)

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


