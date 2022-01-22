import random

WIDTH = 800
HEIGHT = 600
NUM_POINTS_IN_X = 32
NUM_POINTS_IN_Y = 16
SPACING_X = WIDTH / (NUM_POINTS_IN_X + 1)
SPACING_Y = HEIGHT / (NUM_POINTS_IN_Y + 1)

points = []
lines = []

for i in range(NUM_POINTS_IN_Y):
  pinned = True if i == 0 else False
  # pinned = True
  prev_y = points[-1][1] if i > 0 else 0.0
  for j in range(NUM_POINTS_IN_X):
    prev_x = points[-1][0] if j > 0 else 0.0
    points.append((prev_x + SPACING_X, prev_y + SPACING_Y, pinned))

for i in range(0, NUM_POINTS_IN_Y):
  for j in range(0, NUM_POINTS_IN_X):
    p1_id = i * NUM_POINTS_IN_X + j

    if i > 0:
      p2_id = ((i - 1) * NUM_POINTS_IN_X) + j
      lines.append((p1_id, p2_id))

    if j > 0:
      p2_id = (i * NUM_POINTS_IN_X) + (j - 1)
      assert(p2_id < NUM_POINTS_IN_X * NUM_POINTS_IN_Y)
      lines.append((p1_id, p2_id))

    if i > 0 and j > 0:
      p2_id = ((i - 1) * NUM_POINTS_IN_X) + (j - 1)
      assert(p2_id < NUM_POINTS_IN_X * NUM_POINTS_IN_Y)
      lines.append((p1_id, p2_id))

  