
class tab:
     def __init__(self, A):
          self.A = A
          self.start = search_dot('0')
          self.end = search_dot('X')
          self.a
     
     def search_dot(self, ch):
          i = 0
          for s in self.A:
               if ch in s:
                    return [i,s.index(ch)]
               i += 1
     
     def check_dot(self, i, j):
          try:
               if self.A[i][j] != "#":
                    return 1
          except:
               return 0
     
     def get_gvalue(self, dot):
          if dot[1] != self.start:
               return get_gvalue() + 1
          return 0
     

     











A = [['.','.','.','.','.','.','X','.','.','.'],
     ['.','.','.','#','#','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','#','#','.','#','#','.','.','.'],
     ['.','.','#','.','.','.','.','.','.','.'],
     ['.','#','#','.','#','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','0','.','.','.','.','.','.','.']]

