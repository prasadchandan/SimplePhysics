from dataclasses import dataclass
from .geometry import Kernel, Point, Line

@dataclass
class PhysicsPoint:
  position:Point
  prev_position:Point
  pinned:bool

@dataclass
class PhysicsStick:
  line:Line
  length:float

def simulate():
  k = Kernel()
  for pt in k.points:



