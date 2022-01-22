from typing import Dict
from enum import Enum
from dataclasses import dataclass
from math import sqrt
import numpy as np
from copy import deepcopy

class Directions(Enum):
  X = 0
  Y = 1

@dataclass
class Point:
  "Point Class - Stores a point at location (x, y)"
  id:int
  position:np.ndarray
  prev_position:np.ndarray
  pinned:bool=False


"Alias to the Point class"
Vector = Point

@dataclass
class Line:
  "Line joining two points A and B, stores ids"
  pt_1_id:int
  pt_2_id:int
  length:float

@dataclass
class Kernel:
  "Stores all the geometry information"
  points:Dict[int, Point]
  lines:Dict[int, Line]
  num_points:int = 0
  num_lines:int = 0

@dataclass
class WorldConfig:
  gravity:float = 9.8
  down:np.ndarray = np.array([0.0, 1.0])
  dt:float = 0.1 # timestep size
  num_phys_iter:int = 3

def distance(a:Point, b:Point):
  "Distance between a and b"
  return np.linalg.norm(a.position - b.position)

def length(k:Kernel, l:Line):
  "Length of a line"
  return distance(l.pt_1_id, l.pt_2_id)

def add_point(k:Kernel, x: float, y: float, pinned:bool):
  k.points[k.num_points] = Point(k.num_points, np.array([x, y]), np.array([x-1, y-1]), pinned)
  k.num_points += 1

def get_point(k:Kernel, id:int):
  try:
    return k.points[id]
  except KeyError as e:
    raise Exception(f'Point {id} out of bounds, kernel only has {k.num_points} points.')

def add_line(k:Kernel, p1:Point, p2:Point):
  k.lines[k.num_lines] = Line(p1.id, p2.id, distance(p1, p2))
  k.num_lines += 1

def update_points(k:Kernel, w:WorldConfig):
  for p in k.points.values():
    if not p.pinned:
      prev_pos = deepcopy(p.position)
      p.position += p.position - p.prev_position
      p.position = p.position + w.down * w.gravity * w.dt * w.dt
      p.prev_position = prev_pos

def update_lines(k:Kernel, w:WorldConfig):
  for l in k.lines.values():
    p1 = get_point(k, l.pt_1_id)
    p2 = get_point(k, l.pt_2_id)
    
    center = (p1.position + p2.position) / 2

    direction = p1.position - p2.position
    length = np.linalg.norm(direction)
    if length > 0:
      direction = direction / length

    half_length = l.length / 2
    if not p1.pinned:
      p1.position = center + direction * half_length
    if not p2.pinned:
      p2.position = center - direction * half_length

def simulate_step(k:Kernel, w:WorldConfig):
  update_points(k, w)
  update_lines(k, w)

def simulate(k:Kernel, w:WorldConfig, num_steps:int):
  for s in range(num_steps):
    simulate_step(k, w)
  

  
