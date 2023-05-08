import geometry as g
import draw as d
from rich import print
import argparse

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

def main(model):
  k, w = initialize(model.points, model.lines)
  d.draw(k, w)

if __name__ == "__main__":
  import importlib
  parser = argparse.ArgumentParser()
  parser.add_argument("--example", help="select example, one of [ball, box, cloth, double_pendulum]", default="ball")
  args = parser.parse_args()
  if args.example in ["ball", "box", "cloth", "double_pendulum"]:
    model = importlib.import_module(f"examples.{args.example}")
    main(model)
  else: 
    print("Invalid example, select one of (ball, box, cloth, double_pendulum)")
    exit(1)