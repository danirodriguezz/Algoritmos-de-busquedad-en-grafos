# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path(search.romania))
print(search.depth_first_graph_search(ab).path(search.romania))
print(search.branch_and_bound_search(ab).path(search.romania))