from geolocation import *
from url import map_at
from green_analysis import *
from points import *
from visualise import *

def main():
  geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
  london_location=geolocate("London")
  #print london_location


  map_response=map_at(51.5072, -0.1275, zoom=10)
  url=map_response.url
  print url

  from StringIO import StringIO
  print count_green_in_png(map_at(*london_location))


  print "green ammount along line:", [count_green_in_png(map_at(*location,zoom=10,satellite=True))
              for location in location_sequence(
                  geolocate("London"),
                  geolocate("Birmingham"),
                  10)]


  ### "save"
  import matplotlib
  matplotlib.use('Agg')
  import matplotlib.pyplot as plt
  with open('green.png','w') as green:
      green.write(show_green_in_png(map_at(*london_location,
          zoom=10,satellite=True)))

  plt.plot([
      count_green_in_png(
          map_at(*location,zoom=10,satellite=True))
            for location in location_sequence(
                geolocate("London"),
                geolocate("Birmingham"),10)])
  plt.savefig('greengraph.png')


if __name__ == "__main__":
  main()
