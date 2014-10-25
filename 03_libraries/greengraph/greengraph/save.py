### "save"
import matplotlib

def plot_points(points):
  matplotlib.use('Agg')
  import matplotlib.pyplot as plt
  with open('green.png','w') as green:
      green.write(show_green_in_png(map_at(*london_location,
          zoom=10,satellite=True)))

  plt.plot(points)
  plt.savefig('greengraph.png')

