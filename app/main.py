import geometry as g
import draw as d
from rich import print

def initialize(points, lines):
  w = g.WorldConfig()
  k = g.Kernel(points={}, lines={})

  for p in points:
    g.add_point(k, *p)
  
  for l in lines:
    p1 = g.get_point(k, l[0])
    p2 = g.get_point(k, l[1])
    g.add_line(k, p1, p2)
  
  return k, w

def main():
  # from examples import double_pendulum as current
  # from examples import cloth as current
  from examples import ball as current
  k, w = initialize(current.points, current.lines)
  d.draw(k, w)
  print(k)
  print(w)

if __name__ == "__main__":
  main()