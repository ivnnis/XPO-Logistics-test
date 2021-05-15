A = [['.','.','.','.','.','.','X','.','.','.'],
     ['.','.','.','#','#','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','#','#','#','#','#','.','.','.'],
     ['.','.','#','.','#','.','.','.','.','.'],
     ['.','#','#','.','#','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','0','.','.','.','.','.','.','.']]

class Dot:
     def __init__(self, cord, parent_cord, parent_gvalue):
          self.cord = cord
          self.target = target
          self.G = parent_gvalue + 1
          self.H = self.get_hvalue(cord)
          self.F = self.G + self.H
     
     def get_hvalue(self,cord):
          return abs(target[0] - cord[0]) + abs(target[1] - cord[0])


def search_dot(A, ch):
          i = 0
          for s in A:
               if ch in s:
                    return [i,s.index(ch)]
               i += 1


def append_active(cord, act):
     for dot in active_dots:
          if dot.cord == cord: 
               if dot.G > act.F:
                    dot.G = act.G
                    dot.parent_cord = act.cord
                    return 0
               else:
                    return 0
     try:
          if A[cord[0]][cord[1]] != '#':
               active_dots.append(Dot([cord[0],cord[1]], cord, act.G))
               A[act.cord[0]][act.cord[1]] = 'o'
     except:
          pass


start = search_dot(A,'0')
target = search_dot(A,'X')
act = Dot(start, start, -1)
active_dots = []
inactive_dots = []

while act.H != 0:
     
     append_active([act.cord[0]-1, act.cord[1]], act)
     append_active([act.cord[0], act.cord[1]+1], act)
     append_active([act.cord[0]+1, act.cord[1]], act)
     append_active([act.cord[0], act.cord[1]-1], act)
     
     inactive_dots.append(act)
     for dot in active_dots:
          if dot.F < act.F:
               act = dot
     active_dots.remove(dot)
print(A)


     

     













