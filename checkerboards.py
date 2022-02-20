import numpy as np

class Checkerboard:

  
  def __init__(self):
    self.state = np.zeros((3, 3), dtype=int)
    self.is_live = True

  
  def update(self, coordinates, player):
    (i, j) = coordinates
    self.state[i - 1, j - 1] = player
    # check if game now over
    diagonal_1 = self.state[0, 0] * self.state[1, 1] * self.state[2, 2]
    diagonal_2 = self.state[2, 0] * self.state[1, 1] * self.state[0, 2]
    rows = self.state.prod(axis=0)
    cols = self.state.prod(axis=1)
    diags = [diagonal_1, diagonal_2]
    lines = [*rows, *cols, *diags]
    # a straight line of o's <=> state 1, 1, 1 <=> product = 1
    # straigt line of x's <=> state 2, 2, 2 <=> product = 8
    # full board <=> product != 0
    if 1 in lines or 8 in lines or self.state.prod() != 0:
      self.is_live = False

  
  def print(self):
    np_state = self.state
    
    str_lkup = {0: ' ',
                1: 'o',
                2: 'x'}
    
    str_state = [[str_lkup[np_state[i, j]] for j in range(len(np_state[i]))] for i in range(len(np_state))]

    if self.is_live:
      print('This game is live')
    else:
      print('This game is over')
    for i in range(len(str_state)):
      print(*str_state[i], sep='|')
      if i < 2:
        print('-+-+-')
      else:
        print()
    