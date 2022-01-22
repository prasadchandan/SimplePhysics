import geometry as g
import draw as d
from rich import print

points = [
  (400, 20, True),
  (300, 30, False),
  (200, 30, False)
]

lines = [
  (0, 1),
  (1, 2)
]

def initialize():
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
  k, w = initialize()
  d.draw(k, w)
  print(k)
  print(w)

if __name__ == "__main__":
  main()