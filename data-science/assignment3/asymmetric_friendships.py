import MapReduce
import sys
import MapReduce
import sys

"""
Asymmetric friend finding in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend = record[1]
    relation = [person, friend]
    relation.sort()
    mr.emit_intermediate(','.join(relation), (person, friend))

def reducer(key, list_of_values):
    if(len(list_of_values) < 2):
        mr.emit(list_of_values[0])
        mr.emit(list_of_values[0][::-1])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)