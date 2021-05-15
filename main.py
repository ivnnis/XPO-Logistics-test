
class Dot:
     def __init__(self, cord, parent, parent_cord, parent_gvalue, target):
          self.cord = cord
          self.parent = parent
          self.parent_cord = parent_cord
          self.G = parent_gvalue + 1
          self.H = abs(target[0] - self.cord[0]) + abs(target[1] - self.cord[1])
          self.F = self.G + self.H


def search_dot(A, ch):
          i = 0
          for s in A:
               if ch in s:
                    return [i,s.index(ch)]
               i += 1


def append_active(A,cord, act, active_dots, target):
     for dot in active_dots:
          if dot.cord == cord: 
               if dot.G > act.F:
                    dot.G = act.G
                    dot.parent_cord = act.cord
                    return 0
               else:
                    return 0
     try:
          if A[cord[0]][cord[1]] != '#' and cord[0]>=0 and cord[1]>=0:
               active_dots.append(Dot(cord, act, act.cord, act.G, target))         
     except:
          pass


def print_path(A, dot): 
     if dot != []:
          A[dot.cord[0]][dot.cord[1]] = 'o'
          print_path(A, dot.parent)

def path(A):
     start = search_dot(A,'0')
     target = search_dot(A,'X')
     act = Dot(start, [], ['0','0'], -1, target)
     active_dots = []
     inactive_dots = []

     while act.H > 0:
          #определение соседних точек
          append_active(A, [act.cord[0]-1, act.cord[1]], act, active_dots, target)
          append_active(A, [act.cord[0], act.cord[1]+1], act, active_dots, target)
          append_active(A, [act.cord[0]+1, act.cord[1]], act, active_dots, target)
          append_active(A, [act.cord[0], act.cord[1]-1], act, active_dots, target)
          inactive_cords = []
          if act.cord not in inactive_cords:
               inactive_dots.append(act)
          for dot in inactive_dots:
               inactive_cords.append(dot.cord)
          
          active_dots[:] = [item for item in active_dots if item.cord not in inactive_cords]

          #Выбор точки с минимальным значением F из соседних 
          min = 100
          for dot in active_dots:    
               if dot.F <= min: 
                    act = dot
                    min = dot.F

     print_path(A, inactive_dots[-1])

     for i in A:
          print(' '.join(i))
     print('\n', 'число шагов: ', act.G, '\n\n')
     



A = [['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','X','.','.','.','.','.','.'],
     ['.','#','#','#','#','#','#','#','#','.'],
     ['.','#','0','.','.','.','.','.','.','.'],
     ['.','#','.','.','.','.','.','.','.','.'],
     ['.','#','.','.','.','.','.','.','.','.'],
     ['.','#','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.']]

path(A)

B = [['.','.','.','.','.','#','.','.','.','.'],
     ['.','.','.','#','.','#','.','#','.','.'],
     ['.','.','.','#','.','.','.','#','X','.'],
     ['.','#','#','#','#','#','#','#','#','.'],
     ['.','#','0','#','.','.','.','.','#','.'],
     ['.','#','.','#','.','#','.','.','#','.'],
     ['.','#','.','#','.','#','.','.','#','.'],
     ['.','#','.','#','.','#','.','.','#','.'],
     ['.','#','.','.','.','#','.','.','.','.'],
     ['.','.','.','.','.','#','.','.','.','.']]

path(B)     

C = [['.','.','.','X','.','.','.','.','.','.'],
     ['.','.','.','#','#','.','.','#','.','.'],
     ['.','.','.','.','.','.','.','#','.','.'],
     ['.','.','#','#','#','#','#','#','.','.'],
     ['.','.','#','.','.','.','.','#','.','.'],
     ['.','#','#','.','#','.','.','#','.','.'],
     ['.','.','#','.','.','.','.','#','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','0','.','.'],
     ['.','.','.','.','.','.','.','.','.','.']]

path(C)     













