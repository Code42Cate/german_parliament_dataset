def get_index(L):
  for i in xrange(0, len(L)):
    if L[i] > L[i+1]: 
      return i;
T = int(raw_input())
for i in xrange(1, T+1):
    N = int(raw_input())
    L = map(int, raw_input().split())
    done = False
    while done is False:
      done = True
      for e in xrange(0, len(L)-2):
        if L[e] > L[e+2]:
          temp = L[e]
          L[e] = L[e+2]
          L[e+2] = temp
          done = False
    if all(L[y] <= L[y+1] for y in xrange(len(L)-1)):
      print "Case #" + str(i) + ": OK"
    else:
      print "Case #" + str(i) + ": " + str(get_index(L))