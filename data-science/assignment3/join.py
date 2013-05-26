import MapReduce
import sys

"""
Join in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: order id
    # value: list of items and orders
    order = None
    items = []
    for v in list_of_values:
      if(v[0] == 'order'):
          order = v
      else:
          items.append(v)
          
    for item in items:
        mr.emit(order + item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
