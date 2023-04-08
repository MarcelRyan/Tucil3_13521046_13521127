from graph import Graph
from astar import astar

def main_program():
    # HEADER
    print('''\n
        =============================================
        UCS and A* Algorithm for Closest Path Finding
        =============================================
    ''')
    
    # INPUT FILENAME
    filename = input("Input filename [name].txt : ")
    graph = Graph(filename)

    # INPUT SOURCE
    source = input('Input source location name : ')
    
    # INPUT DESTINATION
    destination = input('Input destination location name : ')

    # INPUT ALGORITHM CHOICE
    print('''\n
        Algorithm :
        [1] Uniform Cost Search (UCS)
        [2] A*
    ''')
    choice = -1
    while choice < 1 or choice > 2 :
        choice = int(input("Input algorithm choices : "))
    
    # SELECT ALGORITHM
    result = None
    if choice == 1:
        pass
    else :
        result = astar(graph, source, destination)
    
    # PRINT RESULT
    print(result)
    distance = result.f 
    route = result.route.replace(' ', ' - ')
    print(f'''
        ============ RESULT ============
        Filename        : {filename}
        Source          : {source}
        Destination     : {destination}
        Distance (km)   : {distance}
        Route           : {route}
    ''')

    print('''
TO VIEW VISUALIZER:
[1] In web browser go to localhost:5000
[2] Red Point   : Source Location
    Green Point : Destination Location
    Blue Point  : Regular Location
    Blue Line   : Shortest Route from source to destination
    Green Line  : Regular Route
    ''')

    # DATA MANIPULATION FOR VISUALIZING
    shortest_route_name_list = route.split(' - ')

    # CREATE LIST OF ROUTES BETWEEN EACH ADJACENT IN SHORTEST ROUTE NAME LIST
    shortest_routes = []
    for i in range(len(shortest_route_name_list) - 1):
        start_loc = graph.findLocation(shortest_route_name_list[i])
        end_loc = graph.findLocation(shortest_route_name_list[i+1])
        start = (start_loc.getLat(), start_loc.getLong())
        end = (end_loc.getLat(), end_loc.getLong())
        route = [start, end]
        shortest_routes.append(route)
        shortest_routes.append(list(reversed(route)))

    # GET SOURCE AND DESTINATION LOCATION
    source_loc = graph.findLocation(source)
    destination_loc = graph.findLocation(destination)

    return graph.locations, graph.adjacencyMatrix, source_loc, destination_loc, shortest_routes
