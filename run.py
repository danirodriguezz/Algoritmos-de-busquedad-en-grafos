# Search methods

import search

roads = [
    ['A', 'B'], 
    ['O', 'E'], 
    ['G', 'Z'], 
    ['N', 'D'], 
    ['M', 'F']
    ]


def show_details(roads):
    """Displays a well-structured message for each search"""
    for inital, goal in roads:
        problem = search.GPSProblem(inital, goal, search.romania)
        print(f"\n-------------------- <Node:{problem.initial}> -> <Node:{problem.goal}> ----------------------")
        print("---- Busquedad en anchura ----")
        print(search.breadth_first_graph_search(problem).path())
        print("\n---- Busquedad en profundidad ----")
        print(search.depth_first_graph_search(problem).path())
        print("\n---- Busquedad por ramificación y acotación ----")
        print(search.branch_and_bound_search(problem).path())
        print("\n---- Busquedad por ramificación y acotación con subestimación ----")
        print(search.branch_and_bound_search_underestimation(problem).path())
        print(f"---------------------------------------------------------------------------------------------")


show_details(roads)