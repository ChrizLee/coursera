import MapReduce
import sys

"""
Friend count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    row = record[1]
    col = record[2]
    a_rows = 5
    b_cols = 5
    
    if(matrix == 'a'):
        for j in range(b_cols):
            mr.emit_intermediate((row, j), record)
    else:
        for i in range(a_rows):
            mr.emit_intermediate((i, col), record)

def reducer(key, list_of_values):
    row = key[0]
    col = key[1]
    a = []
    b = []
    val = 0
    for v in list_of_values:
      if(v[0] == 'a'):
          a.append(v)
      else:
          b.append(v)
    for v1 in a:
        vala = v1[3]
        cola = v1[2]
        valb = 0
        for v2 in b:
            if(v2[1] == cola):
                valb = v2[3]
        val += vala*valb
        
    mr.emit((row, col, val))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
