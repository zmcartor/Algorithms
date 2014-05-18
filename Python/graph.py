# from think complexity book

class Graph(dict):
  def __init__(self, vs=[], eg=[]):
    """create new graph vs is vertexes and eg is edges """
    for v in vs:
      self.add_vertex(v)

    for e in eg:
      self.add_edge(e)

  def add_vertex(self, v):
    self[v] = {}

  def add_edge(self, edge):
    """ add an edge to the graph. Pass an Edge object
        edge added to each node (non-directional) """
    node_one , node_two = edge
    self[node_one][node_two] = edge
    self[node_two][node_one] = edge


class Vertex(object):
  def __init__(self, label=''):
    self.label = label

  def __repr__(self):
    return 'Vertex: (%s)' % repr(self.label)

""" repr is legal python express. str is for humans """
  __str__ = __repr__


class Edge(tuple):
  def __new__(cls, edge1, edge2):
    return tuple.__new__(cls,edge1, edge2)

  def __repr__(self):
    return 'Edge: (%s, %s)' % (repr(self[0]) , repr(self[1]))

    __str__ = __repr__
  
