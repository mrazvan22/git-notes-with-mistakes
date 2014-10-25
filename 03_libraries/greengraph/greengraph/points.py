### "points"

from numpy import linspace
def location_sequence(start,end,steps):
  # Would actually prefer this if steps
  # were deduced from zoomlevel
  # But need projection code for that
  lats=linspace(start[0],end[0],steps)
  longs=linspace(start[1],end[1],steps)
  return zip(lats,longs)


