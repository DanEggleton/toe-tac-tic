import matches as m
 
m1 = m.Match()

m1.print()

while m1.is_live:
  m1.take_turn(m1.whose_turn)
  m1.print()
