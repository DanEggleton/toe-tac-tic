import checkerboards as ch

class Match:

  
  def __init__(self):
    self.is_live = True
    self.boards = [ch.Checkerboard() for i in range(3)]
    self.whose_turn = 1
  
  
  def print(self):
    if not self.is_live:
      print()
      print('Final state of match')
      print('====================')
    print()
    print('State of match')
    print('--------------') 
    if self.is_live:
      print('Match is live')
    else:
      print('Match is over')
    print()
    print('State of games')
    print('--------------')
    for i, board in enumerate(self.boards):
      print(f'Board {i + 1}')
      board.print()
    print()
    if self.is_live:
      print(f'It\'s player {self.whose_turn}\'s turn')
    else:
      print()
      print('\*/ WINNER!!! \*/')
      print('=================')
      print(f'Player {self.whose_turn} is the winner!!!')
    print()
  

  def get_turn_decision(self, player):
    decision = {'board': None, 'row': None, 'column': None}
    while decision['board'] is None:
      # decide which board to play on
      board = input(f'Which board will player {player} play on? Enter 1, 2 or 3. ')
      if board not in ['1', '2', '3']:
        print('I was expecting 1, 2 or 3')
        print()
      elif not self.boards[int(board) - 1].is_live:
        print('Looks like that game has finished!')
        print()
      else:
        decision['board'] = int(board)
    while decision['row'] is None or decision['column'] is None:
      # decide which row and column to play on
      row = input(f'Which row will player {player} play on? Enter 1, 2 or 3. ')
      if row not in ['1', '2', '3']:
        print('I was expecting 1, 2 or 3')
        print()
        continue
      column = input(f'Which column will player {player} play on? Enter 1, 2 or 3. ')
      if column not in ['1', '2', '3']:
        print('I was expecting 1, 2 or 3')
        print()
        continue
      if self.boards[int(board) - 1].state[int(row) - 1, int(column) - 1] != 0:
        print('Looks like someone has already played there!')
        print()
        continue
      else:
        decision['row'] = int(row)
        decision['column'] = int(column)
    return decision

  
  def take_turn(self, player):
    decision = self.get_turn_decision(player)
    board, row, column = decision.values()
    coordinates = (row, column)
    self.boards[board - 1].update(coordinates, player)
    if True not in [board.is_live for board in self.boards]:
      self.is_live = False
    self.whose_turn = 3 - self.whose_turn
      