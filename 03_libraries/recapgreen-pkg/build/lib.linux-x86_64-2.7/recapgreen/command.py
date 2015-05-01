from argparse import ArgumentParser
from recapgreen import *
import sys

def process():

  parser = ArgumentParser(description = "Generate recapgraph by Raz before python exam")

  #parser.add_argument('--help')
  #args = parser.parse_args
  
  if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print "Help for recapgraph"  
  else:
    run()

if __name__ == "__main__":
  process()
