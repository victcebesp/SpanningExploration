# coding=utf-8
# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
on = search.GPSProblem('O', 'N', search.romania)


#print search.breadth_first_graph_search(ab).path()
#print search.depth_first_graph_search(ab).path()
print "Búsqueda y salto (AB)\n"
print search.branch_boundary_graph_search(ab).path()
print "Búsqueda y salto con subestimación(AB)\n"
print search.branch_boundary_graph_search_substimation(ab).path()
print "Búsqueda y salto (ON)\n"
print search.branch_boundary_graph_search(on).path()
print "Búsqueda y salto con subestimación(AB)\n"
print search.branch_boundary_graph_search_substimation(on).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
