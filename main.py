
def search(ch):
     i = 0
     for s in A:
          if ch in s:
               return [i,s.index(ch)]
          i += 1


def dist(dot, end, nonactive):
     try:
          if A[dot[0]][dot[1]] != '#':
               if dot in nonactive:
                    return (abs(end[0]-dot[0]) + abs(end[1]-dot[1]))*2
               else:
                    return abs(end[0]-dot[0]) + abs(end[1]-dot[1])
          else:
               return 100
     except:
          return 100

def path(A):
     start = search('0')
     end = search('X')
     active_dot = start
     nonactive = []

     for st in A:
          print(' '.join(st))
     print()   

     while active_dot != end:
          next_dots = [[active_dot[0],active_dot[1]-1],
                    [active_dot[0]-1,active_dot[1]],
                    [active_dot[0],active_dot[1]+1],
                    [active_dot[0]+1,active_dot[1]],]
          next_dots_dist = list(map(lambda x: dist(x, end, nonactive), next_dots))
          nonactive.append(active_dot)
          A[active_dot[0]][active_dot[1]] = 'o'
          active_dot = next_dots[next_dots_dist.index(min(next_dots_dist))]

     for st in A:
          print(' '.join(st))



A = [['.','.','.','.','.','.','X','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.','.'],
     ['.','.','#','#','#','.','.','.','.','.'],
     ['.','.','.','.','#','.','.','.','.','.'],
     ['.','.','.','.','#','.','.','.','.','.'],
     ['.','.','.','.','#','.','.','.','.','.'],
     ['.','.','.','.','#','.','.','.','.','.'],
     ['.','.','.','.','#','.','.','.','.','.'],
     ['.','.','0','.','.','.','.','.','.','.']]


path(A)
